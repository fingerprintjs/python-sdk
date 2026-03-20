import unittest
from urllib.parse import urlencode

from fingerprint_server_sdk import (
    BadRequestException,
    Configuration,
    ConflictException,
    ErrorCode,
    ErrorResponse,
    Event,
    EventSearch,
    EventUpdate,
    ForbiddenException,
    NotFoundException,
    TooManyRequestsException,
    __version__,
)
from fingerprint_server_sdk.api.fingerprint_api import FingerprintApi
from fingerprint_server_sdk.configuration import Region
from test.mock_pool_manager import MockPoolManager

API_KEY = '<secret-api-key>'
REGION = Region.US


class TestFingerprintApi(unittest.TestCase):
    """FingerprintApi unit test stubs"""

    def setUp(self) -> None:
        configuration = Configuration(api_key=API_KEY, region=REGION)
        self.integration_info = ('ii', f'fingerprint-pro-server-python-sdk/{__version__}')
        self.request_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}',
            'Accept': 'application/json',
            'User-Agent': f'fingerprint-pro-server-python-sdk/{__version__}',
        }
        self.api = FingerprintApi(configuration)

    def tearDown(self) -> None:
        del self.api

    @staticmethod
    def get_event_path(event_id, region: Region = Region.US):
        base = Configuration.get_host(region)
        return f'{base}/events/{event_id}'

    @staticmethod
    def get_search_events_path(params: dict, region: Region = Region.US):
        base = Configuration.get_host(region)
        url = f'{base}/events'
        if not params:
            return url

        query_param_pairs: list[tuple[str, str]] = []
        for k, v in params.items():
            if v is None:
                continue
            if isinstance(v, (list, tuple)):
                for item in v:
                    if item is None:
                        continue
                    query_param_pairs.append((k, str(item)))
            else:
                query_param_pairs.append((k, str(v)))

        return f'{url}?{urlencode(query_param_pairs, doseq=True)}' if query_param_pairs else url

    @staticmethod
    def delete_visitor_path(visitor_id, region: Region = Region.US):
        base = Configuration.get_host(region)
        return f'{base}/visitors/{visitor_id}'

    def test_delete_visitor_data(self) -> None:
        """Test case for delete_visitor_data

        Delete data by visitor ID
        """
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        visitor_id = 'XXXXXXXXXXXXXXXXXXXX'
        mock_pool.expect_request(
            'DELETE',
            TestFingerprintApi.delete_visitor_path(visitor_id),
            body=None,
            response_text='{}',
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
        )

        self.api.delete_visitor_data(visitor_id)

    def test_delete_visitor_data_bad_request(self) -> None:
        """Test case for delete_visitor_data with 400 Bad Request response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        visitor_id = 'invalid_visitor_id'
        mock_pool.expect_request(
            'DELETE',
            TestFingerprintApi.delete_visitor_path(visitor_id),
            body=None,
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_status_code=400,
            response_data_file='errors/400_visitor_id_invalid.json',
        )

        with self.assertRaises(BadRequestException) as context:
            self.api.delete_visitor_data(visitor_id)

        self.assertEqual(context.exception.status, 400)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.REQUEST_CANNOT_BE_PARSED)

    def test_delete_visitor_data_forbidden(self) -> None:
        """Test case for delete_visitor_data with 403 Forbidden response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        visitor_id = 'XXXXXXXXXXXXXXXXXXXX'
        mock_pool.expect_request(
            'DELETE',
            TestFingerprintApi.delete_visitor_path(visitor_id),
            body=None,
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_status_code=403,
            response_data_file='errors/403_feature_not_enabled.json',
        )

        with self.assertRaises(ForbiddenException) as context:
            self.api.delete_visitor_data(visitor_id)

        self.assertEqual(context.exception.status, 403)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.FEATURE_NOT_ENABLED)

    def test_delete_visitor_data_not_found(self) -> None:
        """Test case for delete_visitor_data with 404 Not Found response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        visitor_id = 'nonexistent_visitor_id'
        mock_pool.expect_request(
            'DELETE',
            TestFingerprintApi.delete_visitor_path(visitor_id),
            body=None,
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_status_code=404,
            response_data_file='errors/404_visitor_not_found.json',
        )

        with self.assertRaises(NotFoundException) as context:
            self.api.delete_visitor_data(visitor_id)

        self.assertEqual(context.exception.status, 404)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.VISITOR_NOT_FOUND)

    def test_delete_visitor_data_too_many_requests(self) -> None:
        """Test case for delete_visitor_data with 429 Too Many Requests response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        visitor_id = 'XXXXXXXXXXXXXXXXXXXX'
        mock_pool.expect_request(
            'DELETE',
            TestFingerprintApi.delete_visitor_path(visitor_id),
            body=None,
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_status_code=429,
            response_data_file='errors/429_too_many_requests.json',
            response_headers={'Retry-After': '5'},
        )

        with self.assertRaises(TooManyRequestsException) as context:
            self.api.delete_visitor_data(visitor_id)

        self.assertEqual(context.exception.status, 429)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.TOO_MANY_REQUESTS)

    def test_get_event(self) -> None:
        """Test case for get_event

        Get an event by event ID
        """
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        event_id = '0000000000000.XXXXX'
        mock_pool.expect_request(
            'GET',
            TestFingerprintApi.get_event_path(event_id),
            fields=[],
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_data_file='events/get_event_200.json',
        )

        event_response = self.api.get_event(event_id)
        self.assertIsInstance(event_response, Event)

    def test_get_event_bad_request(self) -> None:
        """Test case for get_event with 400 Bad Request response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        event_id = 'invalid'
        mock_pool.expect_request(
            'GET',
            TestFingerprintApi.get_event_path(event_id),
            fields=[],
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_status_code=400,
            response_data_file='errors/400_event_id_invalid.json',
        )

        with self.assertRaises(BadRequestException) as context:
            self.api.get_event(event_id)

        self.assertEqual(context.exception.status, 400)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.REQUEST_CANNOT_BE_PARSED)

    def test_get_event_forbidden(self) -> None:
        """Test case for get_event with 403 Forbidden response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        event_id = '0000000000000.XXXXX'
        mock_pool.expect_request(
            'GET',
            TestFingerprintApi.get_event_path(event_id),
            fields=[],
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_status_code=403,
            response_data_file='errors/403_secret_api_key_required.json',
        )

        with self.assertRaises(ForbiddenException) as context:
            self.api.get_event(event_id)

        self.assertEqual(context.exception.status, 403)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.SECRET_API_KEY_REQUIRED)

    def test_get_event_not_found(self) -> None:
        """Test case for get_event with 404 Not Found response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        event_id = 'nonexistent_event_id'
        mock_pool.expect_request(
            'GET',
            TestFingerprintApi.get_event_path(event_id),
            fields=[],
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_status_code=404,
            response_data_file='errors/404_event_not_found.json',
        )

        with self.assertRaises(NotFoundException) as context:
            self.api.get_event(event_id)

        self.assertEqual(context.exception.status, 404)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.EVENT_NOT_FOUND)

    def test_get_event_too_many_requests(self) -> None:
        """Test case for get_event with 429 Too Many Requests response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        event_id = '0000000000000.XXXXX'
        mock_pool.expect_request(
            'GET',
            TestFingerprintApi.get_event_path(event_id),
            fields=[],
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_status_code=429,
            response_data_file='errors/429_too_many_requests.json',
        )

        with self.assertRaises(TooManyRequestsException) as context:
            self.api.get_event(event_id)

        self.assertEqual(context.exception.status, 429)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.TOO_MANY_REQUESTS)

    def test_search_events(self) -> None:
        """Test case for search_events

        Search events
        """
        params = {'limit': 2}

        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_pool.expect_request(
            'GET',
            TestFingerprintApi.get_search_events_path(params),
            fields=[],
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_data_file='events/search/get_event_search_200.json',
        )
        event_response = self.api.search_events(**params)
        self.assertIsInstance(event_response, EventSearch)
        self.assertEqual(len(event_response.events), 1)
        first_event = event_response.events[0]
        self.assertIsInstance(first_event, Event)
        self.assertEqual(first_event.event_id, '1708102555327.NLOjmg')

    def test_search_events_bad_request(self) -> None:
        """Test case for search_events with 400 Bad Request response"""
        params = {'limit': 99}

        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_pool.expect_request(
            'GET',
            TestFingerprintApi.get_search_events_path(params),
            fields=[],
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_status_code=400,
            response_data_file='errors/400_request_body_invalid.json',
        )

        with self.assertRaises(BadRequestException) as context:
            self.api.search_events(**params)

        self.assertEqual(context.exception.status, 400)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.REQUEST_CANNOT_BE_PARSED)

    def test_search_events_forbidden(self) -> None:
        """Test case for search_events with 403 Forbidden response"""
        params = {'limit': 2}

        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_pool.expect_request(
            'GET',
            TestFingerprintApi.get_search_events_path(params),
            fields=[],
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            response_status_code=403,
            response_data_file='errors/403_secret_api_key_required.json',
        )

        with self.assertRaises(ForbiddenException) as context:
            self.api.search_events(**params)

        self.assertEqual(context.exception.status, 403)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.SECRET_API_KEY_REQUIRED)

    def test_update_event(self) -> None:
        """Test case for update_event

        Update an event
        """
        test_cases = [
            (EventUpdate(linked_id='qwe'), '{"linkedId": "qwe"}'),
            (EventUpdate(tags={'qwe': 123}), '{"tags": {"qwe": 123}}'),
            (EventUpdate(suspect=False), '{"suspect": false}'),
            (EventUpdate(suspect=True), '{"suspect": true}'),
            (
                EventUpdate(linked_id='qwe', tags={'qwe': 123}, suspect=False),
                '{"linkedId": "qwe", "tags": {"qwe": 123}, "suspect": false}',
            ),
        ]

        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool

        event_id = '0000000000000.XXXXX'

        for update_body, serialized_body in test_cases:
            mock_pool.expect_request(
                'PATCH',
                TestFingerprintApi.get_event_path(event_id),
                headers=self.request_headers,
                preload_content=True,
                timeout=None,
                body=serialized_body,
                response_text='OK',
            )

            self.api.update_event(event_id, update_body)

    def test_update_event_bad_request(self) -> None:
        """Test case for update_event with 400 Bad Request response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        event_id = '0000000000000.XXXXX'
        update_body = EventUpdate(linked_id='test')
        mock_pool.expect_request(
            'PATCH',
            TestFingerprintApi.get_event_path(event_id),
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            body='{"linkedId": "test"}',
            response_status_code=400,
            response_data_file='errors/400_request_body_invalid.json',
        )

        with self.assertRaises(BadRequestException) as context:
            self.api.update_event(event_id, update_body)

        self.assertEqual(context.exception.status, 400)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.REQUEST_CANNOT_BE_PARSED)

    def test_update_event_forbidden(self) -> None:
        """Test case for update_event with 403 Forbidden response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        event_id = '0000000000000.XXXXX'
        update_body = EventUpdate(suspect=True)
        mock_pool.expect_request(
            'PATCH',
            TestFingerprintApi.get_event_path(event_id),
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            body='{"suspect": true}',
            response_status_code=403,
            response_data_file='errors/403_secret_api_key_required.json',
        )

        with self.assertRaises(ForbiddenException) as context:
            self.api.update_event(event_id, update_body)

        self.assertEqual(context.exception.status, 403)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.SECRET_API_KEY_REQUIRED)

    def test_update_event_not_found(self) -> None:
        """Test case for update_event with 404 Not Found response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        event_id = 'nonexistent_event_id'
        update_body = EventUpdate(suspect=True)
        mock_pool.expect_request(
            'PATCH',
            TestFingerprintApi.get_event_path(event_id),
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            body='{"suspect": true}',
            response_status_code=404,
            response_data_file='errors/404_event_not_found.json',
        )

        with self.assertRaises(NotFoundException) as context:
            self.api.update_event(event_id, update_body)

        self.assertEqual(context.exception.status, 404)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.EVENT_NOT_FOUND)

    def test_update_event_conflict(self) -> None:
        """Test case for update_event with 409 Conflict response"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        event_id = '0000000000000.XXXXX'
        update_body = EventUpdate(suspect=True)
        mock_pool.expect_request(
            'PATCH',
            TestFingerprintApi.get_event_path(event_id),
            headers=self.request_headers,
            preload_content=True,
            timeout=None,
            body='{"suspect": true}',
            response_status_code=409,
            response_data_file='errors/409_state_not_ready.json',
        )

        with self.assertRaises(ConflictException) as context:
            self.api.update_event(event_id, update_body)

        self.assertEqual(context.exception.status, 409)
        self.assertIsInstance(context.exception.data, ErrorResponse)
        self.assertEqual(context.exception.data.error.code, ErrorCode.STATE_NOT_READY)


if __name__ == '__main__':
    unittest.main()
