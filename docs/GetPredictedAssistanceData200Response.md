# GetPredictedAssistanceData200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path to the file that contains PGPS prediction data. | 
**host** | **str** | The protocol agnostic URL for accessing PGPS prediction files. | 

## Example

```python
from nrf_cloud_client.models.get_predicted_assistance_data200_response import GetPredictedAssistanceData200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPredictedAssistanceData200Response from a JSON string
get_predicted_assistance_data200_response_instance = GetPredictedAssistanceData200Response.from_json(json)
# print the JSON string representation of the object
print(GetPredictedAssistanceData200Response.to_json())

# convert the object into a dict
get_predicted_assistance_data200_response_dict = get_predicted_assistance_data200_response_instance.to_dict()
# create an instance of GetPredictedAssistanceData200Response from a dict
get_predicted_assistance_data200_response_from_dict = GetPredictedAssistanceData200Response.from_dict(get_predicted_assistance_data200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


