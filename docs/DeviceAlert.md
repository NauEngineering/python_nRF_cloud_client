# DeviceAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Universally unique identifier | 
**device_id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**created_at** | **datetime** | HTML-encoded ISO-8601 date-time string denoting the start or end of a date range. If the string includes only a date, the time is the beginning of the day (00:00:00). | [optional] 
**received_at** | **datetime** | HTML-encoded ISO-8601 date-time string denoting the start or end of a date range. If the string includes only a date, the time is the beginning of the day (00:00:00). | 
**status_changed_at** | **datetime** | HTML-encoded ISO-8601 date-time string denoting the start or end of a date range. If the string includes only a date, the time is the beginning of the day (00:00:00). | [optional] 
**status_changed_by** | **str** | Universally unique identifier | [optional] 
**status** | [**AlertStatus**](AlertStatus.md) |  | 
**original_message** | **object** | The original message sent from the device that triggered the alert. | 

## Example

```python
from nrf_cloud_client.models.device_alert import DeviceAlert

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAlert from a JSON string
device_alert_instance = DeviceAlert.from_json(json)
# print the JSON string representation of the object
print(DeviceAlert.to_json())

# convert the object into a dict
device_alert_dict = device_alert_instance.to_dict()
# create an instance of DeviceAlert from a dict
device_alert_from_dict = DeviceAlert.from_dict(device_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


