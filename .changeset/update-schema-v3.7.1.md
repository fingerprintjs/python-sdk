---
"fingerprint-pro-server-api-python-sdk": minor
---

Update Server API schema to `v3.7.1`:

- **errors**: Add `RequestReadTimeout` `ErrorCode` value and document `429`/`504` responses on affected endpoints.
- **events**: Require `label` on `LabelsInner` entries.
- **events-search**: Clarify that `reverse` defaults to `false` (sorted newest first) when omitted.
- **visitors**: Document that `GET /visitors/{visitor_id}` now returns at most one item in `visits`; use `GET /events/search` for multi-event history and pagination.
- Clarify `ProxyDetails.proxy_type` and other signal descriptions to match the updated API v3 documentation.
