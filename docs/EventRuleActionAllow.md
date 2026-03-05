# EventRuleActionAllow
Informs the client that the request should be forwarded to the origin with optional request header modifications.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleset_id** | **str** | The ID of the evaluated ruleset. | 
**rule_id** | **str** | The ID of the rule that matched the identification event. | [optional] 
**rule_expression** | **str** | The expression of the rule that matched the identification event. | [optional] 
**type** | [**RuleActionType**](RuleActionType.md) |  | 
**request_header_modifications** | [**RequestHeaderModifications**](RequestHeaderModifications.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

