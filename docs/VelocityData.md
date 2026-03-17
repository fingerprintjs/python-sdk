# VelocityData
Is absent if the velocity data could not be generated for the visitor Id.


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_5_minutes** | **int** | Count for the last 5 minutes of velocity data, from the time of the event.  | 
**var_1_hour** | **int** | Count for the last 1 hour of velocity data, from the time of the event.  | 
**var_24_hours** | **int** | The `24_hours` interval of `distinct_ip`, `distinct_linked_id`, `distinct_country`, `distinct_ip_by_linked_id` and `distinct_visitor_id_by_linked_id` will be omitted if the number of `events` for the visitor Id in the last 24 hours (`events.['24_hours']`) is higher than 20.000.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

