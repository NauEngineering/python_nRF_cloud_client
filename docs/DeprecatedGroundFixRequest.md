# DeprecatedGroundFixRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lte** | [**List[LteCell]**](LteCell.md) |  | [optional] 
**wifi** | [**WifiAccessPointsRequest**](WifiAccessPointsRequest.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.deprecated_ground_fix_request import DeprecatedGroundFixRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedGroundFixRequest from a JSON string
deprecated_ground_fix_request_instance = DeprecatedGroundFixRequest.from_json(json)
# print the JSON string representation of the object
print(DeprecatedGroundFixRequest.to_json())

# convert the object into a dict
deprecated_ground_fix_request_dict = deprecated_ground_fix_request_instance.to_dict()
# create an instance of DeprecatedGroundFixRequest from a dict
deprecated_ground_fix_request_from_dict = DeprecatedGroundFixRequest.from_dict(deprecated_ground_fix_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


