from fingerprint_server_sdk import WebhookValidation

header = "v1=1b2c16b75bd2a870c114153ccda5bcfca63314bc722fa160d690de133ccbb9db"
secret = "secret"
data = b"data"

is_valid = WebhookValidation.is_valid_webhook_signature(header, data, secret)

print("Webhook signature is correct!" if is_valid else "Webhook signature is incorrect!")
