# GenerateServiceKeyAndToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The private key of the service key pair. | 
**token** | **str** | JWT signed by the private key of the service key pair. | 

## Example

```python
from nrf_cloud_client.models.generate_service_key_and_token200_response import GenerateServiceKeyAndToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateServiceKeyAndToken200Response from a JSON string
generate_service_key_and_token200_response_instance = GenerateServiceKeyAndToken200Response.from_json(json)
# print the JSON string representation of the object
print(GenerateServiceKeyAndToken200Response.to_json())

# convert the object into a dict
generate_service_key_and_token200_response_dict = generate_service_key_and_token200_response_instance.to_dict()
# create an instance of GenerateServiceKeyAndToken200Response from a dict
generate_service_key_and_token200_response_from_dict = GenerateServiceKeyAndToken200Response.from_dict(generate_service_key_and_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


