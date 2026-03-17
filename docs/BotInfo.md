# BotInfo
Extended bot information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The type and purpose of the bot. | 
**provider** | **str** | The organization or company operating the bot. | 
**provider_url** | **str** | The URL of the bot provider's website. | [optional] 
**name** | **str** | The specific name or identifier of the bot. | 
**identity** | **str** | The verification status of the bot's identity:  * `verified` - well-known bot with publicly verifiable identity, directed by the bot provider.  * `signed` - bot that signs its platform via Web Bot Auth, directed by the bot provider’s customers.  * `spoofed` - bot that claims a public identity but fails verification.  * `unknown` - bot that does not publish a verifiable identity.  | 
**confidence** | **str** | Confidence level of the bot identification. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

