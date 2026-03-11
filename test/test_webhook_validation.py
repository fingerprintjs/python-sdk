import unittest

from fingerprint_server_sdk import WebhookValidation


class TestWebhookValidation(unittest.TestCase):
    valid_header = 'v1=1b2c16b75bd2a870c114153ccda5bcfca63314bc722fa160d690de133ccbb9db'
    valid_header_v2 = 'v2=1b2c16b75bd2a870c114153ccda5bcfca63314bc722fa160d690de133ccbb9db'
    secret = 'secret'
    data = b'data'

    def test_valid_header(self):
        result = WebhookValidation.is_valid_webhook_signature(
            self.valid_header, self.data, self.secret
        )
        self.assertTrue(result)

    def test_invalid_header(self):
        result = WebhookValidation.is_valid_webhook_signature('v2=invalid', self.data, self.secret)
        self.assertFalse(result)

    def test_header_without_version(self):
        result = WebhookValidation.is_valid_webhook_signature('invalid', self.data, self.secret)
        self.assertFalse(result)

    def test_header_with_unsupported_version(self):
        result = WebhookValidation.is_valid_webhook_signature(
            self.valid_header_v2, self.data, self.secret
        )
        self.assertFalse(result)

    def test_empty_header(self):
        result = WebhookValidation.is_valid_webhook_signature('', self.data, self.secret)
        self.assertFalse(result)

    def test_empty_secret(self):
        result = WebhookValidation.is_valid_webhook_signature('invalid', self.data, '')
        self.assertFalse(result)

    def test_empty_data(self):
        result = WebhookValidation.is_valid_webhook_signature(self.valid_header, b'', self.secret)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
