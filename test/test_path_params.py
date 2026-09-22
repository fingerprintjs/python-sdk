# coding: utf-8

"""Tests for how path parameter values reach the Server API."""

import threading
import unittest

from collections import namedtuple
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Optional

from fingerprint_pro_server_api_sdk import (Configuration, EventsUpdateRequest,
                                            InvalidParameterError)
from fingerprint_pro_server_api_sdk.api.fingerprint_api import FingerprintApi  # noqa: E501

API_KEY = 'private_key'

EMPTY_BODY = b'{}'
EVENT_BODY = b'{"products": {}}'
VISITS_BODY = b'{"visitorId": "visitor_id", "visits": []}'

PathParamOperation = namedtuple(
    'PathParamOperation', ['name', 'param', 'prefix', 'call', 'response_body']
)

OPERATIONS = (
    PathParamOperation(
        name='get_event',
        param='request_id',
        prefix='/events/',
        call=lambda api, request_id: api.get_event(request_id),
        response_body=EVENT_BODY,
    ),
    PathParamOperation(
        name='update_event',
        param='request_id',
        prefix='/events/',
        call=lambda api, request_id: api.update_event(
            EventsUpdateRequest(linked_id='linked_id'), request_id
        ),
        response_body=EMPTY_BODY,
    ),
    PathParamOperation(
        name='get_visits',
        param='visitor_id',
        prefix='/visitors/',
        call=lambda api, visitor_id: api.get_visits(visitor_id),
        response_body=VISITS_BODY,
    ),
    PathParamOperation(
        name='delete_visitor_data',
        param='visitor_id',
        prefix='/visitors/',
        call=lambda api, visitor_id: api.delete_visitor_data(visitor_id),
        response_body=EMPTY_BODY,
    ),
)


class StubServer:
    """A local HTTP server recording the request target it was last asked for."""

    def __init__(self):
        self.request_target = None  # type: Optional[str]
        self.response_body = EMPTY_BODY
        server = self

        class Handler(BaseHTTPRequestHandler):
            def _handle(self):
                server.request_target = self.path.split('?', 1)[0]

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(server.response_body)))
                self.end_headers()
                self.wfile.write(server.response_body)

            do_GET = _handle
            do_PUT = _handle
            do_DELETE = _handle

            def log_message(self, *args):
                """Silence the default logging."""

        self._server = HTTPServer(('127.0.0.1', 0), Handler)
        self._thread = threading.Thread(target=self._server.serve_forever)
        self._thread.daemon = True

    def start(self):
        self._thread.start()

    def stop(self):
        self._server.shutdown()
        self._server.server_close()
        self._thread.join()

    def reset(self, response_body=EMPTY_BODY):
        self.request_target = None
        self.response_body = response_body

    @property
    def base_path(self):
        host, port = self._server.server_address[:2]
        return 'http://%s:%s/base' % (host, port)


class TestPathParams(unittest.TestCase):
    """Test path parameter handling for every operation that takes an ID in the path."""

    @classmethod
    def setUpClass(cls):
        cls.server = StubServer()
        cls.server.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.stop()

    def setUp(self):
        self.server.reset()
        configuration = Configuration(api_key=API_KEY)
        configuration.host = self.server.base_path
        self.api = FingerprintApi(configuration)

    def call(self, operation, value):
        """Run operation with value and return the request target the server received."""
        self.server.reset(operation.response_body)
        operation.call(self.api, value)
        return self.server.request_target

    def test_value_is_encoded_into_a_single_path_segment(self):
        cases = (
            ('path', '../events', '..%2Fevents'),
            ('nested path', '../../base/events', '..%2F..%2Fbase%2Fevents'),
            ('leading slash', '/events/123', '%2Fevents%2F123'),
            ('absolute url', 'https://test.com/events', 'https%3A%2F%2Ftest.com%2Fevents'),
            ('protocol relative url', '//test.com', '%2F%2Ftest.com'),
            ('query injection', '123?limit=1', '123%3Flimit%3D1'),
            ('fragment injection', '123#fragment', '123%23fragment'),
            ('whitespace', 'hello world', 'hello%20world'),
            ('non ascii', u'\xe9', '%C3%A9'),
            ('pre-encoded', '..%2Fevents', '..%252Fevents'),
        )

        for operation in OPERATIONS:
            for name, value, encoded in cases:
                with self.subTest(operation=operation.name, case=name):
                    request_target = self.call(operation, value)

                    self.assertEqual('/base' + operation.prefix + encoded, request_target)

    def test_dot_in_value_is_not_touched(self):
        """Test dots in the value stay literal."""
        cases = (
            ('request id', '1708102555327.NLOjmg'),
            ('three dots', '...'),
            ('leading dot', '.leading'),
            ('trailing dot', 'trailing.'),
        )

        for operation in OPERATIONS:
            for name, value in cases:
                with self.subTest(operation=operation.name, case=name):
                    request_target = self.call(operation, value)

                    self.assertEqual('/base' + operation.prefix + value, request_target)

    def test_dot_segment_is_rejected_without_sending_a_request(self):
        """`.` and `..` are refused"""
        for operation in OPERATIONS:
            for value in ('.', '..'):
                with self.subTest(operation=operation.name, value=value):
                    self.server.reset(operation.response_body)

                    with self.assertRaises(InvalidParameterError) as context:
                        operation.call(self.api, value)

                    self.assertIsNone(self.server.request_target)
                    self.assertEqual(operation.param, context.exception.parameter)
                    self.assertEqual(value, context.exception.value)
                    self.assertIn(operation.param, str(context.exception))

    def test_empty_value_does_not_address_the_collection(self):
        """An empty ID leaves a trailing slash"""
        for operation in OPERATIONS:
            with self.subTest(operation=operation.name):
                request_target = self.call(operation, '')

                self.assertEqual('/base' + operation.prefix, request_target)
                self.assertNotEqual('/base' + operation.prefix.rstrip('/'), request_target)


if __name__ == '__main__':
    unittest.main()
