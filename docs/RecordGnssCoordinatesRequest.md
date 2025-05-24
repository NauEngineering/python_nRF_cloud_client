# RecordGnssCoordinatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | WGS 84 geodetic grid line, north to south. | 
**lon** | **float** | WGS 84 geodetic grid line, east to west. | 
**acc** | **float** | Accuracy in (2D 1-sigma) in meters. | [optional] 
**alt** | **float** | Altitude above WGS 84 ellipsoid in meters. | [optional] 
**spd** | **float** | Horizontal speed in meters per second. | [optional] 
**hdg** | **float** | Heading of movement in degrees. | [optional] 

## Example

```python
from nrf_cloud_client.models.record_gnss_coordinates_request import RecordGnssCoordinatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordGnssCoordinatesRequest from a JSON string
record_gnss_coordinates_request_instance = RecordGnssCoordinatesRequest.from_json(json)
# print the JSON string representation of the object
print(RecordGnssCoordinatesRequest.to_json())

# convert the object into a dict
record_gnss_coordinates_request_dict = record_gnss_coordinates_request_instance.to_dict()
# create an instance of RecordGnssCoordinatesRequest from a dict
record_gnss_coordinates_request_from_dict = RecordGnssCoordinatesRequest.from_dict(record_gnss_coordinates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


