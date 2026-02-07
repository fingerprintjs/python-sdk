# EventRuleActionBlock
Informs the client the request should be blocked using the response described by this rule action.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RuleActionType**](RuleActionType.md) |  | 
**status_code** | **int** | A valid HTTP status code. | [optional] 
**headers** | [**List[RuleActionHeaderField]**](RuleActionHeaderField.md) | A list of headers to send. | [optional] 
**body** | **str** | The response body to send to the client. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

