---
'fingerprint-pro-server-api-python-sdk': patch
---

Reject `.` and `..` as path parameter values. `get_event`, `update_event`, `get_visits`, and `delete_visitor_data` now raise the new `InvalidPathParameterError` without sending a request.
