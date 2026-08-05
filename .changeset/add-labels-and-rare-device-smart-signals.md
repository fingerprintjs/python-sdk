---
"fingerprint-pro-server-api-python-sdk": minor
---

Update Server API schema to `v3.5.2`:

- **events**: Add `labels` field with machine learning based predictions for specific use cases (beta).
- **events**: Add `rareDevice` Smart Signal with `result` and `percentileBucket`.
- **events-search**: Add `rare_device` and `rare_device_percentile_bucket` filters.
- **events**: Add `mlScore` fields to the `VPN` and `Proxy` signals, and `mlPrediction` to `VPNMethods` (beta).
- **events**: Add the `unknown` value to the `ProxyDetails` `proxyType` field for proxies detected solely by the ML model.
- Clarify the `DeveloperTools` signal description to note it also covers Android/iOS devices.
