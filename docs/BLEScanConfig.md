# BLEScanConfig

Parameters for configuring a BLE scan operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_type** | [**BLEScanType**](BLEScanType.md) |  | [optional] 
**scan_timeout** | **int** | Scan timeout between &#x60;1&#x60; and &#x60;65535&#x60; seconds, &#x60;0&#x60; disables timeout. Default &#x3D; &#x60;3&#x60;. | 
**scan_reporting** | **str** | Use &#x60;batch&#x60; to send one message for all advertisements received on scan timeout. Use &#x60;instant&#x60; if every advertisement received shall be sent instantly. Default &#x3D; &#x60;instant&#x60;. | [optional] [default to 'instant']
**filter** | [**BLEScanConfigFilter**](BLEScanConfigFilter.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.ble_scan_config import BLEScanConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BLEScanConfig from a JSON string
ble_scan_config_instance = BLEScanConfig.from_json(json)
# print the JSON string representation of the object
print(BLEScanConfig.to_json())

# convert the object into a dict
ble_scan_config_dict = ble_scan_config_instance.to_dict()
# create an instance of BLEScanConfig from a dict
ble_scan_config_from_dict = BLEScanConfig.from_dict(ble_scan_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


