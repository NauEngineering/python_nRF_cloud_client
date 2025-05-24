# DescriptorsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[float]** |  | 
**path** | **str** |  | 
**uuid** | **str** |  | 

## Example

```python
from nrf_cloud_client.models.descriptors_value import DescriptorsValue

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptorsValue from a JSON string
descriptors_value_instance = DescriptorsValue.from_json(json)
# print the JSON string representation of the object
print(DescriptorsValue.to_json())

# convert the object into a dict
descriptors_value_dict = descriptors_value_instance.to_dict()
# create an instance of DescriptorsValue from a dict
descriptors_value_from_dict = DescriptorsValue.from_dict(descriptors_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


