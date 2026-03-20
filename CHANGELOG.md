# Fingerprint Pro Server Python SDK

## 9.0.1

### Patch Changes

- Fix incorrect SDK name in the integration info parameter ([43e083e](https://github.com/fingerprintjs/python-sdk/commit/43e083ee74b4533cadfed206502a490df82c2803))
- Bump minimum required `cryptography` version from `41.0.0` to `46.0.5`. ([91288d5](https://github.com/fingerprintjs/python-sdk/commit/91288d573e31aa54e51ae83ba25e5dc6e8cf22a7))

## 9.0.0

### Major Changes

- Changed library name to `fingerprint_server_sdk`

  **BREAKING CHANGE**:

  - You need to change package name to `fingerprint_server_sdk`.

  **MIGRATION_GUIDE**:

  Replace imports to new name:

  ```diff
  - import fingerprint_pro_server_api_sdk
  + import fingerprint_server_sdk
  ```

  If you are using docker compose file, please re-build the SDK. ([1f8ea14](https://github.com/fingerprintjs/python-sdk/commit/1f8ea14bbd77d439c53bc30bcd7f0e64c66c7d3e))

- Migrate to Server API v4.

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
  - New v4 models: `BotInfo`, `Canvas`, `Emoji`, `EventRuleAction`, `FontPreferences`, ... ([f61ab2c](https://github.com/fingerprintjs/python-sdk/commit/f61ab2c876f538de8bca02f60cbab14ceae91801))

## 9.0.0-rc.1

### Patch Changes

- fix build system ([fa1da3b](https://github.com/fingerprintjs/python-sdk/commit/fa1da3b9fc8201d20964dce6f347cae5e01eb5e1))

## 9.0.0-rc.0

### Major Changes

- Changed library name to `fingerprint_server_sdk`

  **BREAKING CHANGE**:

  - You need to change package name to `fingerprint_server_sdk`.

  **MIGRATION_GUIDE**:

  Replace imports to new name:

  ```diff
  - import fingerprint_pro_server_api_sdk
  + import fingerprint_server_sdk
  ```

  If you are using docker compose file, please re-build the SDK. ([1f8ea14](https://github.com/fingerprintjs/python-sdk/commit/1f8ea14bbd77d439c53bc30bcd7f0e64c66c7d3e))

- Migrate to Server API v4.

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
  - New v4 models: `BotInfo`, `Canvas`, `Emoji`, `EventRuleAction`, `FontPreferences`, ... ([f61ab2c](https://github.com/fingerprintjs/python-sdk/commit/f61ab2c876f538de8bca02f60cbab14ceae91801))

## 8.11.0

### Minor Changes

- **events-search**: Event search now supports a new set of filter parameters: `developer_tools`, `location_spoofing`, `mitm_attack`, `proxy`, `sdk_version`, `sdk_platform`, `environment` ([4e2baaf](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4e2baafe8cbaad13bb72d46ab9f227053eba28ed))
- **webhook**: Add `supplementaryIds` property to the Webhooks schema. ([4e2baaf](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4e2baafe8cbaad13bb72d46ab9f227053eba28ed))
- Add `proximity` signal that represents a fixed geographical zone in a discrete global grid within which the device is observed. ([8b24e3b](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8b24e3b39b28d4c774e50f42e1648f5bfd804f11))
- Add `environmentId` property to `identification` ([4e2baaf](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4e2baafe8cbaad13bb72d46ab9f227053eba28ed))

## 8.11.0-rc.0

### Minor Changes

- **events-search**: Event search now supports a new set of filter parameters: `developer_tools`, `location_spoofing`, `mitm_attack`, `proxy`, `sdk_version`, `sdk_platform`, `environment` ([4e2baaf](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4e2baafe8cbaad13bb72d46ab9f227053eba28ed))
- **webhook**: Add `supplementaryIds` property to the Webhooks schema. ([4e2baaf](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4e2baafe8cbaad13bb72d46ab9f227053eba28ed))
- Add `proximity` signal that represents a fixed geographical zone in a discrete global grid within which the device is observed. ([8b24e3b](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8b24e3b39b28d4c774e50f42e1648f5bfd804f11))
- Add `environmentId` property to `identification` ([4e2baaf](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4e2baafe8cbaad13bb72d46ab9f227053eba28ed))

## 8.10.0

### Minor Changes

- Add `details` object to the `proxy` signal. This field includes the `type` of the detected proxy (`residential` or `data_center`) and the `lastSeenAt` timestamp of when an IP was last observed to show proxy-like behavior. ([32ae9b2](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/32ae9b2fe9ec37519876e21555fb3c508605f03d))

## 8.9.0

### Minor Changes

- Mark `replayed` field required in the `identification` product schema. This field will always be present. ([05e1540](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/05e154067f2508294bde4cf4614ea72d0266aa1f))
- Add `sdk` field with platform metadata to `identification` ([05e1540](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/05e154067f2508294bde4cf4614ea72d0266aa1f))

### Patch Changes

- Deprecate the Remote Control Detection Smart Signal. This signal is no longer available. ([05e1540](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/05e154067f2508294bde4cf4614ea72d0266aa1f))

## 8.9.0-rc.0

### Minor Changes

- Mark `replayed` field required in the `identification` product schema. This field will always be present. ([05e1540](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/05e154067f2508294bde4cf4614ea72d0266aa1f))
- Add `sdk` field with platform metadata to `identification` ([05e1540](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/05e154067f2508294bde4cf4614ea72d0266aa1f))

### Patch Changes

- Deprecate the Remote Control Detection Smart Signal. This signal is no longer available. ([05e1540](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/05e154067f2508294bde4cf4614ea72d0266aa1f))

## 8.8.0

### Minor Changes

- add `replayed` field to `identification` in Events and Webhooks ([c25383b](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/c25383b7a7621c2b4d49c2072e24cbdccd43eca7))

## 8.7.0

### Minor Changes

- Add `confidence` property to the Proxy detection Smart Signal, which now supports both residential and public web proxies. ([b7d40f1](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/b7d40f12269ad9435246bb07aaff559034c34838))

## 8.7.0-rc.1

### Minor Changes

- Add `confidence` property to the Proxy detection Smart Signal, which now supports both residential and public web proxies. ([b7d40f1](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/b7d40f12269ad9435246bb07aaff559034c34838))

## 8.6.1-rc.0

### Patch Changes

- Testing updated workflow ([1a67d34](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/1a67d34d606fa998db0a31a02d29d232511bdb24))

## 8.6.0

### Minor Changes

- **events-search**: Event search now supports a new set of filter parameters: `vpn`, `virtual_machine`, `tampering`, `anti_detect_browser`, `incognito`, `privacy_settings`, `jailbroken`, `frida`, `factory_reset`, `cloned_app`, `emulator`, `root_apps`, `vpn_confidence`, `min_suspect_score`. ([9354da9](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9354da95724f407566a5190d1a24f571c3ca4f3f))
- **events-search**: Event search now supports two new filter parameters: `ip_blocklist`, `datacenter` ([826cb8e](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/826cb8e1a939994240a2cb5e048451f4aaf02cde))

### Patch Changes

- **webhook**: Add `environmentId` property ([9354da9](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9354da95724f407566a5190d1a24f571c3ca4f3f))

## 8.6.0-rc.0

### Minor Changes

- **events-search**: Event search now supports a new set of filter parameters: `vpn`, `virtual_machine`, `tampering`, `anti_detect_browser`, `incognito`, `privacy_settings`, `jailbroken`, `frida`, `factory_reset`, `cloned_app`, `emulator`, `root_apps`, `vpn_confidence`, `min_suspect_score`. ([9354da9](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9354da95724f407566a5190d1a24f571c3ca4f3f))
- **events-search**: Event search now supports two new filter parameters: `ip_blocklist`, `datacenter` ([826cb8e](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/826cb8e1a939994240a2cb5e048451f4aaf02cde))

### Patch Changes

- **webhook**: Add `environmentId` property ([9354da9](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9354da95724f407566a5190d1a24f571c3ca4f3f))

## 8.5.0

### Minor Changes

- Add `mitmAttack` (man-in-the-middle attack) Smart Signal. ([7a25214](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/7a252141e24af42aed0a99051dc0bcfd83ce0ef8))

## 8.4.0

### Minor Changes

- **events-search**: Add `pagination_key` parameter ([0410a74](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/0410a746d8246bfdad7b754ae4edebfe3ceb7295))

## 8.4.0-rc.0

### Minor Changes

- **events-search**: Add `pagination_key` parameter ([0410a74](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/0410a746d8246bfdad7b754ae4edebfe3ceb7295))

## 8.3.0

### Minor Changes

- **events-search**: Add a new `events/search` API endpoint. Allow users to search for identification events matching one or more search criteria, for example, visitor ID, IP address, bot detection result, etc. ([2ce9734](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/2ce97343ee676a163b383b8040737ac481dfbb03))

### Patch Changes

- **events-search**: Improve parameter descriptions for `bot`, `suspect` ([8a336e3](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8a336e3ce379e1a82aa8789adc0529c1e3ebe204))

## 8.3.0-rc.0

### Minor Changes

- **events-search**: Add a new `events/search` API endpoint. Allow users to search for identification events matching one or more search criteria, for example, visitor ID, IP address, bot detection result, etc. ([2ce9734](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/2ce97343ee676a163b383b8040737ac481dfbb03))

## 8.2.1

### Patch Changes

- Correctly serialize nullable fields to `null` ([5c21ca0](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5c21ca0acaec7d48c2db1292c126bef2fbbbca0e))

## 8.2.1-dev.0

### Patch Changes

- Correctly serialize nullable fields to `null` ([5c21ca0](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5c21ca0acaec7d48c2db1292c126bef2fbbbca0e))

## 8.2.0

### Minor Changes

- Add Related Visitors API ([691d02a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/691d02a0868aa4c4a17df7e6485c5bde749ea9f5))

## 8.1.0

### Minor Changes

- Add `relay` detection method to the VPN Detection Smart Signal ([cff0ef7](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/cff0ef77d21758844f7b9ff466df78aa7ecba51e))
- **events**: Add a `suspect` field to the `identification` product schema ([cff0ef7](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/cff0ef77d21758844f7b9ff466df78aa7ecba51e))

## 8.0.0

### Major Changes

The underlying Server API hasn’t changed, but we made SDK type and class generation more precise, resulting in small breaking changes for the SDK itself. This change should make the SDK API a lot more stable going forward

- - Remove the `BrowserDetails` field `botProbability`.
  - Update the `IdentificationConfidence` field `score` type format: `float` -> `double`.
  - Make the `RawDeviceAttributeError` field `name` **optional** .
  - Make the `RawDeviceAttributeError` field `message` **optional** .
  - **events**: Remove the `EventsResponse` field `error`.
    - [note]: The errors are represented by `ErrorResponse` model.
  - **events**: Update the `HighActivity` field `dailyRequests` type format: `number` -> `int64`.
  - **events**: Specify the `Tampering` field `anomalyScore` type format: `double`.
  - **webhook**: Make the `Webhook` fields **optional**: `visitorId`, `visitorFound`, `firstSeenAt`, `lastSeenAt`, `browserDetails`, `incognito`.
  - **webhook**: Make the `WebhookClonedApp` field `result` **optional**.
  - **webhook**: Make the `WebhookDeveloperTools` field `result` **optional**.
  - **webhook**: Make the `WebhookEmulator` field `result` **optional**.
  - **webhook**: Make the `WebhookFactoryReset` fields `time` and `timestamp` **optional**.
  - **webhook**: Make the `WebhookFrida` field `result` **optional**.
  - **webhook**: Update the `WebhookHighActivity` field `dailyRequests` type format: `number` -> `int64`.
  - **webhook**: Make the `WebhookIPBlocklist` fields `result` and `details` **optional**.
  - **webhook**: Make the `WebhookJailbroken` field `result` **optional**.
  - **webhook**: Make the `WebhookLocationSpoofing` field `result` **optional**.
  - **webhook**: Make the `WebhookPrivacySettings` field `result` **optional**.
  - **webhook**: Make the `WebhookProxy` field `result` **optional**.
  - **webhook**: Make the `WebhookRemoteControl` field `result` **optional**.
  - **webhook**: Make the `WebhookRootApps` field `result` **optional**.
  - **webhook**: Make the `WebhookSuspectScore` field `result` **optional**.
  - **webhook**: Make the `WebhookTampering` fields `result`, `anomalyScore` and `antiDetectBrowser` **optional**.
  - **webhook**: Specify the `WebhookTampering` field `anomalyScore` type format: `double`.
  - **webhook**: Make the `WebhookTor` field `result` **optional**.
  - **webhook**: Make the `WebhookVelocity` fields **optional**: `distinctIp`, `distinctLinkedId`, `distinctCountry`, `events`, `ipEvents`, `distinctIpByLinkedId`, `distinctVisitorIdByLinkedId`.
  - **webhook**: Make the `WebhookVirtualMachine` field `result` **optional**.
  - **webhook**: Make the `WebhookVPN` fields **optional**: `result`, `confidence`, `originTimezone`, `methods`. ([8df1d4a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8df1d4acf7c26bd72bce13c04d9ea1a85f2b0155))
- - Rename `BotdResult` -> `Botd`.
  - Rename `BotdDetectionResult` -> `BotdBot`:
    - Extract `result` type as `BotdBotResult`.
  - Rename `ClonedAppResult` -> `ClonedApp`.
  - Rename `DeveloperToolsResult` -> `DeveloperTools`.
  - Rename `EmulatorResult` -> `Emulator`.
  - Refactor error models:
    - Remove `ErrorCommon403Response`, `ErrorCommon429Response`, `ErrorEvent404Response`, `TooManyRequestsResponse`, `ErrorVisits403`, `ErrorUpdateEvent400Response`, `ErrorUpdateEvent409Response`, `ErrorVisitor400Response`, `ErrorVisitor404Response`, `IdentificationError`, `ProductError`.
    - Introduce `ErrorResponse` and `ErrorPlainResponse`.
      - [note]: `ErrorPlainResponse` has a different format `{ "error": string }` and it is used only in `GET /visitors`.
    - Extract `error` type as `Error`.
    - Extract `error.code` type as `ErrorCode`.
  - Rename `EventResponse` -> `EventsGetResponse`.
  - Rename `EventUpdateRequest` -> `EventsUpdateRequest`.
  - Rename `FactoryResetResult` -> `FactoryReset`.
  - Rename `FridaResult` -> `Frida`.
  - Rename `IPLocation` -> `Geolocation`:
    - Rename `IPLocationCity` -> `GeolocationCity`.
    - Extract `subdivisions` type as `GeolocationSubdivisions`.
    - Rename `Location` -> `GeolocationContinent`:
    - Introduce a dedicated type `GeolocationCountry`.
    - Rename `Subdivision` -> `GeolocationSubdivision`.
  - Rename `HighActivityResult` -> `HighActivity`.
  - Rename `Confidence` -> `IdentificationConfidence`.
  - Rename `SeenAt` -> `IdentificationSeenAt`.
  - Rename `IncognitoResult` -> `Incognito`.
  - Rename `IpBlockListResult` -> `IPBlocklist`:
    - Extract `details` type as `IPBlocklistDetails`.
  - Rename `IpInfoResult` -> `IPInfo`:
    - Rename `IpInfoResultV4` -> `IPInfoV4`.
    - Rename `IpInfoResultV6` -> `IPInfoV6`.
    - Rename `ASN` -> `IPInfoASN`.
    - Rename `DataCenter` -> `IPInfoDataCenter`.
  - Rename `JailbrokenResult` -> `Jailbroken`.
  - Rename `LocationSpoofingResult` -> `LocationSpoofing`.
  - Rename `PrivacySettingsResult` -> `PrivacySettings`.
  - Rename `ProductsResponse` -> `Products`:
    - Rename inner types: `ProductsResponseIdentification` -> `ProductIdentification`, `ProductsResponseIdentificationData` -> `Identification`, `ProductsResponseBotd` -> `ProductBotd`, `SignalResponseRootApps` -> `ProductRootApps`, `SignalResponseEmulator` -> `ProductEmulator`, `SignalResponseIpInfo` -> `ProductIPInfo`, `SignalResponseIpBlocklist` -> `ProductIPBlocklist`, `SignalResponseTor` -> `ProductTor`, `SignalResponseVpn` -> `ProductVPN`, `SignalResponseProxy` -> `ProductProxy`, `ProxyResult` -> `Proxy`, `SignalResponseIncognito` -> `ProductIncognito`, `SignalResponseTampering` -> `ProductTampering`, `SignalResponseClonedApp` -> `ProductClonedApp`, `SignalResponseFactoryReset` -> `ProductFactoryReset`, `SignalResponseJailbroken` -> `ProductJailbroken`, `SignalResponseFrida` -> `ProductFrida`, `SignalResponsePrivacySettings` -> `ProductPrivacySettings`, `SignalResponseVirtualMachine` -> `ProductVirtualMachine`, `SignalResponseRawDeviceAttributes` -> `ProductRawDeviceAttributes`, `RawDeviceAttributesResultValue` -> `RawDeviceAttributes`, `SignalResponseHighActivity` -> `ProductHighActivity`, `SignalResponseLocationSpoofing` -> `ProductLocationSpoofing`, `SignalResponseSuspectScore` -> `ProductSuspectScore`, `SignalResponseRemoteControl` -> `ProductRemoteControl`, `SignalResponseVelocity` -> `ProductVelocity`, `SignalResponseDeveloperTools` -> `ProductDeveloperTools`.
    - Extract `identification.data` type as `Identification`.
  - Rename `RawDeviceAttributesResult` -> `RawDeviceAttributes`:
    - Extract item type as `RawDeviceAttribute`.
    - Extract `error` type as `RawDeviceAttributeError`.
  - Rename `RemoteControlResult` -> `RemoteControl`.
  - Rename `RootAppsResult` -> `RootApps`.
  - Rename `SuspectScoreResult` -> `SuspectScore`.
  - Extract new model `Tag`.
  - Rename `TamperingResult` -> `Tampering`.
  - Rename `TorResult` -> `Tor`.
  - Rename `VelocityResult` -> `Velocity`:
    - Rename `VelocityIntervals` -> `VelocityData`.
    - Rename `VelocityIntervalResult` -> `VelocityIntervals`.
  - Rename `VirtualMachineResult` -> `VirtualMachine`.
  - Rename the `Visit` field `ipLocation` type `DeprecatedIPLocation` -> `DeprecatedGeolocation`.
    - Instead of `DeprecatedIPLocationCity` use common `GeolocationCity`
  - Rename `Response` -> `VisitorsGetResponse`.
    - Omit extra inner type `ResponseVisits`
  - Rename `VpnResult` -> `VPN`.
    - Extract `confidence` type as `VPNConfidence`.
    - Extract `methods` type as `VPNMethods`.
  - Rename `WebhookVisit` -> `Webhook`.
    - Introduce new inner types: `WebhookRootApps`, `WebhookEmulator`, `WebhookIPInfo`, `WebhookIPBlocklist`, `WebhookTor`, `WebhookVPN`, `WebhookProxy`, `WebhookTampering`, `WebhookClonedApp`, `WebhookFactoryReset`, `WebhookJailbroken`, `WebhookFrida`, `WebhookPrivacySettings`, `WebhookVirtualMachine`, `WebhookRawDeviceAttributes`, `WebhookHighActivity`, `WebhookLocationSpoofing`, `WebhookSuspectScore`, `WebhookRemoteControl`, `WebhookVelocity`, `WebhookDeveloperTools`. ([8df1d4a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8df1d4acf7c26bd72bce13c04d9ea1a85f2b0155))
- Rename `Webhook` class to `WebhookValidation`.
  Right now, `Webhook` class points to the actual data model. ([8710516](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/871051665e6fe50a6a1f6fdbdb647f67d0418453))

### Minor Changes

- Added new `ipEvents`, `distinctIpByLinkedId`, and `distinctVisitorIdByLinkedId` fields to the `velocity` Smart Signal. ([8df1d4a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8df1d4acf7c26bd72bce13c04d9ea1a85f2b0155))
- - Make the `GeolocationCity` field `name` **required**.
  - Make the `GeolocationSubdivision` field `isoCode` **required**.
  - Make the `GeolocationSubdivision` field `name` **required**.
  - Make the `IPInfoASN` field `name` **required** .
  - Make the `IPInfoDataCenter` field `name` **required**.
  - Add **optional** `IdentificationConfidence` field `comment`.
  - **events**: Add **optional** `Botd` field `meta`.
  - **events**: Add **optional** `Identification` field `components`.
  - **events**: Make the `VPN` field `originCountry` **required**.
  - **visitors**: Add **optional** `Visit` field `components`.
  - **webhook**: Add **optional** `Webhook` field `components`. ([8df1d4a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8df1d4acf7c26bd72bce13c04d9ea1a85f2b0155))
- **events**: Add `antiDetectBrowser` detection method to the `tampering` Smart Signal. ([8df1d4a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8df1d4acf7c26bd72bce13c04d9ea1a85f2b0155))

## 8.0.0-dev.0

### Major Changes

- - Remove the `BrowserDetails` field `botProbability`.
  - Update the `IdentificationConfidence` field `score` type format: `float` -> `double`.
  - Make the `RawDeviceAttributeError` field `name` **optional** .
  - Make the `RawDeviceAttributeError` field `message` **optional** .
  - **events**: Remove the `EventsResponse` field `error`.
    - [note]: The errors are represented by `ErrorResponse` model.
  - **events**: Update the `HighActivity` field `dailyRequests` type format: `number` -> `int64`.
  - **events**: Specify the `Tampering` field `anomalyScore` type format: `double`.
  - **webhook**: Make the `Webhook` fields **optional**: `visitorId`, `visitorFound`, `firstSeenAt`, `lastSeenAt`, `browserDetails`, `incognito`.
  - **webhook**: Make the `WebhookClonedApp` field `result` **optional**.
  - **webhook**: Make the `WebhookDeveloperTools` field `result` **optional**.
  - **webhook**: Make the `WebhookEmulator` field `result` **optional**.
  - **webhook**: Make the `WebhookFactoryReset` fields `time` and `timestamp` **optional**.
  - **webhook**: Make the `WebhookFrida` field `result` **optional**.
  - **webhook**: Update the `WebhookHighActivity` field `dailyRequests` type format: `number` -> `int64`.
  - **webhook**: Make the `WebhookIPBlocklist` fields `result` and `details` **optional**.
  - **webhook**: Make the `WebhookJailbroken` field `result` **optional**.
  - **webhook**: Make the `WebhookLocationSpoofing` field `result` **optional**.
  - **webhook**: Make the `WebhookPrivacySettings` field `result` **optional**.
  - **webhook**: Make the `WebhookProxy` field `result` **optional**.
  - **webhook**: Make the `WebhookRemoteControl` field `result` **optional**.
  - **webhook**: Make the `WebhookRootApps` field `result` **optional**.
  - **webhook**: Make the `WebhookSuspectScore` field `result` **optional**.
  - **webhook**: Make the `WebhookTampering` fields `result`, `anomalyScore` and `antiDetectBrowser` **optional**.
  - **webhook**: Specify the `WebhookTampering` field `anomalyScore` type format: `double`.
  - **webhook**: Make the `WebhookTor` field `result` **optional**.
  - **webhook**: Make the `WebhookVelocity` fields **optional**: `distinctIp`, `distinctLinkedId`, `distinctCountry`, `events`, `ipEvents`, `distinctIpByLinkedId`, `distinctVisitorIdByLinkedId`.
  - **webhook**: Make the `WebhookVirtualMachine` field `result` **optional**.
  - **webhook**: Make the `WebhookVPN` fields **optional**: `result`, `confidence`, `originTimezone`, `methods`. ([8df1d4a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8df1d4acf7c26bd72bce13c04d9ea1a85f2b0155))
- - Rename `BotdResult` -> `Botd`.
  - Rename `BotdDetectionResult` -> `BotdBot`:
    - Extract `result` type as `BotdBotResult`.
  - Rename `ClonedAppResult` -> `ClonedApp`.
  - Rename `DeveloperToolsResult` -> `DeveloperTools`.
  - Rename `EmulatorResult` -> `Emulator`.
  - Refactor error models:
    - Remove `ErrorCommon403Response`, `ErrorCommon429Response`, `ErrorEvent404Response`, `TooManyRequestsResponse`, `ErrorVisits403`, `ErrorUpdateEvent400Response`, `ErrorUpdateEvent409Response`, `ErrorVisitor400Response`, `ErrorVisitor404Response`, `IdentificationError`, `ProductError`.
    - Introduce `ErrorResponse` and `ErrorPlainResponse`.
      - [note]: `ErrorPlainResponse` has a different format `{ "error": string }` and it is used only in `GET /visitors`.
    - Extract `error` type as `Error`.
    - Extract `error.code` type as `ErrorCode`.
  - Rename `EventResponse` -> `EventsGetResponse`.
  - Rename `EventUpdateRequest` -> `EventsUpdateRequest`.
  - Rename `FactoryResetResult` -> `FactoryReset`.
  - Rename `FridaResult` -> `Frida`.
  - Rename `IPLocation` -> `Geolocation`:
    - Rename `IPLocationCity` -> `GeolocationCity`.
    - Extract `subdivisions` type as `GeolocationSubdivisions`.
    - Rename `Location` -> `GeolocationContinent`:
    - Introduce a dedicated type `GeolocationCountry`.
    - Rename `Subdivision` -> `GeolocationSubdivision`.
  - Rename `HighActivityResult` -> `HighActivity`.
  - Rename `Confidence` -> `IdentificationConfidence`.
  - Rename `SeenAt` -> `IdentificationSeenAt`.
  - Rename `IncognitoResult` -> `Incognito`.
  - Rename `IpBlockListResult` -> `IPBlocklist`:
    - Extract `details` type as `IPBlocklistDetails`.
  - Rename `IpInfoResult` -> `IPInfo`:
    - Rename `IpInfoResultV4` -> `IPInfoV4`.
    - Rename `IpInfoResultV6` -> `IPInfoV6`.
    - Rename `ASN` -> `IPInfoASN`.
    - Rename `DataCenter` -> `IPInfoDataCenter`.
  - Rename `JailbrokenResult` -> `Jailbroken`.
  - Rename `LocationSpoofingResult` -> `LocationSpoofing`.
  - Rename `PrivacySettingsResult` -> `PrivacySettings`.
  - Rename `ProductsResponse` -> `Products`:
    - Rename inner types: `ProductsResponseIdentification` -> `ProductIdentification`, `ProductsResponseIdentificationData` -> `Identification`, `ProductsResponseBotd` -> `ProductBotd`, `SignalResponseRootApps` -> `ProductRootApps`, `SignalResponseEmulator` -> `ProductEmulator`, `SignalResponseIpInfo` -> `ProductIPInfo`, `SignalResponseIpBlocklist` -> `ProductIPBlocklist`, `SignalResponseTor` -> `ProductTor`, `SignalResponseVpn` -> `ProductVPN`, `SignalResponseProxy` -> `ProductProxy`, `ProxyResult` -> `Proxy`, `SignalResponseIncognito` -> `ProductIncognito`, `SignalResponseTampering` -> `ProductTampering`, `SignalResponseClonedApp` -> `ProductClonedApp`, `SignalResponseFactoryReset` -> `ProductFactoryReset`, `SignalResponseJailbroken` -> `ProductJailbroken`, `SignalResponseFrida` -> `ProductFrida`, `SignalResponsePrivacySettings` -> `ProductPrivacySettings`, `SignalResponseVirtualMachine` -> `ProductVirtualMachine`, `SignalResponseRawDeviceAttributes` -> `ProductRawDeviceAttributes`, `RawDeviceAttributesResultValue` -> `RawDeviceAttributes`, `SignalResponseHighActivity` -> `ProductHighActivity`, `SignalResponseLocationSpoofing` -> `ProductLocationSpoofing`, `SignalResponseSuspectScore` -> `ProductSuspectScore`, `SignalResponseRemoteControl` -> `ProductRemoteControl`, `SignalResponseVelocity` -> `ProductVelocity`, `SignalResponseDeveloperTools` -> `ProductDeveloperTools`.
    - Extract `identification.data` type as `Identification`.
  - Rename `RawDeviceAttributesResult` -> `RawDeviceAttributes`:
    - Extract item type as `RawDeviceAttribute`.
    - Extract `error` type as `RawDeviceAttributeError`.
  - Rename `RemoteControlResult` -> `RemoteControl`.
  - Rename `RootAppsResult` -> `RootApps`.
  - Rename `SuspectScoreResult` -> `SuspectScore`.
  - Extract new model `Tag`.
  - Rename `TamperingResult` -> `Tampering`.
  - Rename `TorResult` -> `Tor`.
  - Rename `VelocityResult` -> `Velocity`:
    - Rename `VelocityIntervals` -> `VelocityData`.
    - Rename `VelocityIntervalResult` -> `VelocityIntervals`.
  - Rename `VirtualMachineResult` -> `VirtualMachine`.
  - Rename the `Visit` field `ipLocation` type `DeprecatedIPLocation` -> `DeprecatedGeolocation`.
    - Instead of `DeprecatedIPLocationCity` use common `GeolocationCity`
  - Rename `Response` -> `VisitorsGetResponse`.
    - Omit extra inner type `ResponseVisits`
  - Rename `VpnResult` -> `VPN`.
    - Extract `confidence` type as `VPNConfidence`.
    - Extract `methods` type as `VPNMethods`.
  - Rename `WebhookVisit` -> `Webhook`.
    - Introduce new inner types: `WebhookRootApps`, `WebhookEmulator`, `WebhookIPInfo`, `WebhookIPBlocklist`, `WebhookTor`, `WebhookVPN`, `WebhookProxy`, `WebhookTampering`, `WebhookClonedApp`, `WebhookFactoryReset`, `WebhookJailbroken`, `WebhookFrida`, `WebhookPrivacySettings`, `WebhookVirtualMachine`, `WebhookRawDeviceAttributes`, `WebhookHighActivity`, `WebhookLocationSpoofing`, `WebhookSuspectScore`, `WebhookRemoteControl`, `WebhookVelocity`, `WebhookDeveloperTools`. ([8df1d4a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8df1d4acf7c26bd72bce13c04d9ea1a85f2b0155))

### Minor Changes

- Added new `ipEvents`, `distinctIpByLinkedId`, and `distinctVisitorIdByLinkedId` fields to the `velocity` Smart Signal. ([8df1d4a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8df1d4acf7c26bd72bce13c04d9ea1a85f2b0155))
- - Make the `GeolocationCity` field `name` **required**.
  - Make the `GeolocationSubdivision` field `isoCode` **required**.
  - Make the `GeolocationSubdivision` field `name` **required**.
  - Make the `IPInfoASN` field `name` **required** .
  - Make the `IPInfoDataCenter` field `name` **required**.
  - Add **optional** `IdentificationConfidence` field `comment`.
  - **events**: Add **optional** `Botd` field `meta`.
  - **events**: Add **optional** `Identification` field `components`.
  - **events**: Make the `VPN` field `originCountry` **required**.
  - **visitors**: Add **optional** `Visit` field `components`.
  - **webhook**: Add **optional** `Webhook` field `components`. ([8df1d4a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8df1d4acf7c26bd72bce13c04d9ea1a85f2b0155))
- **events**: Add `antiDetectBrowser` detection method to the `tampering` Smart Signal. ([8df1d4a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8df1d4acf7c26bd72bce13c04d9ea1a85f2b0155))

## 7.1.0

### Minor Changes

- **visitors**: Add the confidence field to the VPN Detection Smart Signal ([e98dbd4](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/e98dbd4675bdb28f5e98c4a670612e3f8d0aa671))

## 7.1.0-rc.0

### Minor Changes

- **visitors**: Add the confidence field to the VPN Detection Smart Signal ([e98dbd4](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/e98dbd4675bdb28f5e98c4a670612e3f8d0aa671))

## [7.0.1](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/compare/v7.0.0...v7.0.1) (2024-08-22)

### Bug Fixes

- deserialize `raw_device_attributes.data` to correct type `RawDeviceAttributesResult` ([743db13](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/743db13b384003a6fffd4124936db29fa7e9a850))

## [7.0.0](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/compare/v6.0.0...v7.0.0) (2024-08-14)

### ⚠ BREAKING CHANGES

- rename `unseal_events_response` to `unseal_event_response` to keep proper naming
- minimum supported Python version is 3.9 now
- rename `error_event403_response`, `error_event403_response_error`, `many_requests_response` to `common403_error_response`, `error_common403_response` `too_many_requests_response`

### Features

- add `delete_visitor_data` method ([961a165](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/961a165bd1acf43797dd3767fc3c1d72cc541917))
- add `developer_tools` signal ([ca25ef7](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/ca25ef7f07acbf47a7e5a55092bd336050cd0967))
- add `osMismatch` field to the `vpn` signal ([0b95bda](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/0b95bdadaad62285558c442cf36b3990668537c1))
- add `remoteControl` signal ([5c7b149](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5c7b1493dfa84ddab2df753c4c856da808bf844d))
- add `revision` field to the `confidence` signal ([9b42d6b](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9b42d6b984a0c8c65a98faeea21bd86460a51df1))
- add `update_event` method ([752b1c9](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/752b1c97054a131afcb3582a58a77f6a4d8b1816))
- add `velocity` signal ([9b31367](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9b313677da304c8090518f484406694c7b1123b8))
- add better error reporting in case of wrong data shape ([40e9e6a](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/40e9e6a4a7d743d853c6defcb2f0ae6aa78f5e7e))
- add webhook validation method ([d92b1fe](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/d92b1fe9a69e943926c729affa6ef7b91a0857d8))
- create base class for models and move here utility functions ([bfa2285](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/bfa2285cd45136c970cc3d07b1ada56874011c98))
- drop Python 3.8 support ([d857954](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/d857954e826b05f2061d195b2a2a8c3cae5b0232))
- simplify `Configuration` class, use inline types ([8cad048](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8cad04860ec59b6a57d50827fb288871c2dbf384))
- simplify `rest.py` and `api_client.py` and add inline types ([a8b1ae6](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/a8b1ae61d74ff5eaca09012741be4a894ff8526e))
- update schema ([c2e99cd](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/c2e99cd104e6ab9c7e9f670636d984e829eb2747))
- use inline types for `fingerprint_api.py` ([c466bd5](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/c466bd58f1838baf0b6bbf5aac2de6b0a047630b))
- use inline types instead of annotations for models ([1121a5c](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/1121a5c5e81d3458595d2bd7920463cce0b661ac))

### Bug Fixes

- `unseal_event_response` returns correct `EventResponse` structure ([a7a0e2d](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/a7a0e2d3c0c42fb225545673954ee816917d3124))
- don't serialise empty fields in models ([9643e1d](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9643e1d7781e0d1eb414f8f5177cdace16ef3063))
- make `tag` field optional for webhook ([e8a28f6](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/e8a28f69d08a7969af3b1b66ef399aacd4bc14d1))
- mark optional fields in models ([2c62e20](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/2c62e209de1d09ebd58f3174a0be81e39c6d8bf6))
- remove Python2 compatibility code ([2621ccd](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/2621ccddb01c495a8a385766d15ea875171260e8))
- update schema with required `body` field for the `updateEvent` method ([c6eaf5e](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/c6eaf5e64d387ce55a898ba800b8989e77c5cae0))

## [6.0.0](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/compare/v5.0.0...v6.0.0) (2024-03-27)

### ⚠ BREAKING CHANGES

- now only Python >= 3.8 is supported

### Features

- drop support for python < 3.8 ([1e18e2c](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/1e18e2ccafb6967229922d7783782f2c97cadb64))

## [5.0.0](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/compare/v4.0.0...v5.0.0) (2024-03-20)

### ⚠ BREAKING CHANGES

- make identification field `confidence` optional
- deprecated `ipLocation` field uses `DeprecatedIpLocation` model
- change models for the most smart signals

### Features

- add `linked_id` field to the `BotdResult` type ([3aba5d0](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/3aba5d0c4782696d1974f650ae22ff30deeedd20))
- add `origin_country` field to the `vpn` signal ([27f7c58](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/27f7c580e36b2c6b803c2617462b19d51c886e17))
- add `SuspectScore` smart signal support ([331f2a8](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/331f2a82b31e7a281dfaa7921b015128b147cbe8))
- fix `ipLocation` deprecation ([cb3b7b1](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/cb3b7b1ade37fc3d221e2fa46c5d691a85a37248))
- make identification field `tag` required ([678a3a1](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/678a3a187fe5a10c5811b56dc43daab57e7cdff4))
- use shared structures for webhooks and event ([c15ae21](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/c15ae2107256d29fff02af3cc70b065d93092af3))

### Bug Fixes

- make fields required according to real API response ([8beb757](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/8beb757db67af38b7a112f93f1a7c21ef35e62a8))

## [4.0.0](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/compare/v3.0.0...v4.0.0) (2024-02-14)

### ⚠ BREAKING CHANGES

- now only Python >= 3.6 is supported

### Features

- add method for decoding sealed results ([1acdeea](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/1acdeea7003c599261ae61e5f0a678c88899d85a))
- drop support for python < 3.6 ([82d5213](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/82d5213e95af4a142f0ca49051f270046c972eb5))

## [3.0.0](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/compare/v2.6.0...v3.0.0) (2024-01-12)

### ⚠ BREAKING CHANGES

- `IpInfo` field `data_center` renamed to `datacenter`

### Features

- deprecate `IPLocation` ([b39189b](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/b39189b8a2cee94ab277729033f82460c72c8b38))
- use `datacenter` field instead of the wrong `dataCenter` ([53bcda2](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/53bcda26729b7e7a793c61f7292fa474536ef652))

## [2.6.0](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/compare/v2.5.1...v2.6.0) (2023-11-27)

### Features

- add `highActivity` and `locationSpoofing` signals, support `originTimezone` for `vpn` signal ([36793fe](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/36793feab226c6cfc65c6c156995c7d1f46b5b6d))

## [2.5.1](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/compare/v2.5.0...v2.5.1) (2023-09-20)

### Bug Fixes

- update OpenAPI Schema with `asn` and `dataCenter` signals ([4684316](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4684316e153d1782fd0980e08488a8d7d78d695e))
- update OpenAPI Schema with `auxiliaryMobile` method for VPN signal ([5422741](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5422741d3250c63884eeb5b6f8365e2e4210c47a))

## [2.5.0](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/compare/v2.4.0...v2.5.0) (2023-08-10)

### Features

- make SDK more independent from environment ([1d017c1](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/1d017c158849d9125ca6ba01f414ec0948458769)), closes [#31](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/issues/31)

### Bug Fixes

- fix `multiprocessing.pool` detection fro Lambda ([9373a93](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9373a9360bc6111fe362ea39ea1eea1a86d9bfcf))

# Changelog

<!--next-version-placeholder-->

## v2.4.0 (2023-07-31)

### Feature

- Add raw device attributes support ([`6b81649`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/6b81649005cdd336173dd33ae41143fc8aa4f5ef))
- Add support for smart signals ([`28926b8`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/28926b87954f31f0bbaa917dc7b956217c61e5a6))

### Documentation

- Improve model documentation, add special fix for `RawDeviceAttributesResult` documentation ([`36ddc0d`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/36ddc0df68dc394640e01ad0fd060d353ef7eb63))
- **README:** Use `pagination_key` in README example instead of deprecated `before` ([`5dd6e55`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5dd6e5528bbe710f54e3bd9c5660d15fe5aa548c))

## v2.3.0 (2023-06-06)

### Feature

- Update schema with correct `IpLocation` format and doc updates ([`d501cfa`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/d501cfa13b585e881c0645eed6dd89c09ea46a78))

## v2.2.0 (2023-05-16)

### Feature

- Introduce additional signals ([`4e5fc79`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4e5fc79eebc0d67bd5b451636e60c461f08dd7ee))

## v2.1.0 (2023-02-03)

### Feature

- Improve error reporting by adding `KnownApiException` class ([`f60625a`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/f60625a209525a3591b4e2f1f52c38550f6a303e))

### Fix

- Set `retry_after` to `1` in case of missed header ([`1d5b5b9`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/1d5b5b9ba91b0cf265f31130bc246275abf97f20))
- Add `retry_after` value from header to `ManyRequestsResponse` error ([`25dc803`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/25dc8035626b9dff388cd94b74ecc8fc4f4782a3))
- Update schema ([`c9be3d3`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/c9be3d36266e065fa606591fef6c6357f14e8556))

### Documentation

- Extend example with new error reporting ([`d78d12b`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/d78d12bbe44116c75d1deb802cc386fd12b993eb))

## v2.0.0 (2023-01-16)

### Feature

- Update schema ([`065f23c`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/065f23cd8afc3f87a9186927942b86a75981c6f8))

### Breaking

- `StSeenAt` type renamed to `SeenAt` ([`065f23c`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/065f23cd8afc3f87a9186927942b86a75981c6f8))

### Documentation

- Add coverage badge ([`f8c6236`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/f8c623687b3b41422606b763b81e0f4e98a97bc4))
- Add instruction how to run tests ([`5eb8115`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5eb81158eba44968d40725d66da2dfa24d54c9cd))

## v1.3.0 (2022-10-25)

### Feature

- Update schema to support url field for botd result ([`24bfdf0`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/24bfdf0339bf9965b7e5a31e0871304c87562c7e))

### Fix

- Restore some parts of api_doc.mustache template from swagger-codegen repository ([`5b6b531`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5b6b531244cebbf00b8f1d8bc580301ed5b7ac01))

## v1.2.0 (2022-09-14)

### Feature

- Introduce /event/{request_id} endpoint ([`3e587d0`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/3e587d08b6b02532667c382daf27f05a80a98a4b))

### Documentation

- **README:** Add examples to readme ([`13256fd`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/13256fd34a1275c9c3a9ca8c01cd5beb1fafa668))

## v1.1.0 (2022-08-25)

### Feature

- Support nullable types ([`7ac3b07`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/7ac3b07a9622ddeb9e332a793f02f8112bcd3b7f))

### Fix

- Regenerate schema with nullable types support ([`9c05f3e`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9c05f3e9492c3a1374ef5a950b95420be9600af5))

## v1.0.0 (2022-08-24)

### Feature

- Stable release ([`993a34a`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/993a34af407279b75b98d1b72e439e799c072cae))

### Breaking

- stable release ([`993a34a`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/993a34af407279b75b98d1b72e439e799c072cae))

## v0.0.4 (2022-08-19)

### Fix

- Add correct links to documentation from PyPI ([`af8264f`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/af8264f6e9cabc7aa75c1e2b5269045884373600))

### Documentation

- Improve setup instruction ([`c95f794`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/c95f79468050b332313f1bfcf803b249624bf493))
- Remove extra imports, use print instead of pprint in example ([`9cccd53`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9cccd53a7fcf05d60cdab484a2aaf43c5a83038d))
- Add keywords ([`93fc3a2`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/93fc3a2c3c993905a6133776e0dca531ff26e683))

## v0.0.3 (2022-08-17)

### Fix

- Sync version in generated code ([`0181453`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/0181453ea61341188c04bcad4bb81d8769bf5664))
- Update release commit message to not trigger new release ([`9d079ca`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9d079ca4aa0c04b7e77c7f76fe8c3fee673bf9e9))

## v0.0.2 (2022-08-16)

### Documentation

- Add pypi badge ([`af44bbb`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/af44bbb457f6d56e640b944c28ecd9d14e559f53))
- Add ci badges ([`ac20d9e`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/ac20d9ea07b2d1b8cc851a0c25c3318cd81c87e2))

## v0.0.2-beta.9 (2022-08-15)

### Documentation

- Add author ([`ad95a50`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/ad95a5038641a9dc94237894d78bf03cd3ac69e4))
- Update description ([`4b28f0f`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4b28f0fac38700e27d41baee25e857de975af110))

## v0.0.2-beta.8 (2022-08-12)

### Documentation

- Use full url to logo ([`5cd84fa`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5cd84fabbf1a230a41f0e93039e2739227f79597))

## v0.0.2-beta.7 (2022-08-12)

## v0.0.2-beta.6 (2022-08-12)

## v0.0.2-beta.5 (2022-08-12)

## v0.0.2-beta.4 (2022-08-12)
