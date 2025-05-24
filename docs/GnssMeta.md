# GnssMeta

Metadata sent from device when reporting GNSS location in PVT format. Can include other non-gnss related key/value pairs for easy retrieval later. Only populated for GNSS PVT formatted fixes, empty object otherwise.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acc** | **float** | Accuracy in (2D 1-sigma) in meters. | 
**alt** | **float** | Altitude above WGS 84 ellipsoid in meters. | 
**spd** | **float** | Horizontal speed in meters per second. | 
**hdg** | **float** | Heading of movement in degrees. | 

## Example

```python
from nrf_cloud_client.models.gnss_meta import GnssMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GnssMeta from a JSON string
gnss_meta_instance = GnssMeta.from_json(json)
# print the JSON string representation of the object
print(GnssMeta.to_json())

# convert the object into a dict
gnss_meta_dict = gnss_meta_instance.to_dict()
# create an instance of GnssMeta from a dict
gnss_meta_from_dict = GnssMeta.from_dict(gnss_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


