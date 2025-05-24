# PickFotaV2JobExecutionModelExcludeKeyofFotaV2JobExecutionModelCreatedAtOrLastUpdatedAtOrDeviceId

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The UUID of the team owning the device(s) | 
**status** | [**FotaV2JobExecutionEvents**](FotaV2JobExecutionEvents.md) |  | 
**execution_id** | **str** | Universally unique identifier | 
**job_id** | **str** | Universally unique identifier | 
**status_detail** | **str** |  | [optional] 
**job_document** | [**FotaV2JobDocumentModel**](FotaV2JobDocumentModel.md) |  | 

## Example

```python
from nrf_cloud_client.models.pick_fota_v2_job_execution_model_exclude_keyof_fota_v2_job_execution_model_created_at_or_last_updated_at_or_device_id import PickFotaV2JobExecutionModelExcludeKeyofFotaV2JobExecutionModelCreatedAtOrLastUpdatedAtOrDeviceId

# TODO update the JSON string below
json = "{}"
# create an instance of PickFotaV2JobExecutionModelExcludeKeyofFotaV2JobExecutionModelCreatedAtOrLastUpdatedAtOrDeviceId from a JSON string
pick_fota_v2_job_execution_model_exclude_keyof_fota_v2_job_execution_model_created_at_or_last_updated_at_or_device_id_instance = PickFotaV2JobExecutionModelExcludeKeyofFotaV2JobExecutionModelCreatedAtOrLastUpdatedAtOrDeviceId.from_json(json)
# print the JSON string representation of the object
print(PickFotaV2JobExecutionModelExcludeKeyofFotaV2JobExecutionModelCreatedAtOrLastUpdatedAtOrDeviceId.to_json())

# convert the object into a dict
pick_fota_v2_job_execution_model_exclude_keyof_fota_v2_job_execution_model_created_at_or_last_updated_at_or_device_id_dict = pick_fota_v2_job_execution_model_exclude_keyof_fota_v2_job_execution_model_created_at_or_last_updated_at_or_device_id_instance.to_dict()
# create an instance of PickFotaV2JobExecutionModelExcludeKeyofFotaV2JobExecutionModelCreatedAtOrLastUpdatedAtOrDeviceId from a dict
pick_fota_v2_job_execution_model_exclude_keyof_fota_v2_job_execution_model_created_at_or_last_updated_at_or_device_id_from_dict = PickFotaV2JobExecutionModelExcludeKeyofFotaV2JobExecutionModelCreatedAtOrLastUpdatedAtOrDeviceId.from_dict(pick_fota_v2_job_execution_model_exclude_keyof_fota_v2_job_execution_model_created_at_or_last_updated_at_or_device_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


