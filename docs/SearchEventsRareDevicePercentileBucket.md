# SearchEventsRareDevicePercentileBucket
Filter events by Device Rarity percentile bucket.
`<p95` - device configuration is in the bottom 95% (most common).
`p95-p99` - device is in the 95th to 99th percentile.
`p99-p99.5` - device is in the 99th to 99.5th percentile.
`p99.5-p99.9` - device is in the 99.5th to 99.9th percentile.
`p99.9+` - device is in the top 0.1% (rarest).
`not_seen` - device configuration has never been observed before.

> This Smart Signal is currently in beta and only available to select customers. If you are interested, please [contact our support team](https://fingerprint.com/support/).


## Enum

* `LESS_THAN_P95` (value: `'<p95'`)
* `P95_MINUS_P99` (value: `'p95-p99'`)
* `P99_MINUS_P99_DOT_5` (value: `'p99-p99.5'`)
* `P99_DOT_5_MINUS_P99_DOT_9` (value: `'p99.5-p99.9'`)
* `P99_DOT_9_PLUS` (value: `'p99.9+'`)
* `NOT_SEEN` (value: `'not_seen'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

