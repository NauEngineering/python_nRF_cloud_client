# ObservingDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | **str** |  | [optional] 
**firmware_version** | **str** |  | [optional] 
**modem_version** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.observing_device import ObservingDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ObservingDevice from a JSON string
observing_device_instance = ObservingDevice.from_json(json)
# print the JSON string representation of the object
print(ObservingDevice.to_json())

# convert the object into a dict
observing_device_dict = observing_device_instance.to_dict()
# create an instance of ObservingDevice from a dict
observing_device_from_dict = ObservingDevice.from_dict(observing_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


