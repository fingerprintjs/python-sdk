# IncrementalIdentificationStatus
Only included for requests using incremental identification.
- `partially_completed` - Indicates this event corresponds to a 'minimal' request. Smart Signals, even if included in your plan, are not computed; hence, their values must be ignored.
- `completed` - Indicates this event corresponds to a 'complete' request. Smart Signals, if included in your plan, are computed; hence, their values are valid and relevant. 


## Enum

* `PARTIALLY_COMPLETED` (value: `'partially_completed'`)
* `COMPLETED` (value: `'completed'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

