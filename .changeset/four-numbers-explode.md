---
"fingerprint-pro-server-api-python-sdk": minor
---

### SDK Changes ([8b3971e](https://github.com/fingerprintjs/python-sdk/commit/8b3971eb8a30c2d5bd52f9b188b0c2731a096d43))

- Add `WorkspaceScopedSecretKeyRequired` error code
- Add optional `type` field to `IPInfoASN` (`ip_info_asn`) response model
- Add `integrations` field to the `SDK` model with a list of `Integration` and `IntegrationSubIntegration`.

### Deprecation

:warning: `fingerprint_pro_server_api_sdk` uses Server API v3, which is deprecated. Please migrate to the new [`fingerprint_server_sdk`](https://github.com/fingerprintjs/python-sdk) package which uses Server API v4.
