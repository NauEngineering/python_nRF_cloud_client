# FOTAV2Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Universally unique identifier | 
**target** | [**FotaV2JobTargetModel**](FotaV2JobTargetModel.md) |  | 
**description** | **str** |  | [optional] 
**status** | [**FotaV2JobEvents**](FotaV2JobEvents.md) |  | 
**status_detail** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_updated_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**execution_stats** | [**FOTAV2JobExecutionStats**](FOTAV2JobExecutionStats.md) |  | 
**firmware** | [**FOTAV2JobFirmware**](FOTAV2JobFirmware.md) |  | 

## Example

```python
from nrf_cloud_client.models.fotav2_job import FOTAV2Job

# TODO update the JSON string below
json = "{}"
# create an instance of FOTAV2Job from a JSON string
fotav2_job_instance = FOTAV2Job.from_json(json)
# print the JSON string representation of the object
print(FOTAV2Job.to_json())

# convert the object into a dict
fotav2_job_dict = fotav2_job_instance.to_dict()
# create an instance of FOTAV2Job from a dict
fotav2_job_from_dict = FOTAV2Job.from_dict(fotav2_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


