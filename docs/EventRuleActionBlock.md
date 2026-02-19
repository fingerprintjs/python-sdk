# EventRuleActionBlock
Informs the client the request should be blocked using the response described by this rule action.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleset_id** | **str** | The ID of the evaluated ruleset. | 
**rule_id** | **str** | The ID of the rule that matched the identification event. | [optional] 
**rule_expression** | **str** | The expression of the rule that matched the identification event. | [optional] 
**type** | [**RuleActionType**](RuleActionType.md) |  | 
**status_code** | **int** | A valid HTTP status code. | [optional] 
**headers** | [**List[RuleActionHeaderField]**](RuleActionHeaderField.md) | A list of headers to send. | [optional] 
**body** | **str** | The response body to send to the client. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

