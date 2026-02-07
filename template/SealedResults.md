# Sealed results 

## **UnsealEventResponse**
> unseal_event_response(sealed: bytes, keys: DecryptionKey[]) -> Event

Decrypts the sealed response with provided keys.
### Required Parameters

| Name       | Type                | Description                                                                              | Notes |
|------------|---------------------|------------------------------------------------------------------------------------------|-------|
| **sealed** | **bytes**           | Base64 encoded sealed data                                                               |       |
| **keys**   | **DecryptionKey[]** | Decryption keys. The SDK will try to decrypt the result with each key until it succeeds. |       |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
