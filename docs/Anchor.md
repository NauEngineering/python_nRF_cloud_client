# Anchor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_address** | **str** | String comprised of 6 hexadecimal pairs, separated by colons or dashes. When used in a positioning request, it must be universally assigned. See &lt;a href&#x3D;\&quot;https://docs.nordicsemi.com/bundle/nrf-cloud/page/LocationServices/Guides/LocationTroubleshooting.html#my-wi-fi-request-returns-the-error-mac-address-mac-is-a-local-mac-address\&quot; target&#x3D;\&quot;_blank\&quot;&gt;this help page&lt;/a&gt; for details. | 
**lat** | **float** | WGS 84 geodetic grid line, north to south. | 
**lon** | **float** | WGS 84 geodetic grid line, east to west. | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | [optional] 
**name** | **str** | Limit 32 characters. Only numbers, letters, underscores, dashes, and spaces allowed. All other characters will be removed. | [optional] 

## Example

```python
from nrf_cloud_client.models.anchor import Anchor

# TODO update the JSON string below
json = "{}"
# create an instance of Anchor from a JSON string
anchor_instance = Anchor.from_json(json)
# print the JSON string representation of the object
print(Anchor.to_json())

# convert the object into a dict
anchor_dict = anchor_instance.to_dict()
# create an instance of Anchor from a dict
anchor_from_dict = Anchor.from_dict(anchor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


