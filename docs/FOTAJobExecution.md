# FOTAJobExecution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The UUID of the team owning the device(s) | 
**status** | [**FotaV2JobExecutionEvents**](FotaV2JobExecutionEvents.md) |  | 
**execution_id** | **str** | Universally unique identifier | 
**job_id** | **str** | Universally unique identifier | 
**status_detail** | **str** |  | [optional] 
**job_document** | [**FotaV2JobDocumentModel**](FotaV2JobDocumentModel.md) |  | 
**created_at** | **datetime** |  | 
**device_id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**last_updated_at** | **datetime** |  | 

## Example

```python
from nrf_cloud_client.models.fota_job_execution import FOTAJobExecution

# TODO update the JSON string below
json = "{}"
# create an instance of FOTAJobExecution from a JSON string
fota_job_execution_instance = FOTAJobExecution.from_json(json)
# print the JSON string representation of the object
print(FOTAJobExecution.to_json())

# convert the object into a dict
fota_job_execution_dict = fota_job_execution_instance.to_dict()
# create an instance of FOTAJobExecution from a dict
fota_job_execution_from_dict = FOTAJobExecution.from_dict(fota_job_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


