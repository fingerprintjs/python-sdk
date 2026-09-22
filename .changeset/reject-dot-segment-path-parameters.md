---
'fingerprint-pro-server-api-python-sdk': patch
---

Reject `.` and `..` as request and visitor IDs. `get_event`, `update_event`, `get_visits`, and `delete_visitor_data` now raise the new `InvalidArgumentError` without sending a request.
