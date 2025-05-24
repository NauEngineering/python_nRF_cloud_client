# DeviceFirmwareArgsApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.device_firmware_args_app import DeviceFirmwareArgsApp

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceFirmwareArgsApp from a JSON string
device_firmware_args_app_instance = DeviceFirmwareArgsApp.from_json(json)
# print the JSON string representation of the object
print(DeviceFirmwareArgsApp.to_json())

# convert the object into a dict
device_firmware_args_app_dict = device_firmware_args_app_instance.to_dict()
# create an instance of DeviceFirmwareArgsApp from a dict
device_firmware_args_app_from_dict = DeviceFirmwareArgsApp.from_dict(device_firmware_args_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


