# LocationServiceUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | **float** |  | 
**devices_using** | **float** |  | 

## Example

```python
from nrf_cloud_client.models.location_service_usage import LocationServiceUsage

# TODO update the JSON string below
json = "{}"
# create an instance of LocationServiceUsage from a JSON string
location_service_usage_instance = LocationServiceUsage.from_json(json)
# print the JSON string representation of the object
print(LocationServiceUsage.to_json())

# convert the object into a dict
location_service_usage_dict = location_service_usage_instance.to_dict()
# create an instance of LocationServiceUsage from a dict
location_service_usage_from_dict = LocationServiceUsage.from_dict(location_service_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


