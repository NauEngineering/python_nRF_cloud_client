# OnboardDevices202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_ops_request_id** | **str** | Universally Unique Lexicographically Sortable Identifier (using Crockford&#39;s alphabet). | 

## Example

```python
from nrf_cloud_client.models.onboard_devices202_response import OnboardDevices202Response

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardDevices202Response from a JSON string
onboard_devices202_response_instance = OnboardDevices202Response.from_json(json)
# print the JSON string representation of the object
print(OnboardDevices202Response.to_json())

# convert the object into a dict
onboard_devices202_response_dict = onboard_devices202_response_instance.to_dict()
# create an instance of OnboardDevices202Response from a dict
onboard_devices202_response_from_dict = OnboardDevices202Response.from_dict(onboard_devices202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


