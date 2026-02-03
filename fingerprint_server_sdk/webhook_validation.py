import hmac
import hashlib


class WebhookValidation:
    """Manages work with webhooks."""
    @staticmethod
    def is_valid_hmac_signature(signature: str, data: bytes, secret: str) -> bool:
        """Validates an HMAC signature."""
        hmac_instance = hmac.new(secret.encode('utf-8'), data, hashlib.sha256)
        computed_hash = hmac_instance.hexdigest()
        return signature == computed_hash

    @staticmethod
    def is_valid_webhook_signature(header: str, data: bytes, secret: str) -> bool:
        """Verifies the HMAC signature extracted from the "fpjs-event-signature" header of the incoming request.
        This is a part of the webhook signing process, which is available only for enterprise customers.
        If you wish to enable it, please contact our support: https://fingerprint.com/support"""

        signatures = header.split(',')

        for signature in signatures:
            parts = signature.split('=')
            if len(parts) == 2:
                version, hash_value = parts
                if version == "v1" and WebhookValidation.is_valid_hmac_signature(hash_value, data, secret):
                    return True

        return False

