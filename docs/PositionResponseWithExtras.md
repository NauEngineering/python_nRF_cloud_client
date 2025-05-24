# PositionResponseWithExtras


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | WGS 84 geodetic grid line, north to south. | 
**lon** | **float** | WGS 84 geodetic grid line, east to west. | 
**uncertainty** | **int** | Radius of the uncertainty circle around the location in meters. Also known as Horizontal Positioning Error (HPE). | 
**anchors** | [**List[AnchorMeta]**](AnchorMeta.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.position_response_with_extras import PositionResponseWithExtras

# TODO update the JSON string below
json = "{}"
# create an instance of PositionResponseWithExtras from a JSON string
position_response_with_extras_instance = PositionResponseWithExtras.from_json(json)
# print the JSON string representation of the object
print(PositionResponseWithExtras.to_json())

# convert the object into a dict
position_response_with_extras_dict = position_response_with_extras_instance.to_dict()
# create an instance of PositionResponseWithExtras from a dict
position_response_with_extras_from_dict = PositionResponseWithExtras.from_dict(position_response_with_extras_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


