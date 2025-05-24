# DeviceCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | This is the canonical device id used in the device certificate, and as the MQTT client id. | 
**ca_cert** | **str** | The AmazonRootCA1.pem used for establishing TLS communications with AWS IoT. | 
**client_cert** | **str** | The x.509 certificate. If this is for an \&quot;mqtt team device\&quot; this string contains only one certificate. JITP device certificates, which are generated using an intermediate CA cert, contain a bundled certificate consisting of the device certificate and the intermediate CA pem. | 
**private_key** | **str** | The private key associated with the device certificate. | [optional] 

## Example

```python
from nrf_cloud_client.models.device_certificate import DeviceCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCertificate from a JSON string
device_certificate_instance = DeviceCertificate.from_json(json)
# print the JSON string representation of the object
print(DeviceCertificate.to_json())

# convert the object into a dict
device_certificate_dict = device_certificate_instance.to_dict()
# create an instance of DeviceCertificate from a dict
device_certificate_from_dict = DeviceCertificate.from_dict(device_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


