# EventRuleAction
Describes the action the client should take, according to the rule in the ruleset that matched the event. When getting an event by event ID, the rule_action will only be included when the ruleset_id query parameter is specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleset_id** | **str** | The ID of the evaluated ruleset. | 
**rule_id** | **str** | The ID of the rule that matched the identification event. | [optional] 
**rule_expression** | **str** | The expression of the rule that matched the identification event. | [optional] 
**type** | [**RuleActionType**](RuleActionType.md) |  | 
**request_header_modifications** | [**RequestHeaderModifications**](RequestHeaderModifications.md) |  | [optional] 
**status_code** | **int** | A valid HTTP status code. | [optional] 
**headers** | [**List[RuleActionHeaderField]**](RuleActionHeaderField.md) | A list of headers to send. | [optional] 
**body** | **str** | The response body to send to the client. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

