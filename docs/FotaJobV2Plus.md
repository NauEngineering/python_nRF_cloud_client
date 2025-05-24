# FotaJobV2Plus

Elivagar FOTA Job definition for integration with device-job-service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Universally unique identifier | 
**target** | [**FotaJobV2PlusTarget**](FotaJobV2PlusTarget.md) |  | 
**description** | **str** |  | [optional] 
**status** | [**FotaV2JobEvents**](FotaV2JobEvents.md) |  | 
**status_detail** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_updated_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**execution_stats** | [**FOTAV2JobExecutionStats**](FOTAV2JobExecutionStats.md) |  | 
**firmware** | [**FOTAV2JobFirmware**](FOTAV2JobFirmware.md) |  | 
**schedule** | [**JobSchedule**](JobSchedule.md) |  | [optional] 
**target_list_type** | [**TargetListType**](TargetListType.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.fota_job_v2_plus import FotaJobV2Plus

# TODO update the JSON string below
json = "{}"
# create an instance of FotaJobV2Plus from a JSON string
fota_job_v2_plus_instance = FotaJobV2Plus.from_json(json)
# print the JSON string representation of the object
print(FotaJobV2Plus.to_json())

# convert the object into a dict
fota_job_v2_plus_dict = fota_job_v2_plus_instance.to_dict()
# create an instance of FotaJobV2Plus from a dict
fota_job_v2_plus_from_dict = FotaJobV2Plus.from_dict(fota_job_v2_plus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


