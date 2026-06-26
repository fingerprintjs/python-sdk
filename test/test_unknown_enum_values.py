import json
import unittest
from pathlib import Path
from typing import Any

from fingerprint_server_sdk import Event
from fingerprint_server_sdk.models.bot_info import BotInfo
from fingerprint_server_sdk.models.proxy_details import ProxyDetails
from fingerprint_server_sdk.models.sdk import SDK

MOCK_DIR = Path(__file__).resolve().parent / 'mocks'


class TestUnknownEnumValues(unittest.TestCase):
    """Test that unknown/new enum values are accepted without errors."""

    def _load_event_json(self) -> dict[str, Any]:
        mock_file = MOCK_DIR / 'events' / 'get_event_200.json'
        return json.loads(mock_file.read_text(encoding='utf-8'))

    def test_event_with_unknown_proxy_type(self) -> None:
        """Unknown proxy_type value should be accepted and preserved."""
        data = self._load_event_json()
        data['proxy_details']['proxy_type'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event, Event)
        self.assertEqual(event.proxy_details.proxy_type, 'unknown-value')

    def test_event_with_unknown_sdk_platform(self) -> None:
        """Unknown SDK platform value should be accepted and preserved."""
        data = self._load_event_json()
        data['sdk']['platform'] = 'new-platform'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event, Event)
        self.assertEqual(event.sdk.platform, 'new-platform')

    def test_event_with_unknown_bot_result(self) -> None:
        """Unknown bot result value should be accepted and preserved."""
        data = self._load_event_json()
        data['bot'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event, Event)
        self.assertEqual(event.bot, 'unknown-value')

    def test_event_with_unknown_vpn_confidence(self) -> None:
        """Unknown vpn_confidence value should be accepted and preserved."""
        data = self._load_event_json()
        data['vpn'] = True
        data['vpn_confidence'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event, Event)
        self.assertEqual(event.vpn_confidence, 'unknown-value')

    def test_event_with_unknown_proxy_confidence(self) -> None:
        """Unknown proxy_confidence value should be accepted and preserved."""
        data = self._load_event_json()
        data['proxy_confidence'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event, Event)
        self.assertEqual(event.proxy_confidence, 'unknown-value')

    def test_event_with_unknown_tampering_confidence(self) -> None:
        """Unknown tampering_confidence value should be accepted and preserved."""
        data = self._load_event_json()
        data['tampering_confidence'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event, Event)
        self.assertEqual(event.tampering_confidence, 'unknown-value')

    def test_event_with_unknown_rare_device_percentile_bucket(self) -> None:
        """Unknown rare_device_percentile_bucket value should be accepted and preserved."""
        data = self._load_event_json()
        data['rare_device_percentile_bucket'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event, Event)
        self.assertEqual(event.rare_device_percentile_bucket, 'unknown-value')

    def test_proxy_details_with_unknown_proxy_type(self) -> None:
        """ProxyDetails model should accept unknown proxy_type directly."""
        details = ProxyDetails.from_dict({'proxy_type': 'unknown-value', 'last_seen_at': 123})
        self.assertIsInstance(details, ProxyDetails)
        self.assertEqual(details.proxy_type, 'unknown-value')

    def test_sdk_with_unknown_platform(self) -> None:
        """SDK model should accept unknown platform directly."""
        sdk = SDK.from_dict({'platform': 'unknown-value', 'version': '1.0.0'})
        self.assertIsInstance(sdk, SDK)
        self.assertEqual(sdk.platform, 'unknown-value')

    def test_bot_info_with_unknown_identity_and_confidence(self) -> None:
        """BotInfo model should accept unknown identity and confidence values."""
        info = BotInfo.from_dict(
            {
                'category': 'crawler',
                'provider': 'TestBot',
                'name': 'test',
                'identity': 'unknown-value',
                'confidence': 'unknown-value',
            }
        )
        self.assertIsInstance(info, BotInfo)
        self.assertEqual(info.identity, 'unknown-value')
        self.assertEqual(info.confidence, 'unknown-value')

    def test_event_with_multiple_unknown_enum_values(self) -> None:
        """Event should deserialize when multiple enum fields have unknown values."""
        data = self._load_event_json()
        data['proxy_details']['proxy_type'] = 'unknown-value'
        data['sdk']['platform'] = 'unknown-value'
        data['bot'] = 'unknown-value'
        data['vpn'] = True
        data['vpn_confidence'] = 'unknown-value'
        data['proxy_confidence'] = 'unknown-value'
        data['tampering_confidence'] = 'unknown-value'
        data['rare_device_percentile_bucket'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event, Event)
        self.assertEqual(event.proxy_details.proxy_type, 'unknown-value')
        self.assertEqual(event.sdk.platform, 'unknown-value')
        self.assertEqual(event.bot, 'unknown-value')
        self.assertEqual(event.vpn_confidence, 'unknown-value')
        self.assertEqual(event.proxy_confidence, 'unknown-value')
        self.assertEqual(event.tampering_confidence, 'unknown-value')
        self.assertEqual(event.rare_device_percentile_bucket, 'unknown-value')

    def test_known_enum_values_still_work(self) -> None:
        """Known enum values should continue to work as before."""
        data = self._load_event_json()

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event, Event)
        self.assertEqual(event.proxy_details.proxy_type, 'residential')
        self.assertEqual(event.sdk.platform, 'js')


if __name__ == '__main__':
    unittest.main()
