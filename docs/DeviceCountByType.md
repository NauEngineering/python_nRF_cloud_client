# DeviceCountByType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generic** | **float** |  | 
**gateway** | **float** |  | 
**bluetooth_le** | **float** |  | 
**total** | **float** |  | 

## Example

```python
from nrf_cloud_client.models.device_count_by_type import DeviceCountByType

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCountByType from a JSON string
device_count_by_type_instance = DeviceCountByType.from_json(json)
# print the JSON string representation of the object
print(DeviceCountByType.to_json())

# convert the object into a dict
device_count_by_type_dict = device_count_by_type_instance.to_dict()
# create an instance of DeviceCountByType from a dict
device_count_by_type_from_dict = DeviceCountByType.from_dict(device_count_by_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


