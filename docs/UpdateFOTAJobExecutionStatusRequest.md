# UpdateFOTAJobExecutionStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** |  | [optional] 
**status** | [**FotaV2JobExecutionEvents**](FotaV2JobExecutionEvents.md) |  | 

## Example

```python
from nrf_cloud_client.models.update_fota_job_execution_status_request import UpdateFOTAJobExecutionStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFOTAJobExecutionStatusRequest from a JSON string
update_fota_job_execution_status_request_instance = UpdateFOTAJobExecutionStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFOTAJobExecutionStatusRequest.to_json())

# convert the object into a dict
update_fota_job_execution_status_request_dict = update_fota_job_execution_status_request_instance.to_dict()
# create an instance of UpdateFOTAJobExecutionStatusRequest from a dict
update_fota_job_execution_status_request_from_dict = UpdateFOTAJobExecutionStatusRequest.from_dict(update_fota_job_execution_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


