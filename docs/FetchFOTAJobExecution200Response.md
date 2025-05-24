# FetchFOTAJobExecution200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Universally unique identifier | 
**status** | [**FotaV2JobExecutionEvents**](FotaV2JobExecutionEvents.md) |  | 
**execution_id** | **str** | Universally unique identifier | 
**job_id** | **str** | Universally unique identifier | 
**status_detail** | **str** |  | 
**job_document** | [**FetchFOTAJobExecution200ResponseAnyOfJobDocument**](FetchFOTAJobExecution200ResponseAnyOfJobDocument.md) |  | 
**created_at** | **datetime** |  | 
**device_id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**last_updated_at** | **datetime** |  | 

## Example

```python
from nrf_cloud_client.models.fetch_fota_job_execution200_response import FetchFOTAJobExecution200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FetchFOTAJobExecution200Response from a JSON string
fetch_fota_job_execution200_response_instance = FetchFOTAJobExecution200Response.from_json(json)
# print the JSON string representation of the object
print(FetchFOTAJobExecution200Response.to_json())

# convert the object into a dict
fetch_fota_job_execution200_response_dict = fetch_fota_job_execution200_response_instance.to_dict()
# create an instance of FetchFOTAJobExecution200Response from a dict
fetch_fota_job_execution200_response_from_dict = FetchFOTAJobExecution200Response.from_dict(fetch_fota_job_execution200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


