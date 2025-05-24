# UpdateJobInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**target_list_type** | [**TargetListType**](TargetListType.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.update_job_input import UpdateJobInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateJobInput from a JSON string
update_job_input_instance = UpdateJobInput.from_json(json)
# print the JSON string representation of the object
print(UpdateJobInput.to_json())

# convert the object into a dict
update_job_input_dict = update_job_input_instance.to_dict()
# create an instance of UpdateJobInput from a dict
update_job_input_from_dict = UpdateJobInput.from_dict(update_job_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


