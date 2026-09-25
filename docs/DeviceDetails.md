# DeviceDetails
Native, SDK-collected mobile device identification signals (manufacturer, model, and OS version). Structurally separate from the top-level `device`, `os`, and `os_version` fields and from `browser_details`, all of which are derived from user-agent parsing rather than native SDK signals.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_manufacturer** | **str** | Raw device manufacturer string as reported by the device OS. Not normalized: casing is vendor-defined (samsung, Xiaomi, OPPO, HUAWEI). Always `Apple` on iOS. | [optional] 
**device_model** | **str** | Raw device model identifier, as reported by the mobile OS. | [optional] 
**os_version** | **str** | Mobile operating system version. Component count is not fixed and must not be assumed by consumers: iOS always reports `major.minor.patch` (e.g. `17.4.1`), while Android's precision varies by OS era and which raw signal resolved it — `major` only (`9`, `13`) since Android 10 dropped point releases, `major.minor` (`16.1`) from Android 16 (API 36+) reintroducing a minor component, or a genuine `major.minor.patch` (`8.1.0`) on pre-Android 10 devices that shipped real point releases. Never a fabricated/zero-padded component. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

