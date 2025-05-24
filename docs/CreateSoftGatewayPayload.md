# CreateSoftGatewayPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cognito_identity_id** | **str** |  | 
**soft_gateway_type** | [**SoftGatewayType**](SoftGatewayType.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.create_soft_gateway_payload import CreateSoftGatewayPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSoftGatewayPayload from a JSON string
create_soft_gateway_payload_instance = CreateSoftGatewayPayload.from_json(json)
# print the JSON string representation of the object
print(CreateSoftGatewayPayload.to_json())

# convert the object into a dict
create_soft_gateway_payload_dict = create_soft_gateway_payload_instance.to_dict()
# create an instance of CreateSoftGatewayPayload from a dict
create_soft_gateway_payload_from_dict = CreateSoftGatewayPayload.from_dict(create_soft_gateway_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


