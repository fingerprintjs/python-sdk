from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit, parse_qsl, urlunsplit, urlencode
from fingerprint_server_sdk import __version__

import urllib3

MOCK_SEARCH_EVENTS_200 = 'events/get_event_200.json'


class MockPoolManager(object):

    def __init__(self, tc, request_headers=None):
        self.request_headers = request_headers
        self._tc = tc
        self._reqs = []
        self.request_headers = request_headers

    def expect_request(self, *args, **kwargs):
        self._reqs.append((args, kwargs))

    @staticmethod
    def get_mock_from_path(path):
        return path.split('/')[-1]

    def request(self, *args, **kwargs):
        self._tc.assertTrue(len(self._reqs) > 0)
        (request_method, request_url), request_config = self._reqs.pop(0)

        response_status_code = request_config.pop('response_status_code', 200)
        response_data_file = request_config.pop('response_data_file', None)
        response_text = request_config.pop('response_text', None)
        response_headers = request_config.pop('response_headers', None)

        self._tc.maxDiff = None
        self._tc.assertEqual(request_method, args[0])

        url, ii_value = self._strip_query_param(args[1], "ii")
        self._tc.assertIsInstance(ii_value, str)
        self._tc.assertEqual(f"fingerprint-server-python-sdk/{__version__}", ii_value)
        self._tc.assertEqual(request_url, url)

        self._tc.assertEqual(set(request_config.keys()), set(kwargs.keys()))

        if 'fields' in kwargs and 'fields' in request_config:
            self._tc.assertEqual(Counter(kwargs['fields']), Counter(request_config['fields']))

        response_body = None
        if response_text is not None:
            response_body = response_text.encode('utf-8')
        elif response_data_file is not None:
            if not isinstance(response_data_file, Path) and not isinstance(response_data_file, str):
                raise TypeError('response_data_file must be str or Path')
            base_dir = Path(__file__).resolve().parent / 'mocks'
            mock_file_path = base_dir / response_data_file
            with mock_file_path.open('r', encoding='utf-8') as mock_file:
                response_body = mock_file.read().encode('utf-8')

        return urllib3.HTTPResponse(status=response_status_code, body=response_body, headers=response_headers)

    @staticmethod
    def _strip_query_param(url: str, name: str):
        s = urlsplit(url)
        pairs = parse_qsl(s.query, keep_blank_values=True)
        values = [v for k, v in pairs if k == name]
        kept = [(k, v) for k, v in pairs if k != name]
        new_query = urlencode(kept, doseq=True)
        new_url = urlunsplit((s.scheme, s.netloc, s.path, new_query, s.fragment))
        return new_url, (values[0] if values else None)