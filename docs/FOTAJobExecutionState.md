# FOTAJobExecutionState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**status** | **str** |  | 
**status_detail** | **str** |  | [optional] 
**last_updated_at** | **datetime** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.fota_job_execution_state import FOTAJobExecutionState

# TODO update the JSON string below
json = "{}"
# create an instance of FOTAJobExecutionState from a JSON string
fota_job_execution_state_instance = FOTAJobExecutionState.from_json(json)
# print the JSON string representation of the object
print(FOTAJobExecutionState.to_json())

# convert the object into a dict
fota_job_execution_state_dict = fota_job_execution_state_instance.to_dict()
# create an instance of FOTAJobExecutionState from a dict
fota_job_execution_state_from_dict = FOTAJobExecutionState.from_dict(fota_job_execution_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


