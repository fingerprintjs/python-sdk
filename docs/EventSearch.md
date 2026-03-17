# EventSearch
Contains a list of all identification events matching the specified search criteria.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[Event]**](Event.md) |  | 
**pagination_key** | **str** | Use this value in the `pagination_key` parameter to request the next page of search results. | [optional] 
**total_hits** | **int** | This value represents the total number of events matching the search query, up to the limit provided in the `total_hits` query parameter. Only present if the `total_hits` query parameter was provided. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

