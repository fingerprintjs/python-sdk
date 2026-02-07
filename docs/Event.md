# Event
Contains results from Fingerprint Identification and all active Smart Signals.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Unique identifier of the user&#39;s request. The first portion of the event_id is a unix epoch milliseconds timestamp For example: &#x60;1758130560902.8tRtrH&#x60;  | 
**timestamp** | **int** | Timestamp of the event with millisecond precision in Unix time. | 
**linked_id** | **str** | A customer-provided id that was sent with the request. | [optional] 
**environment_id** | **str** | Environment Id of the event. For example: &#x60;ae_47abaca3db2c7c43&#x60;  | [optional] 
**suspect** | **bool** | Field is &#x60;true&#x60; if you have previously set the &#x60;suspect&#x60; flag for this event using the [Server API Update event endpoint](https://dev.fingerprint.com/reference/updateevent). | [optional] 
**sdk** | [**SDK**](SDK.md) |  | [optional] 
**replayed** | **bool** | &#x60;true&#x60; if we determined that this payload was replayed, &#x60;false&#x60; otherwise.  | [optional] 
**identification** | [**Identification**](Identification.md) |  | [optional] 
**supplementary_id_high_recall** | [**SupplementaryIDHighRecall**](SupplementaryIDHighRecall.md) |  | [optional] 
**tags** | **Dict[str, object]** | A customer-provided value or an object that was sent with the identification request or updated later. | [optional] 
**url** | **str** | Page URL from which the request was sent. For example &#x60;https://example.com/&#x60;  | [optional] 
**bundle_id** | **str** | Bundle Id of the iOS application integrated with the Fingerprint SDK for the event. For example: &#x60;com.foo.app&#x60;  | [optional] 
**package_name** | **str** | Package name of the Android application integrated with the Fingerprint SDK for the event. For example: &#x60;com.foo.app&#x60;  | [optional] 
**ip_address** | **str** | IP address of the requesting browser or bot. | [optional] 
**user_agent** | **str** | User Agent of the client, for example: &#x60;Mozilla/5.0 (Windows NT 6.1; Win64; x64) ....&#x60;  | [optional] 
**client_referrer** | **str** | Client Referrer field corresponds to the &#x60;document.referrer&#x60; field gathered during an identification request. The value is an empty string if the user navigated to the page directly (not through a link, but, for example, by using a bookmark) For example: &#x60;https://example.com/blog/my-article&#x60;  | [optional] 
**browser_details** | [**BrowserDetails**](BrowserDetails.md) |  | [optional] 
**proximity** | [**Proximity**](Proximity.md) |  | [optional] 
**bot** | [**BotResult**](BotResult.md) |  | [optional] 
**bot_type** | **str** | Additional classification of the bot type if detected.  | [optional] 
**bot_info** | [**BotInfo**](BotInfo.md) |  | [optional] 
**cloned_app** | **bool** | Android specific cloned application detection. There are 2 values:  * &#x60;true&#x60; - Presence of app cloners work detected (e.g. fully cloned application found or launch of it inside of a not main working profile detected). * &#x60;false&#x60; - No signs of cloned application detected or the client is not Android.  | [optional] 
**developer_tools** | **bool** | &#x60;true&#x60; if the browser is Chrome with DevTools open or Firefox with Developer Tools open, &#x60;false&#x60; otherwise.  | [optional] 
**emulator** | **bool** | Android specific emulator detection. There are 2 values:  * &#x60;true&#x60; - Emulated environment detected (e.g. launch inside of AVD).  * &#x60;false&#x60; - No signs of emulated environment detected or the client is not Android.  | [optional] 
**factory_reset_timestamp** | **int** | The time of the most recent factory reset that happened on the **mobile device** is expressed as Unix epoch time. When a factory reset cannot be detected on the mobile device or when the request is initiated from a browser,  this field will correspond to the *epoch* time (i.e 1 Jan 1970 UTC) as a value of 0. See [Factory Reset Detection](https://dev.fingerprint.com/docs/smart-signals-overview#factory-reset-detection) to learn more about this Smart Signal.  | [optional] 
**frida** | **bool** | [Frida](https://frida.re/docs/) detection for Android and iOS devices. There are 2 values: * &#x60;true&#x60; - Frida detected * &#x60;false&#x60; - No signs of Frida or the client is not a mobile device.  | [optional] 
**ip_blocklist** | [**IPBlockList**](IPBlockList.md) |  | [optional] 
**ip_info** | [**IPInfo**](IPInfo.md) |  | [optional] 
**proxy** | **bool** | IP address was used by a public proxy provider or belonged to a known recent residential proxy  | [optional] 
**proxy_confidence** | [**ProxyConfidence**](ProxyConfidence.md) |  | [optional] 
**proxy_details** | [**ProxyDetails**](ProxyDetails.md) |  | [optional] 
**incognito** | **bool** | &#x60;true&#x60; if we detected incognito mode used in the browser, &#x60;false&#x60; otherwise.  | [optional] 
**jailbroken** | **bool** | iOS specific jailbreak detection. There are 2 values:  * &#x60;true&#x60; - Jailbreak detected. * &#x60;false&#x60; - No signs of jailbreak or the client is not iOS.  | [optional] 
**location_spoofing** | **bool** | Flag indicating whether the request came from a mobile device with location spoofing enabled. | [optional] 
**mitm_attack** | **bool** | * &#x60;true&#x60; - When requests made from your users&#39; mobile devices to Fingerprint servers have been intercepted and potentially modified.  * &#x60;false&#x60; - Otherwise or when the request originated from a browser. See [MitM Attack Detection](https://dev.fingerprint.com/docs/smart-signals-reference#mitm-attack-detection) to learn more about this Smart Signal.  | [optional] 
**privacy_settings** | **bool** | &#x60;true&#x60; if the request is from a privacy aware browser (e.g. Tor) or from a browser in which fingerprinting is blocked. Otherwise &#x60;false&#x60;.  | [optional] 
**root_apps** | **bool** | Android specific root management apps detection. There are 2 values:  * &#x60;true&#x60; - Root Management Apps detected (e.g. Magisk). * &#x60;false&#x60; - No Root Management Apps detected or the client isn&#39;t Android.  | [optional] 
**rule_action** | [**EventRuleAction**](EventRuleAction.md) |  | [optional] 
**suspect_score** | **int** | Suspect Score is an easy way to integrate Smart Signals into your fraud protection work flow.  It is a weighted representation of all Smart Signals present in the payload that helps identify suspicious activity. The value range is [0; S] where S is sum of all Smart Signals weights.  See more details here: https://dev.fingerprint.com/docs/suspect-score  | [optional] 
**tampering** | **bool** | Flag indicating browser tampering was detected. This happens when either:   * There are inconsistencies in the browser configuration that cross internal tampering thresholds (see &#x60;tampering_details.anomaly_score&#x60;).   * The browser signature resembles an \&quot;anti-detect\&quot; browser specifically designed to evade fingerprinting (see &#x60;tampering_details.anti_detect_browser&#x60;).  | [optional] 
**tampering_details** | [**TamperingDetails**](TamperingDetails.md) |  | [optional] 
**velocity** | [**Velocity**](Velocity.md) |  | [optional] 
**virtual_machine** | **bool** | &#x60;true&#x60; if the request came from a browser running inside a virtual machine (e.g. VMWare), &#x60;false&#x60; otherwise.  | [optional] 
**vpn** | **bool** | VPN or other anonymizing service has been used when sending the request.  | [optional] 
**vpn_confidence** | [**VpnConfidence**](VpnConfidence.md) |  | [optional] 
**vpn_origin_timezone** | **str** | Local timezone which is used in timezone_mismatch method.  | [optional] 
**vpn_origin_country** | **str** | Country of the request (only for Android SDK version &gt;&#x3D; 2.4.0, ISO 3166 format or unknown).  | [optional] 
**vpn_methods** | [**VpnMethods**](VpnMethods.md) |  | [optional] 
**high_activity_device** | **bool** | Flag indicating if the request came from a high-activity visitor. | [optional] 
**raw_device_attributes** | [**RawDeviceAttributes**](RawDeviceAttributes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

