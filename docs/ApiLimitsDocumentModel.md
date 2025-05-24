# ApiLimitsDocumentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | **float** |  | 
**monthly_fota_job_executions** | **float** |  | 
**monthly_stored_device_messages** | **float** |  | 
**monthly_location_service_requests** | **float** |  | 
**message_routing_service_destinations** | **float** |  | 

## Example

```python
from nrf_cloud_client.models.api_limits_document_model import ApiLimitsDocumentModel

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLimitsDocumentModel from a JSON string
api_limits_document_model_instance = ApiLimitsDocumentModel.from_json(json)
# print the JSON string representation of the object
print(ApiLimitsDocumentModel.to_json())

# convert the object into a dict
api_limits_document_model_dict = api_limits_document_model_instance.to_dict()
# create an instance of ApiLimitsDocumentModel from a dict
api_limits_document_model_from_dict = ApiLimitsDocumentModel.from_dict(api_limits_document_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


