---
"@fingerprint/python-sdk": major
---

Migrate to Server API v4.

### Breaking Changes

- Flatten event structure. Access fields directly intead of through `products` wrapper.
- Remove `get_visitors` and `get_releated_visitors` endpoints (use `search_events` instead).
- Remove deprecated v3 models (webhook models, product wrapper models, etc.)

### Migration Guide

**Event structure:**
```diff
- event.products.identification.data.visitor_id
+ event.identification.visitor_id
```

**Region parameter:**
```diff
- Configuration(api_key="key", region="us")
+ from fingerprint_server_sdk.configuration import Region
+ Configuration(api_key="key", region=Region.US)
```

**New Features:**

- New exception classes: `TooManyRequestsException`, `ConflictException`, `UnprocessableEntityException`, ...
- New v4 models: `BotInfo`, `Canvas`, `Emoji`, `EventRuleAction`, `FontPreferences`, ...
