# ReverseGeoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | WGS 84 geodetic grid line, north to south. | 
**lon** | **float** | WGS 84 geodetic grid line, east to west. | 
**uncertainty** | **int** | Radius of the uncertainty circle around the location in meters. Also known as Horizontal Positioning Error (HPE). | 
**formatted** | **str** | Description of the address, created from values in the &#39;address&#39; property | 
**address** | [**ReverseGeoAddress**](ReverseGeoAddress.md) |  | 

## Example

```python
from nrf_cloud_client.models.reverse_geo_response import ReverseGeoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseGeoResponse from a JSON string
reverse_geo_response_instance = ReverseGeoResponse.from_json(json)
# print the JSON string representation of the object
print(ReverseGeoResponse.to_json())

# convert the object into a dict
reverse_geo_response_dict = reverse_geo_response_instance.to_dict()
# create an instance of ReverseGeoResponse from a dict
reverse_geo_response_from_dict = ReverseGeoResponse.from_dict(reverse_geo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


