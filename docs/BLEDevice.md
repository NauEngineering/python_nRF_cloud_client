# BLEDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**name** | **str** | Friendly device name. Can be used for searching and filtering devices. | 
**image** | **str** |  | [optional] 
**tags** | **List[str]** |  | 
**tenant_id** | **str** | The UUID of the team owning the device(s) | 
**sub_type** | [**BLEDeviceSubType**](BLEDeviceSubType.md) |  | 
**firmware** | [**DeviceFirmwareArgs**](DeviceFirmwareArgs.md) |  | [optional] 
**meta** | [**DeviceDocMeta**](DeviceDocMeta.md) |  | 
**cloud_mqtt_enabled** | **bool** | This describes if the device has been fully onboarded to the cloud, and has the proper certificates to connect via MQTT. It may take up to 5 minutes for this to be updated after a certificate is registered to the cloud. | [optional] [default to False]
**type** | [**DeviceTypesBLE**](DeviceTypesBLE.md) |  | 
**gateway_id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**state** | [**Dict[str, BLEDeviceStateValue]**](BLEDeviceStateValue.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.ble_device import BLEDevice

# TODO update the JSON string below
json = "{}"
# create an instance of BLEDevice from a JSON string
ble_device_instance = BLEDevice.from_json(json)
# print the JSON string representation of the object
print(BLEDevice.to_json())

# convert the object into a dict
ble_device_dict = ble_device_instance.to_dict()
# create an instance of BLEDevice from a dict
ble_device_from_dict = BLEDevice.from_dict(ble_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


