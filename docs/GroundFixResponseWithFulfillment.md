# GroundFixResponseWithFulfillment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | WGS 84 geodetic grid line, north to south. | 
**lon** | **float** | WGS 84 geodetic grid line, east to west. | 
**uncertainty** | **int** | Radius of the uncertainty circle around the location in meters. Also known as Horizontal Positioning Error (HPE). | 
**anchors** | [**List[AnchorMeta]**](AnchorMeta.md) |  | [optional] 
**fulfilled_with** | [**GroundFixResponseWithFulfillmentFulfilledWith**](GroundFixResponseWithFulfillmentFulfilledWith.md) |  | 
**alt** | [**AlternateLocation**](AlternateLocation.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.ground_fix_response_with_fulfillment import GroundFixResponseWithFulfillment

# TODO update the JSON string below
json = "{}"
# create an instance of GroundFixResponseWithFulfillment from a JSON string
ground_fix_response_with_fulfillment_instance = GroundFixResponseWithFulfillment.from_json(json)
# print the JSON string representation of the object
print(GroundFixResponseWithFulfillment.to_json())

# convert the object into a dict
ground_fix_response_with_fulfillment_dict = ground_fix_response_with_fulfillment_instance.to_dict()
# create an instance of GroundFixResponseWithFulfillment from a dict
ground_fix_response_with_fulfillment_from_dict = GroundFixResponseWithFulfillment.from_dict(ground_fix_response_with_fulfillment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


