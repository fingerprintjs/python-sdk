---
"@fingerprint/python-sdk": major
---

Changed library name to `fingerprint_server_sdk`

**BREAKING CHANGE**:
- You need to change package name to `fingerprint_server_sdk`.

**MIGRATION_GUIDE**:
- Replace imports to new name:
```diff
- import fingerprint_pro_server_api_sdk
+ import fingerprint_server_sdk
 ```