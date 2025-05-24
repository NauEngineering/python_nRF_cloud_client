# GetServiceToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | The date when the service key pair was created in ISO format. | 
**token** | **str** | JWT signed by the private key of the service key pair. | 

## Example

```python
from nrf_cloud_client.models.get_service_token200_response import GetServiceToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceToken200Response from a JSON string
get_service_token200_response_instance = GetServiceToken200Response.from_json(json)
# print the JSON string representation of the object
print(GetServiceToken200Response.to_json())

# convert the object into a dict
get_service_token200_response_dict = get_service_token200_response_instance.to_dict()
# create an instance of GetServiceToken200Response from a dict
get_service_token200_response_from_dict = GetServiceToken200Response.from_dict(get_service_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


