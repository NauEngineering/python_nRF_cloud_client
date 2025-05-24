# ServiceKeyTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires** | **datetime** | Expiration date for the provided Service Evaluation Token | 
**token** | **str** | JWT signed by the private key of the service key pair. | 

## Example

```python
from nrf_cloud_client.models.service_key_token_response import ServiceKeyTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceKeyTokenResponse from a JSON string
service_key_token_response_instance = ServiceKeyTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceKeyTokenResponse.to_json())

# convert the object into a dict
service_key_token_response_dict = service_key_token_response_instance.to_dict()
# create an instance of ServiceKeyTokenResponse from a dict
service_key_token_response_from_dict = ServiceKeyTokenResponse.from_dict(service_key_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


