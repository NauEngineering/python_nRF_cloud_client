# Firmware


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**version** | **str** |  | 
**type** | [**FirmwareTypes**](FirmwareTypes.md) |  | 
**bundle_id** | **str** | Unique bundle identifier | 
**filenames** | **List[str]** |  | 
**size** | **float** |  | 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.firmware import Firmware

# TODO update the JSON string below
json = "{}"
# create an instance of Firmware from a JSON string
firmware_instance = Firmware.from_json(json)
# print the JSON string representation of the object
print(Firmware.to_json())

# convert the object into a dict
firmware_dict = firmware_instance.to_dict()
# create an instance of Firmware from a dict
firmware_from_dict = Firmware.from_dict(firmware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


