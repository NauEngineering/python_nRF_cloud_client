# AnchorMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_address** | **str** | String comprised of 6 hexadecimal pairs, separated by colons or dashes. When used in a positioning request, it must be universally assigned. See &lt;a href&#x3D;\&quot;https://docs.nordicsemi.com/bundle/nrf-cloud/page/LocationServices/Guides/LocationTroubleshooting.html#my-wi-fi-request-returns-the-error-mac-address-mac-is-a-local-mac-address\&quot; target&#x3D;\&quot;_blank\&quot;&gt;this help page&lt;/a&gt; for details. | 
**name** | **str** | Limit 32 characters. Only numbers, letters, underscores, dashes, and spaces allowed. All other characters will be removed. | [optional] 

## Example

```python
from nrf_cloud_client.models.anchor_meta import AnchorMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AnchorMeta from a JSON string
anchor_meta_instance = AnchorMeta.from_json(json)
# print the JSON string representation of the object
print(AnchorMeta.to_json())

# convert the object into a dict
anchor_meta_dict = anchor_meta_instance.to_dict()
# create an instance of AnchorMeta from a dict
anchor_meta_from_dict = AnchorMeta.from_dict(anchor_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


