# RawDeviceAttributes
A curated subset of raw browser/device attributes that the API surface exposes. Each property contains a value or object with the data for the collected signal.


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font_preferences** | [**FontPreferences**](FontPreferences.md) |  | [optional] 
**emoji** | [**Emoji**](Emoji.md) |  | [optional] 
**fonts** | **List[str]** | List of fonts detected on the device. | [optional] 
**device_memory** | **int** | Rounded amount of RAM (in gigabytes) reported by the browser. | [optional] 
**timezone** | **str** | Timezone identifier detected on the client. | [optional] 
**canvas** | [**Canvas**](Canvas.md) |  | [optional] 
**languages** | **List[List[str]]** | Navigator languages reported by the agent including fallbacks. Each inner array represents ordered language preferences reported by different APIs.  | [optional] 
**webgl_extensions** | [**WebGlExtensions**](WebGlExtensions.md) |  | [optional] 
**webgl_basics** | [**WebGlBasics**](WebGlBasics.md) |  | [optional] 
**screen_resolution** | **List[int]** | Current screen resolution. | [optional] 
**touch_support** | [**TouchSupport**](TouchSupport.md) |  | [optional] 
**oscpu** | **str** | Navigator `oscpu` string. | [optional] 
**architecture** | **int** | Integer representing the CPU architecture exposed by the browser. | [optional] 
**cookies_enabled** | **bool** | Whether the cookies are enabled in the browser. | [optional] 
**hardware_concurrency** | **int** | Number of logical CPU cores reported by the browser. | [optional] 
**date_time_locale** | **str** | Locale derived from the Intl.DateTimeFormat API. Negative values indicate known error states. The negative statuses can be: - \"-1\": A permanent status for browsers that don't support Intl API. - \"-2\": A permanent status for browsers that don't supportDateTimeFormat constructor. - \"-3\": A permanent status for browsers in which DateTimeFormat locale is undefined or null.  | [optional] 
**vendor** | **str** | Navigator vendor string. | [optional] 
**color_depth** | **int** | Screen color depth in bits. | [optional] 
**platform** | **str** | Navigator platform string. | [optional] 
**session_storage** | **bool** | Whether sessionStorage is available. | [optional] 
**local_storage** | **bool** | Whether localStorage is available. | [optional] 
**audio** | **float** | AudioContext fingerprint or negative status when unavailable. The negative statuses can be: - -1: A permanent status for those browsers which are known to always suspend audio context - -2: A permanent status for browsers that don't support the signal - -3: A temporary status that means that an unexpected timeout has happened  | [optional] 
**plugins** | [**List[PluginsInner]**](PluginsInner.md) | Browser plugins reported by `navigator.plugins`. | [optional] 
**indexed_db** | **bool** | Whether IndexedDB is available. | [optional] 
**math** | **str** | Hash of Math APIs used for entropy collection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

