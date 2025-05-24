# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**name** | **str** | Friendly device name. Can be used for searching and filtering devices. | 
**image** | **str** |  | [optional] 
**tags** | **List[str]** |  | 
**tenant_id** | **str** | The UUID of the team owning the device(s) | 
**sub_type** | [**GatewayDeviceSubType**](GatewayDeviceSubType.md) |  | 
**firmware** | [**DeviceFirmwareArgs**](DeviceFirmwareArgs.md) |  | [optional] 
**meta** | [**DeviceDocMeta**](DeviceDocMeta.md) |  | 
**cloud_mqtt_enabled** | **bool** | This describes if the device has been fully onboarded to the cloud, and has the proper certificates to connect via MQTT. It may take up to 5 minutes for this to be updated after a certificate is registered to the cloud. | [optional] [default to False]
**type** | [**DeviceTypesGateway**](DeviceTypesGateway.md) |  | 
**state** | [**DeviceShadow**](DeviceShadow.md) |  | [optional] 
**gateway_id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 

## Example

```python
from nrf_cloud_client.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


