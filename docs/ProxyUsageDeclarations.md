# ProxyUsageDeclarations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agps** | **float** |  | [optional] 
**pgps** | **float** |  | [optional] 
**ground_fix** | **float** |  | [optional] 
**reverse_geo** | **float** |  | [optional] 

## Example

```python
from nrf_cloud_client.models.proxy_usage_declarations import ProxyUsageDeclarations

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyUsageDeclarations from a JSON string
proxy_usage_declarations_instance = ProxyUsageDeclarations.from_json(json)
# print the JSON string representation of the object
print(ProxyUsageDeclarations.to_json())

# convert the object into a dict
proxy_usage_declarations_dict = proxy_usage_declarations_instance.to_dict()
# create an instance of ProxyUsageDeclarations from a dict
proxy_usage_declarations_from_dict = ProxyUsageDeclarations.from_dict(proxy_usage_declarations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


