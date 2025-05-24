# CharacteristicsValueProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broadcast** | **bool** |  | [optional] 
**authorized_signed_write** | **bool** |  | [optional] 
**indicate** | **bool** |  | [optional] 
**notify** | **bool** |  | [optional] 
**write** | **bool** |  | [optional] 
**write_without_response** | **bool** |  | [optional] 
**read** | **bool** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.characteristics_value_properties import CharacteristicsValueProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CharacteristicsValueProperties from a JSON string
characteristics_value_properties_instance = CharacteristicsValueProperties.from_json(json)
# print the JSON string representation of the object
print(CharacteristicsValueProperties.to_json())

# convert the object into a dict
characteristics_value_properties_dict = characteristics_value_properties_instance.to_dict()
# create an instance of CharacteristicsValueProperties from a dict
characteristics_value_properties_from_dict = CharacteristicsValueProperties.from_dict(characteristics_value_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


