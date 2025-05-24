# FotaJobV2PlusTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firmware_versions** | **List[str]** |  | [optional] 
**firmware_type** | [**FirmwareTypes**](FirmwareTypes.md) |  | [optional] 
**tags** | **List[str]** |  | 
**device_ids** | **List[str]** |  | 

## Example

```python
from nrf_cloud_client.models.fota_job_v2_plus_target import FotaJobV2PlusTarget

# TODO update the JSON string below
json = "{}"
# create an instance of FotaJobV2PlusTarget from a JSON string
fota_job_v2_plus_target_instance = FotaJobV2PlusTarget.from_json(json)
# print the JSON string representation of the object
print(FotaJobV2PlusTarget.to_json())

# convert the object into a dict
fota_job_v2_plus_target_dict = fota_job_v2_plus_target_instance.to_dict()
# create an instance of FotaJobV2PlusTarget from a dict
fota_job_v2_plus_target_from_dict = FotaJobV2PlusTarget.from_dict(fota_job_v2_plus_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


