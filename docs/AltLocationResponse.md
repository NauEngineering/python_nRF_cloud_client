# AltLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | WGS 84 geodetic grid line, north to south. | 
**lon** | **float** | WGS 84 geodetic grid line, east to west. | 
**uncertainty** | **int** | Radius of the uncertainty circle around the location in meters. Also known as Horizontal Positioning Error (HPE). | 
**fulfilled_with** | [**GroundFixServiceType**](GroundFixServiceType.md) |  | 

## Example

```python
from nrf_cloud_client.models.alt_location_response import AltLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AltLocationResponse from a JSON string
alt_location_response_instance = AltLocationResponse.from_json(json)
# print the JSON string representation of the object
print(AltLocationResponse.to_json())

# convert the object into a dict
alt_location_response_dict = alt_location_response_instance.to_dict()
# create an instance of AltLocationResponse from a dict
alt_location_response_from_dict = AltLocationResponse.from_dict(alt_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


