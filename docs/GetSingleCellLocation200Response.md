# GetSingleCellLocation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | WGS 84 geodetic grid line, north to south. | 
**lon** | **float** | WGS 84 geodetic grid line, east to west. | 
**uncertainty** | **int** | Radius of the uncertainty circle around the location in meters. Also known as Horizontal Positioning Error (HPE). | 

## Example

```python
from nrf_cloud_client.models.get_single_cell_location200_response import GetSingleCellLocation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSingleCellLocation200Response from a JSON string
get_single_cell_location200_response_instance = GetSingleCellLocation200Response.from_json(json)
# print the JSON string representation of the object
print(GetSingleCellLocation200Response.to_json())

# convert the object into a dict
get_single_cell_location200_response_dict = get_single_cell_location200_response_instance.to_dict()
# create an instance of GetSingleCellLocation200Response from a dict
get_single_cell_location200_response_from_dict = GetSingleCellLocation200Response.from_dict(get_single_cell_location200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


