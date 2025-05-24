# GpsRequest


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
from nrf_cloud_client.models.gps_request import GpsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GpsRequest from a JSON string
gps_request_instance = GpsRequest.from_json(json)
# print the JSON string representation of the object
print(GpsRequest.to_json())

# convert the object into a dict
gps_request_dict = gps_request_instance.to_dict()
# create an instance of GpsRequest from a dict
gps_request_from_dict = GpsRequest.from_dict(gps_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


