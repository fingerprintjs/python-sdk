# ProxyDetails
Proxy detection details (present if `proxy` is `true`)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxy_type** | **str** | Proxy type:  * `residential` - proxies that route through residential and telecom IP addresses to appear as legitimate traffic  * `data_center` - proxies which route through data centers  * `unknown` - reported when a proxy is detected solely by the ML model and the IP sources did not determine a specific type  | 
**last_seen_at** | **int** | Unix millisecond timestamp with hourly resolution of when this IP was last seen as a proxy  | [optional] 
**provider** | **str** | String representing the last proxy service provider detected when this IP was synced. An IP can be shared by multiple service providers.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

