# PaginatedResultFOTAV2JobOrFotaJobV2PlusItemsInner


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
from nrf_cloud_client.models.paginated_result_fotav2_job_or_fota_job_v2_plus_items_inner import PaginatedResultFOTAV2JobOrFotaJobV2PlusItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultFOTAV2JobOrFotaJobV2PlusItemsInner from a JSON string
paginated_result_fotav2_job_or_fota_job_v2_plus_items_inner_instance = PaginatedResultFOTAV2JobOrFotaJobV2PlusItemsInner.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultFOTAV2JobOrFotaJobV2PlusItemsInner.to_json())

# convert the object into a dict
paginated_result_fotav2_job_or_fota_job_v2_plus_items_inner_dict = paginated_result_fotav2_job_or_fota_job_v2_plus_items_inner_instance.to_dict()
# create an instance of PaginatedResultFOTAV2JobOrFotaJobV2PlusItemsInner from a dict
paginated_result_fotav2_job_or_fota_job_v2_plus_items_inner_from_dict = PaginatedResultFOTAV2JobOrFotaJobV2PlusItemsInner.from_dict(paginated_result_fotav2_job_or_fota_job_v2_plus_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


