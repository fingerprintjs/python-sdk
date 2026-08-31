# EdgeRequest
HTTP request metadata (including the HTTP method, headers and IP address) sent by you (your server) to the Fingerprint API for IP and bot analysis. To improve accuracy, retain as much of the original semantics of the HTTP request as possible. For example, preserve the order of the request headers and their capitalization.
At least one of `ipv4_address` or `ipv6_address` must be provided; a request with neither is rejected with a `400` error. If both IPv4 and IPv6 are provided, IP intelligence will be provided for each address. If an IPv4-mapped IPv6 address is provided in the `ipv6_address` request property, the IP intelligence will be provided in the `ipv4_address` property of the response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**List[EdgeRequestHeadersInner]**](EdgeRequestHeadersInner.md) | Ordered header entries from the request made to your server. Each entry represents one header line. If one header name appears as multiple lines, send each as a separate item in the array.  Headers that contain authentication or session data must still be included, but with their value set to an empty string. This includes headers like `Authorization` and `Cookie`, but may contain more depending on your specific project, for instance `Proxy-Authenticate` or `X-Api-Key`. Omitting the headers entirely changes the shape of the request and can affect detection. Never forward the real secret values.  Whenever possible, we recommend preserving header order and capitalization to provide the best accuracy, however it’s not a strict requirement if your runtime does not maintain http header order or canonicalizes header names.  | 
**method** | **str** | The original HTTP method of the request. If supported in your runtime, preserve the original casing. | 
**url** | **str** | Absolute URL of the request, without a \\#fragment suffix. Only HTTP and HTTPS schemes are supported. | 
**ipv4_address** | **str** | Client IPv4 address observed by your server. | [optional] 
**ipv6_address** | **str** | Client IPv6 address observed by your server. | [optional] 
**linked_id** | **str** | A customer-provided id that was sent with the request. | [optional] 
**tags** | **Dict[str, object]** | A customer-provided value or an object that was sent with the identification request or updated later. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

