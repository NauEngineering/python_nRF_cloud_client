# FetchFOTAJobExecution200ResponseAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_document** | [**FetchFOTAJobExecution200ResponseAnyOfJobDocument**](FetchFOTAJobExecution200ResponseAnyOfJobDocument.md) |  | 
**status_detail** | **str** |  | 
**status** | [**FotaV2JobExecutionEvents**](FotaV2JobExecutionEvents.md) |  | 
**last_updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**device_id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**job_id** | **str** | Universally unique identifier | 
**execution_id** | **str** | Universally unique identifier | 
**tenant_id** | **str** | Universally unique identifier | 

## Example

```python
from nrf_cloud_client.models.fetch_fota_job_execution200_response_any_of import FetchFOTAJobExecution200ResponseAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of FetchFOTAJobExecution200ResponseAnyOf from a JSON string
fetch_fota_job_execution200_response_any_of_instance = FetchFOTAJobExecution200ResponseAnyOf.from_json(json)
# print the JSON string representation of the object
print(FetchFOTAJobExecution200ResponseAnyOf.to_json())

# convert the object into a dict
fetch_fota_job_execution200_response_any_of_dict = fetch_fota_job_execution200_response_any_of_instance.to_dict()
# create an instance of FetchFOTAJobExecution200ResponseAnyOf from a dict
fetch_fota_job_execution200_response_any_of_from_dict = FetchFOTAJobExecution200ResponseAnyOf.from_dict(fetch_fota_job_execution200_response_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


