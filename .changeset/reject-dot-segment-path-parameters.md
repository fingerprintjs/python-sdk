---
'@fingerprint/python-sdk': patch
---

Reject `.` and `..` as event and visitor IDs. `get_event`, `update_event`, and `delete_visitor_data` now raise the new `InvalidArgumentError` without sending a request.
