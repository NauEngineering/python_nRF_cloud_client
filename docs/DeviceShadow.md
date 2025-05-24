# DeviceShadow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reported** | **object** | Construct a type with a set of properties K of type T | [optional] 
**desired** | **object** | Construct a type with a set of properties K of type T | [optional] 
**delta** | **object** | Construct a type with a set of properties K of type T | [optional] 
**metadata** | **object** | Construct a type with a set of properties K of type T | [optional] 
**version** | **float** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.device_shadow import DeviceShadow

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceShadow from a JSON string
device_shadow_instance = DeviceShadow.from_json(json)
# print the JSON string representation of the object
print(DeviceShadow.to_json())

# convert the object into a dict
device_shadow_dict = device_shadow_instance.to_dict()
# create an instance of DeviceShadow from a dict
device_shadow_from_dict = DeviceShadow.from_dict(device_shadow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


