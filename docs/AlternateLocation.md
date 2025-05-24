# AlternateLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**AltLocationResponse**](AltLocationResponse.md) |  | 
**dist** | **float** | Distance in meters between the alternate location and the main location. | 

## Example

```python
from nrf_cloud_client.models.alternate_location import AlternateLocation

# TODO update the JSON string below
json = "{}"
# create an instance of AlternateLocation from a JSON string
alternate_location_instance = AlternateLocation.from_json(json)
# print the JSON string representation of the object
print(AlternateLocation.to_json())

# convert the object into a dict
alternate_location_dict = alternate_location_instance.to_dict()
# create an instance of AlternateLocation from a dict
alternate_location_from_dict = AlternateLocation.from_dict(alternate_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


