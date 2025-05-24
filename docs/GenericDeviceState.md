# GenericDeviceState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reported** | **Dict[str, object]** |  | [optional] 
**desired** | **Dict[str, object]** |  | [optional] 
**delta** | **Dict[str, object]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**version** | **float** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.generic_device_state import GenericDeviceState

# TODO update the JSON string below
json = "{}"
# create an instance of GenericDeviceState from a JSON string
generic_device_state_instance = GenericDeviceState.from_json(json)
# print the JSON string representation of the object
print(GenericDeviceState.to_json())

# convert the object into a dict
generic_device_state_dict = generic_device_state_instance.to_dict()
# create an instance of GenericDeviceState from a dict
generic_device_state_from_dict = GenericDeviceState.from_dict(generic_device_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


