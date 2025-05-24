# LocationTrackerItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Universally unique identifier | 
**device_id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**service_type** | [**TrackerServiceType**](TrackerServiceType.md) |  | 
**inserted_at** | **datetime** | HTML-encoded ISO-8601 date-time string denoting the start or end of a date range. If the string includes only a date, the time is the beginning of the day (00:00:00). | 
**lat** | **str** | GPS latitude. | 
**lon** | **str** | GPS Longitude. | 
**meta** | [**GnssMeta**](GnssMeta.md) |  | 
**uncertainty** | **str** | Radius of the uncertainty circle around the location in meters. Also known as Horizontal Positioning Error (HPE). | 
**anchors** | [**List[AnchorMeta]**](AnchorMeta.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.location_tracker_item import LocationTrackerItem

# TODO update the JSON string below
json = "{}"
# create an instance of LocationTrackerItem from a JSON string
location_tracker_item_instance = LocationTrackerItem.from_json(json)
# print the JSON string representation of the object
print(LocationTrackerItem.to_json())

# convert the object into a dict
location_tracker_item_dict = location_tracker_item_instance.to_dict()
# create an instance of LocationTrackerItem from a dict
location_tracker_item_from_dict = LocationTrackerItem.from_dict(location_tracker_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


