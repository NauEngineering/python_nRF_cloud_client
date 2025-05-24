# FotaV2JobTargetModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_ids** | **List[str]** |  | 
**tags** | **List[str]** |  | 

## Example

```python
from nrf_cloud_client.models.fota_v2_job_target_model import FotaV2JobTargetModel

# TODO update the JSON string below
json = "{}"
# create an instance of FotaV2JobTargetModel from a JSON string
fota_v2_job_target_model_instance = FotaV2JobTargetModel.from_json(json)
# print the JSON string representation of the object
print(FotaV2JobTargetModel.to_json())

# convert the object into a dict
fota_v2_job_target_model_dict = fota_v2_job_target_model_instance.to_dict()
# create an instance of FotaV2JobTargetModel from a dict
fota_v2_job_target_model_from_dict = FotaV2JobTargetModel.from_dict(fota_v2_job_target_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


