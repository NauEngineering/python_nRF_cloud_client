# CharacteristicsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptors** | [**Dict[str, DescriptorsValue]**](DescriptorsValue.md) |  | 
**properties** | [**CharacteristicsValueProperties**](CharacteristicsValueProperties.md) |  | 
**value** | **List[float]** |  | 
**handle** | **float** |  | [optional] 
**path** | **str** |  | 
**uuid** | **str** |  | 

## Example

```python
from nrf_cloud_client.models.characteristics_value import CharacteristicsValue

# TODO update the JSON string below
json = "{}"
# create an instance of CharacteristicsValue from a JSON string
characteristics_value_instance = CharacteristicsValue.from_json(json)
# print the JSON string representation of the object
print(CharacteristicsValue.to_json())

# convert the object into a dict
characteristics_value_dict = characteristics_value_instance.to_dict()
# create an instance of CharacteristicsValue from a dict
characteristics_value_from_dict = CharacteristicsValue.from_dict(characteristics_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


