# IdentificationConfidence
The confidence score represents the probability of a false-positive identification. To learn more, visit [Confidence Score](https://docs.fingerprint.com/docs/identification-accuracy-and-confidence#confidence-score). Please note that the confidence score is not yet supported for [High Recall ID](https://docs.fingerprint.com/docs/supplementary-identifiers-highrecall). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | A floating-point number between 0 and 1 that represents the probability of a false-positive identification. For High Recall ID, this value is 0.  | 
**version** | **str** | The version name of the method used to calculate the confidence score. For High Recall ID, this value is \"Not Supported\".  | [optional] 
**comment** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

