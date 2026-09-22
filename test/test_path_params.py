"""Tests for how path parameter values reach the Server API."""

import threading
import unittest
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Callable, Optional

from fingerprint_server_sdk import (
    Configuration,
    EventUpdate,
    InvalidParameterError,
)
from fingerprint_server_sdk.api.fingerprint_api import FingerprintApi

API_KEY = '<secret-api-key>'

RESPONSE_BODY = b'{"event_id": "1708102555327.NLOjmg", "timestamp": 1708102555327}'


@dataclass(frozen=True)
class PathParamOperation:
    """An operation that takes an ID as a URL path parameter."""

    name: str
    param: str
    prefix: str
    call: Callable[[FingerprintApi, str], object]


OPERATIONS = (
    PathParamOperation(
        name='get_event',
        param='event_id',
        prefix='/events/',
        call=lambda api, event_id: api.get_event(event_id),
    ),
    PathParamOperation(
        name='update_event',
        param='event_id',
        prefix='/events/',
        call=lambda api, event_id: api.update_event(event_id, EventUpdate(suspect=True)),
    ),
    PathParamOperation(
        name='delete_visitor_data',
        param='visitor_id',
        prefix='/visitors/',
        call=lambda api, visitor_id: api.delete_visitor_data(visitor_id),
    ),
)


class StubServer:
    """A local HTTP server recording the request target it was last asked for."""

    def __init__(self) -> None:
        self.request_target: Optional[str] = None
        server = self

        class Handler(BaseHTTPRequestHandler):
            def _handle(self) -> None:
                server.request_target = self.path.split('?', 1)[0]

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(RESPONSE_BODY)))
                self.end_headers()
                self.wfile.write(RESPONSE_BODY)

            do_GET = _handle
            do_PATCH = _handle
            do_DELETE = _handle

            def log_message(self, *args: object) -> None:
                """Silence the default logging."""

        self._server = HTTPServer(('127.0.0.1', 0), Handler)
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)

    def start(self) -> None:
        self._thread.start()

    def stop(self) -> None:
        self._server.shutdown()
        self._server.server_close()
        self._thread.join()

    def reset(self) -> None:
        self.request_target = None

    @property
    def base_path(self) -> str:
        host, port = self._server.server_address[:2]
        return f'http://{host!s}:{port!s}/base'


class TestPathParams(unittest.TestCase):
    """Test path parameter handling for every operation that takes an ID in the path."""

    server: StubServer

    @classmethod
    def setUpClass(cls) -> None:
        cls.server = StubServer()
        cls.server.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.stop()

    def setUp(self) -> None:
        self.server.reset()
        self.api = FingerprintApi(Configuration(api_key=API_KEY, host=self.server.base_path))

    def call(self, operation: PathParamOperation, value: str) -> Optional[str]:
        """Run operation with value and return the request target the server received."""
        self.server.reset()
        operation.call(self.api, value)
        return self.server.request_target

    def test_value_is_encoded_into_a_single_path_segment(self) -> None:
        """A value travels as one opaque segment, so it cannot inject path structure."""
        cases = (
            ('path', '../events', '..%2Fevents'),
            ('nested path', '../../base/events', '..%2F..%2Fbase%2Fevents'),
            ('leading slash', '/events/123', '%2Fevents%2F123'),
            ('absolute url', 'https://test.com/events', 'https%3A%2F%2Ftest.com%2Fevents'),
            ('protocol relative url', '//test.com', '%2F%2Ftest.com'),
            ('query injection', '123?limit=1', '123%3Flimit%3D1'),
            ('fragment injection', '123#fragment', '123%23fragment'),
            ('whitespace', 'hello world', 'hello%20world'),
            ('non ascii', 'é', '%C3%A9'),
            ('pre-encoded', '..%2Fevents', '..%252Fevents'),
        )

        for operation in OPERATIONS:
            for name, value, encoded in cases:
                with self.subTest(operation=operation.name, case=name):
                    request_target = self.call(operation, value)

                    self.assertEqual(f'/base{operation.prefix}{encoded}', request_target)

    def test_dot_in_value_is_not_touched(self) -> None:
        """Test dots in the value stay literal."""
        cases = (
            ('event id', '1708102555327.NLOjmg'),
            ('three dots', '...'),
            ('leading dot', '.leading'),
            ('trailing dot', 'trailing.'),
        )

        for operation in OPERATIONS:
            for name, value in cases:
                with self.subTest(operation=operation.name, case=name):
                    request_target = self.call(operation, value)

                    self.assertEqual(f'/base{operation.prefix}{value}', request_target)

    def test_dot_segment_is_rejected_without_sending_a_request(self) -> None:
        """`.` and `..` are refused"""
        for operation in OPERATIONS:
            for value in ('.', '..'):
                with self.subTest(operation=operation.name, value=value):
                    self.server.reset()

                    with self.assertRaises(InvalidParameterError) as context:
                        operation.call(self.api, value)

                    self.assertIsNone(self.server.request_target)
                    self.assertEqual(operation.param, context.exception.parameter)
                    self.assertEqual(value, context.exception.value)
                    self.assertIn(operation.param, str(context.exception))

    def test_empty_value_does_not_address_the_collection(self) -> None:
        """An empty ID leaves a trailing slash"""
        for operation in OPERATIONS:
            with self.subTest(operation=operation.name):
                request_target = self.call(operation, '')

                self.assertEqual(f'/base{operation.prefix}', request_target)
                self.assertNotEqual(f'/base{operation.prefix.rstrip("/")}', request_target)


if __name__ == '__main__':
    unittest.main()
