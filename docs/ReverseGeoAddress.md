# ReverseGeoAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country | 
**state** | **str** | State, province, or region. | 
**country_code** | **str** | Country Code - 2 letter (ISO 3166-1 alpha-2) | [optional] 
**county** | **str** | Geographic region in a country | [optional] 
**postal_code** | **str** | Postcode, PIN, zip code | [optional] 
**state_code** | **str** | State or province code | [optional] 
**city** | **str** | City, town, municipality, borough, hamlet | [optional] 
**suburb** | **str** | Geographic region used for residential and commercial purposes | [optional] 
**street** | **str** | Road, pathway, motorway, highway | [optional] 
**street_number** | **str** | House or building number | [optional] 

## Example

```python
from nrf_cloud_client.models.reverse_geo_address import ReverseGeoAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseGeoAddress from a JSON string
reverse_geo_address_instance = ReverseGeoAddress.from_json(json)
# print the JSON string representation of the object
print(ReverseGeoAddress.to_json())

# convert the object into a dict
reverse_geo_address_dict = reverse_geo_address_instance.to_dict()
# create an instance of ReverseGeoAddress from a dict
reverse_geo_address_from_dict = ReverseGeoAddress.from_dict(reverse_geo_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


