# CellResponseWithFulfillment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | WGS 84 geodetic grid line, north to south. | 
**lon** | **float** | WGS 84 geodetic grid line, east to west. | 
**uncertainty** | **int** | Radius of the uncertainty circle around the location in meters. Also known as Horizontal Positioning Error (HPE). | 
**fulfilled_with** | [**CellServiceType**](CellServiceType.md) |  | 

## Example

```python
from nrf_cloud_client.models.cell_response_with_fulfillment import CellResponseWithFulfillment

# TODO update the JSON string below
json = "{}"
# create an instance of CellResponseWithFulfillment from a JSON string
cell_response_with_fulfillment_instance = CellResponseWithFulfillment.from_json(json)
# print the JSON string representation of the object
print(CellResponseWithFulfillment.to_json())

# convert the object into a dict
cell_response_with_fulfillment_dict = cell_response_with_fulfillment_instance.to_dict()
# create an instance of CellResponseWithFulfillment from a dict
cell_response_with_fulfillment_from_dict = CellResponseWithFulfillment.from_dict(cell_response_with_fulfillment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


