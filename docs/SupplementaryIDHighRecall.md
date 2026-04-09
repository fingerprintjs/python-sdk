# SupplementaryIDHighRecall
The High Recall ID is a supplementary browser identifier designed for use cases that require wider coverage over precision. Compared to the standard visitor ID, the High Recall ID strives to match incoming browsers more generously (rather than precisely) with existing browsers and thus identifies fewer browsers as new. The High Recall ID is best suited for use cases that are sensitive to browsers being identified as new and where mismatched browsers are not detrimental.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visitor_id** | **str** | The High Recall identifier for the visitor's browser. It is an alphanumeric string with a maximum length of 25 characters. | 
**visitor_found** | **bool** | True if this is a returning browser and has been previously identified. Otherwise, false. | 
**confidence** | [**IdentificationConfidence**](IdentificationConfidence.md) |  | [optional] 
**first_seen_at** | **int** | Unix epoch timestamp (in milliseconds) indicating when the browser was first identified. example: `1758069706642` - Corresponding to Wed Sep 17 2025 00:41:46 GMT+0000  | [optional] 
**last_seen_at** | **int** | Unix epoch timestamp (in milliseconds) corresponding to the most recent visit by this browser. example: `1758069706642` - Corresponding to Wed Sep 17 2025 00:41:46 GMT+0000  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

