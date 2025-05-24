# nrf_cloud_client.IPDevicesApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_device**](IPDevicesApi.md#associate_device) | **PUT** /association/{deviceId} | AssociateDevice
[**create_device_certificate**](IPDevicesApi.md#create_device_certificate) | **POST** /devices/{deviceId}/certificates | CreateDeviceCertificate
[**dissociate_device**](IPDevicesApi.md#dissociate_device) | **DELETE** /association/{deviceId} | DissociateDevice
[**onboard_device**](IPDevicesApi.md#onboard_device) | **POST** /devices/{deviceId} | OnboardDevice
[**onboard_devices**](IPDevicesApi.md#onboard_devices) | **POST** /devices | OnboardDevices
[**register_certificates**](IPDevicesApi.md#register_certificates) | **POST** /devices/certificates | RegisterCertificates
[**register_public_keys**](IPDevicesApi.md#register_public_keys) | **POST** /devices/public-keys | RegisterPublicKeys
[**update_device_state**](IPDevicesApi.md#update_device_state) | **PATCH** /devices/{deviceId}/state | UpdateDeviceState


# **associate_device**
> associate_device(device_id, body, sub_type=sub_type)

AssociateDevice

Add a device to your nRF Cloud account. The association process is idempotent. You may therefore use this endpoint to update your device's `subType`. For more on the use of `subType` see the [OnboardDevices endpoint](#operation/OnboardDevices).
```sh
curl -X PUT $API_HOST/v1/association/$DEVICE_ID -d "$DEVICE_OWNERSHIP_CODE" -H "Authorization: Bearer $API_KEY" -H "Content-Type: text/plain"
```

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.IPDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str | 
    sub_type = 'sub_type_example' # str |  (optional)

    try:
        # AssociateDevice
        api_instance.associate_device(device_id, body, sub_type=sub_type)
    except Exception as e:
        print("Exception when calling IPDevicesApi->associate_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **body** | **str**|  | 
 **sub_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_certificate**
> DeviceCertificate create_device_certificate(device_id, body)

CreateDeviceCertificate

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">This endpoint has been deprecated. Please use the <a href="#tag/IP-Devices/operation/OnboardDevice">OnboardDevice endpoint</a> instead.</div>
Creates a just-in-time-provisioning (JITP) certificate for a device using Nordic's registered CA certificate.
Consider this a convenience endpoint for obtaining a device certificate, with the following disadvantages:

1. The JITP process takes approximately 30 seconds and involves multiple connects and disconnects between your MQTT client and the AWS IoT broker.
2. You cannot use your own CA certificate.
3. This endpoint does not support bulk operations.
4. You will have to explicitly [associate](/v1#operation/AssociateDevice) a JITP device with your account.


For this JITP certificate to work properly the device must not yet be provisioned (created) on our platform. If you are creating a certificate for a device that you have already connected to our platform, please delete the device using the `DeleteDevice` [endpoint](#operation/DeleteDevice) before using this certificate.

For a Nordic Semiconductor product such as an nRF9160-DK or a Thingy-91, the `deviceId` is `nrf-[IMEI]`, e.g., `nrf-111222333444555`. The IMEI can be found on your product's label.

If you want to create a certificate for a non-Nordic device, any `deviceId` is sufficient that does not start with `nrf-` (we recommend using a GUID).
```sh
curl -X POST $API_HOST/v1/devices/$DEVICE_ID/certificates -d "$DEVICE_OWNERSHIP_CODE" -H "Authorization: Bearer $API_KEY" -H "Content-Type: text/plain"
```

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.device_certificate import DeviceCertificate
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.IPDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str | 

    try:
        # CreateDeviceCertificate
        api_response = api_instance.create_device_certificate(device_id, body)
        print("The response of IPDevicesApi->create_device_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPDevicesApi->create_device_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **body** | **str**|  | 

### Return type

[**DeviceCertificate**](DeviceCertificate.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissociate_device**
> dissociate_device(device_id)

DissociateDevice

<div style="background-color: #f8d7da; color: #721c24; text-align: center; border: 1px solid #f5c6cb; border-radius: .25rem; padding: .75rem 1.25rem">This endpoint has been deprecated. Please use the <a href="#operation/DeleteDevice">DeleteDevice endpoint</a> instead.</div>

Remove a device from your nRF Cloud account. This does not delete (unprovision) it on nRF Cloud.
```sh
curl -X DELETE $API_HOST/v1/association/$DEVICE_ID -H "Authorization: Bearer $API_KEY"
```

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.IPDevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # DissociateDevice
        api_instance.dissociate_device(device_id)
    except Exception as e:
        print("Exception when calling IPDevicesApi->dissociate_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onboard_device**
> onboard_device(device_id, onboard_single_device_args)

OnboardDevice

[Onboard](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Associations/Onboarding.html) and associate a single device with your nRF Cloud account.

This endpoint supports two onboarding modalities depending upon whether you include device certificates or public keys in your payload.

Uploading a device certificate allows the device to use nRF Cloud services using any supported connectivity protocol, such as HTTP/REST, MQTT, and CoAP. This is the recommended method for onboarding devices.
Unlike the [CreateDeviceCertificate endpoint](#operation/CreateDeviceCertificate), this endpoint involves your own CA certificate and
requires you to upload device certificates that you have already obtained, whether via a CSR produced by the `AT%KEYGEN` command
(modem firmware v1.3+), or offline via your own script. We impose no rules on your CA certificate, and a self-signed certificate may be used.
For more information see [Onboarding](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Associations/Onboarding.html) in the nRF Cloud documentation.

Whether using our APIs via REST or MQTT you will need to flash to your device:
1. <a href="https://www.amazontrust.com/repository/AmazonRootCA1.pem" target="_blank">The Amazon Root CA1 PEM file</a>, which enables the device to authenticate the AWS IoT server.
2. The private key associated with the device certificate.

Additionally, if the device will be using MQTT, you will also need to flash the device certificate. For [signing JWTs](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Security/JWT.html) you will use the private key associated
with the certificate. (During the device onboarding process we extract the corresponding public key from your uploaded certificate and use this for JWT signature verification.)

The second onboarding modality involves uploading a public key to verify the signatures of [JSON Web Tokens (JWTs)](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Security/JWT.html) sent by the device.
Uploading a public key allows the device to use  [JSON Web Tokens (JWTs)](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Security/JWT.html) signed by the private key of an asymmetric key pair, i.e., a private key that is different than the one used to sign the device's CSR (this key pair can be generated via the AT%KEYGEN command).
If you are using JWTs signed by the device CSR key, and you have also uploaded the device's certificate via this or the [OnboardDevices endpoint](#operation/OnboardDevices), there is no need to upload the public key, because it is automatically extracted from the certificate.
This is useful for devices that only want to consume nRF Cloud services over REST.

Please note:
Public keys must be [ES256](https://ldapwiki.com/wiki/Wiki.jsp?page=ES256). For more information, see the [nRF Cloud REST Authentication documentation](https://docs.nordicsemi.com/bundle/nrf-cloud/page/APIs/REST/RESTOverview.html#authentication).

For bulk onboarding of devices, please use the [OnboardDevices endpoint](#operation/OnboardDevices).

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.onboard_single_device_args import OnboardSingleDeviceArgs
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.IPDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    onboard_single_device_args = nrf_cloud_client.OnboardSingleDeviceArgs() # OnboardSingleDeviceArgs | 

    try:
        # OnboardDevice
        api_instance.onboard_device(device_id, onboard_single_device_args)
    except Exception as e:
        print("Exception when calling IPDevicesApi->onboard_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **onboard_single_device_args** | [**OnboardSingleDeviceArgs**](OnboardSingleDeviceArgs.md)|  | 

### Return type

void (empty response body)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onboard_devices**
> OnboardDevices202Response onboard_devices(content_type, body)

OnboardDevices

[Onboard](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Associations/Onboarding.html) and associate one or more devices with your nRF Cloud account by posting CSV data.

This endpoint supports two onboarding modalities depending upon whether you include device certificates or public keys in your CSV Payload.

Uploading a device certificate allows the device to use nRF Cloud services using any supported connectivity protocol, such as HTTP/REST, MQTT, and CoAP. This is the recommended method for onboarding devices.
Unlike the [CreateDeviceCertificate endpoint](#operation/CreateDeviceCertificate), this endpoint involves your own CA certificate and
requires you to upload device certificates that you have already obtained, whether via a CSR produced by the `AT%KEYGEN` command
(modem firmware v1.3+), or offline via your own script. We impose no rules on your CA certificate, and a self-signed certificate may be used.
For more information see [Onboarding](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Associations/Onboarding.html) in the nRF Cloud documentation.

Whether using our APIs via REST or MQTT you will need to flash to your device:
1. <a href="https://www.amazontrust.com/repository/AmazonRootCA1.pem" target="_blank">The Amazon Root CA1 PEM file</a>, which enables the device to authenticate the AWS IoT server.
2. The private key associated with the device certificate.

Additionally, if the device will be using MQTT, you will also need to flash the device certificate. For [signing JWTs](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Security/JWT.html) you will use the private key associated
with the certificate. (During the device onboarding process we extract the corresponding public key from your uploaded certificate and use this for JWT signature verification.)

The second onboarding modality involves uploading a public key to verify the signatures of [JSON Web Tokens (JWTs)](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Security/JWT.html) sent by the device.
Uploading a public key allows the device to use  [JSON Web Tokens (JWTs)](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Security/JWT.html) signed by the private key of an asymmetric key pair, i.e., a private key that is different than the one used to sign the device's CSR (this key pair can be generated via the AT%KEYGEN command).
If you are using JWTs signed by the device CSR key, and you have also uploaded the device's certificate via this or the [OnboardDevices endpoint](#operation/OnboardDevices), there is no need to upload the public key, because it is automatically extracted from the certificate.
This is useful for devices that only want to consume nRF Cloud services over REST.

Please note:
Public keys must be [ES256](https://ldapwiki.com/wiki/Wiki.jsp?page=ES256). For more information, see the [nRF Cloud REST Authentication documentation](https://docs.nordicsemi.com/bundle/nrf-cloud/page/APIs/REST/RESTOverview.html#authentication).

This endpoint supports [asynchronous bulk operations](#tag/Bulk-Ops-Requests). Your data will be validated, and if valid, you
will receive an HTTP 202 response with a `bulkOpsRequestId`. You can use this id with the bulk ops endpoints
to track the request's processing status. If the bulk ops request indicates FAILED status, check the JSON errors file (URL in the bulk
ops request details), fix the offending rows, then re-submit the CSV with only those rows.

Each CSV row must in the format `deviceId,[subType],[tags],[fwTypes],"certPem"`, where:

|Field|Required?|Description|Validation Pattern|
|---|:---:|---|---|
|`deviceId`<div style="width:90px"></div>|Yes|A globally unique device id (UUIDs are highly recommended)|`/^[a-z0-9:_-]{1,128}$/i`|
|`subType`|No|A custom [device type](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Properties/Types.html) (for example `humidity-sensor`) to help you better recognize or categorize your devices. Include "gateway" in your subType if you want to provision it as a `Gateway`. This will give the device additional MQTT permissions for gateway-related topics. Otherwise, it is onboarded as a `Generic` device.|`/[a-zA-Z0-9_.,@\/:#-]{0,799}/`|
|`tags`|No|A list of pipe-delimited tags to create groups of devices (e.g., `warehouse\|sensor\|east`)|Each tag:<br/>`/^[a-zA-Z0-9_.@:#-]+$/`|
|`fwTypes`|No|A list of pipe-delimited firmware types that each device supports for FOTA (e.g., `APP\|MODEM`)|Each type:<br/>`/^(APP\|MODEM\|BOOT\|SOFTDEVICE\|BOOTLOADER\|MDM_FULL)$/`|
|`certPem`|Yes|Dependending on the onboarding modality, either a unique [ES256](https://ldapwiki.com/wiki/Wiki.jsp?page=ES256) X.509 certificate OR public key in PEM format, wrapped in double quotes (to allow for line breaks in CSV)|`/^-{5}BEGIN CERTIFICATE-{5}(\r\n\|\r\|\n)([^-]+)(\r\n\|\r\|\n)-{5}END CERTIFICATE-{5}(\r\n\|\r\|\n)$/` OR `/^-{5}BEGIN PUBLIC KEY-{5}(\r\n\|\r\|\n)([^-]+)(\r\n\|\r\|\n)-{5}END PUBLIC KEY-{5}(\r\n\|\r\|\n)$/`|

Examples of CSV rows:
   #### All values set
<span style="font-family:Courier">f69c0e45-7f04-4949-8def-bb2215b4223e,my-thing-type,tag1|tag2,APP|MODEM,"-----BEGIN CERTIFICATE-----<br/>MIIB7DCCAZMCFD...Av3CVgjzn5BLS03X7lyf4w==<br/>
-----END CERTIFICATE-----<br/>"</span>
   #### `subType` not set
<span style="font-family:Courier">f69c0e45-7f04-4949-8def-bb2215b4223e,,tag1|tag2,APP|MODEM,"-----BEGIN CERTIFICATE-----<br/>MIIB7DCCAZMCFD...Av3CVgjzn5BLS03X7lyf4w==<br/>
-----END CERTIFICATE-----<br/>"</span>
   #### `subType` and `tags` not set, but supported `fwTypes` are set
<span style="font-family:Courier">f69c0e45-7f04-4949-8def-bb2215b4223e,,,APP|MODEM,"-----BEGIN CERTIFICATE-----<br/>MIIB7DCCAZMCFD...Av3CVgjzn5BLS03X7lyf4w==<br/>
-----END CERTIFICATE-----<br/>"</span>
 #### Using the public key modality
   * <span style="font-family:Courier">f69c0e45-7f04-4949-8def-bb2215b4223e,,,APP|MODEM,""-----BEGIN PUBLIC KEY-----<br/>MIIB7DCCAZMCFD...Av3CVgjzn5BLS03X7lyf4w==<br/>
-----END PUBLIC KEY-----<br/>"</span>

Also note:
   * Max number of rows is 1000.
   * Do not use a header.
   * Do not leave any blank lines.

Example of uploading CSV data as a binary file:

```sh
curl -X POST $API_HOST/v1/devices \
--data-binary @$PATH_TO_CSV_FILE \
-H "Content-Type: application/octet-stream" \
-H "Authorization: Bearer $API_KEY"
```
Note that for some unknown reason, curl will strip the final line break in each ES256 cert when sending the CSV file using a non-binary content-type, e.g., using syntax such as `-d @$PATH_TO_CSV_FILE -H "Content-Type: text/csv"`. Therefore, with curl use `--data-binary` only. If you want to send the CSV as text, use a REST client like Postman or Insomnia.
To synchronously provision a single device, you can also use the [OnboardDevice endpoint](#operation/OnboardDevice).

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.onboard_devices202_response import OnboardDevices202Response
from nrf_cloud_client.models.rest_api_payload_content_type_with_csv import RestApiPayloadContentTypeWithCsv
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.IPDevicesApi(api_client)
    content_type = nrf_cloud_client.RestApiPayloadContentTypeWithCsv() # RestApiPayloadContentTypeWithCsv | 
    body = 'body_example' # str | 

    try:
        # OnboardDevices
        api_response = api_instance.onboard_devices(content_type, body)
        print("The response of IPDevicesApi->onboard_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPDevicesApi->onboard_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | [**RestApiPayloadContentTypeWithCsv**](.md)|  | 
 **body** | **str**|  | 

### Return type

[**OnboardDevices202Response**](OnboardDevices202Response.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_certificates**
> OnboardDevices202Response register_certificates(content_type, body)

RegisterCertificates

Register one or more device certificates. If a device has already been added to your team (onboarded) this will delete its existing cert and replace it with the new one.
It is recommended to update existing devices with their new certificates before registering them here.
If it is not onboarded, please use the [OnboardDevice endpoint](#operation/OnboardDevice) to complete the process which allows your device(s) to use nRF Cloud.

This endpoint supports [asynchronous bulk operations](#tag/Bulk-Ops-Requests). Your data will be validated, and if valid, you
will receive an HTTP 202 response with a `bulkOpsRequestId`. You can use this id with the bulk ops endpoints
to track the request's processing status. If the bulk ops request indicates FAILED status, check the JSON errors file (URL in the bulk
ops request details), fix the offending rows, then re-submit the CSV with only those rows.

Each CSV row must in the format `deviceId,"certPem"`, where:

|Field|Required|Description|Validation Pattern|
|---|:---:|---|---|
|`deviceId`<div style="width:90px"></div>|Yes|A globally unique device id (UUIDs are highly recommended)|`/^[a-z0-9:_-]{1,128}$/i`|
|`certPem`|Yes|A unique [ES256](https://ldapwiki.com/wiki/Wiki.jsp?page=ES256) X.509 certificate in PEM format, wrapped in double quotes (to allow for line breaks in CSV)|`/^-{5}BEGIN CERTIFICATE-{5}(\r\n\|\r\|\n)([^-]+)(\r\n\|\r\|\n)-{5}END CERTIFICATE-{5}(\r\n\|\r\|\n)$/`|

Example of a CSV row:
   #### All values set
<span style="font-family:Courier">f69c0e45-7f04-4949-8def-bb2215b4223e,"-----BEGIN CERTIFICATE-----<br/>MIIB7DCCAZMCFD...Av3CVgjzn5BLS03X7lyf4w==<br/>
-----END CERTIFICATE-----<br/>"</span>

Also note:
   * Max number of rows is 1000.
   * Do not use a header.
   * Do not leave any blank lines.

Example of uploading CSV data as a binary file:

```sh
curl -X POST $API_HOST/v1/devices/certificates \
--data-binary @$PATH_TO_CSV_FILE \
-H "Content-Type: application/octet-stream" \
-H "Authorization: Bearer $API_KEY"
```
Note that for some unknown reason, curl will strip the final line break in each ES256 public key when sending the CSV file using a non-binary content-type, e.g., using syntax such as `-d @$PATH_TO_CSV_FILE -H "Content-Type: text/csv"`. Therefore, with curl use `--data-binary` only. If you want to send the CSV as text, use a REST client like Postman or Insomnia.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.onboard_devices202_response import OnboardDevices202Response
from nrf_cloud_client.models.rest_api_payload_content_type_with_csv import RestApiPayloadContentTypeWithCsv
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.IPDevicesApi(api_client)
    content_type = nrf_cloud_client.RestApiPayloadContentTypeWithCsv() # RestApiPayloadContentTypeWithCsv | 
    body = 'body_example' # str | 

    try:
        # RegisterCertificates
        api_response = api_instance.register_certificates(content_type, body)
        print("The response of IPDevicesApi->register_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPDevicesApi->register_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | [**RestApiPayloadContentTypeWithCsv**](.md)|  | 
 **body** | **str**|  | 

### Return type

[**OnboardDevices202Response**](OnboardDevices202Response.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_public_keys**
> OnboardDevices202Response register_public_keys(content_type, body)

RegisterPublicKeys

Register one or more public keys so that the signatures for [JSON Web Tokens (JWTs)](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Security/JWT.html) sent by the device can be verified.

This endpoint supports two main use cases:
1. Devices that <strong>are not onboarded</strong> on nRF Cloud that also want to consume Location Service endpoints over REST. This requires [JWT authentication](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Security/JWT.html). Please note:
<ol type="a">
<li>Unlike Location Services, REST-based consumption of Firmware Over-the-Air Update endpoints requires cloud-onboarding. We recommend using the <a href="/v1#operation/OnboardDevices">OnboardDevices endpoint</a>.
<li>You are still able to cloud-provision devices for which you have registered public keys. There is no conflict there.
<li>Devices that are not onboarded on nRF Cloud cannot use MQTT.
</ol>
2. Devices that <strong>are [onboarded](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Associations/Onboarding.html)</strong> on nRF Cloud that want to use a dedicated private key for signing JWTs instead of using the key associated
with its cloud-onboarding certificate (e.g., they were onboarded with the [OnboardDevices endpoint](#operation/OnboardDevices),
which automatically extracts and stores a public key during the onboarding process for use in subsequent JWT signature verifications).

Only one public key may be registered for each device. Uploading CSV data with a different key for the same device will overwrite the existing key.

Public keys must be [ES256](https://ldapwiki.com/wiki/Wiki.jsp?page=ES256). For more information, see the [nRF Cloud REST Authentication documentation](https://docs.nordicsemi.com/bundle/nrf-cloud/page/APIs/REST/RESTOverview.html#authentication).

This endpoint supports [asynchronous bulk operations](#tag/Bulk-Ops-Requests). Your data will be validated, and if valid, you
will receive an HTTP 202 response with a `bulkOpsRequestId`. You can use this id with the bulk ops endpoints
to track the request's processing status. If the bulk ops request indicates FAILED status, check the JSON errors file (URL in the bulk
ops request details), fix the offending rows, then re-submit the CSV with only those rows.

Each CSV row must in the format `deviceId,"keyPem"`, where:

|Field|Required|Description|Validation Pattern|
|---|:---:|---|---|
|`deviceId`<div style="width:90px"></div>|Yes|A globally unique device id (UUIDs are highly recommended)|`/^[a-z0-9:_-]{1,128}$/i`|
|`keyPem`|Yes|A unique [ES256](https://ldapwiki.com/wiki/Wiki.jsp?page=ES256) public key in PEM format, wrapped in double quotes (to allow for line breaks in CSV)|`/^-{5}BEGIN PUBLIC KEY-{5}(\r\n\|\r\|\n)([^-]+)(\r\n\|\r\|\n)-{5}END PUBLIC KEY-{5}(\r\n\|\r\|\n)$/`|

Example of a CSV row:
   #### All values set
<span style="font-family:Courier">f69c0e45-7f04-4949-8def-bb2215b4223e,"-----BEGIN PUBLIC KEY-----<br/>MIIB7DCCAZMCFD...Av3CVgjzn5BLS03X7lyf4w==<br/>
-----END PUBLIC KEY-----<br/>"</span>

Also note:
   * Max number of rows is 1000.
   * Do not use a header.
   * Do not leave any blank lines.

Example of uploading CSV data as a binary file:

```sh
curl -X POST $API_HOST/v1/devices/public-keys \
--data-binary @$PATH_TO_CSV_FILE \
-H "Content-Type: application/octet-stream" \
-H "Authorization: Bearer $API_KEY"
```
Note that for some unknown reason, curl will strip the final line break in each ES256 public key when sending the CSV file using a non-binary content-type, e.g., using syntax such as `-d @$PATH_TO_CSV_FILE -H "Content-Type: text/csv"`. Therefore, with curl use `--data-binary` only. If you want to send the CSV as text, use a REST client like Postman or Insomnia.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.onboard_devices202_response import OnboardDevices202Response
from nrf_cloud_client.models.rest_api_payload_content_type_with_csv import RestApiPayloadContentTypeWithCsv
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.IPDevicesApi(api_client)
    content_type = nrf_cloud_client.RestApiPayloadContentTypeWithCsv() # RestApiPayloadContentTypeWithCsv | 
    body = 'body_example' # str | 

    try:
        # RegisterPublicKeys
        api_response = api_instance.register_public_keys(content_type, body)
        print("The response of IPDevicesApi->register_public_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPDevicesApi->register_public_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | [**RestApiPayloadContentTypeWithCsv**](.md)|  | 
 **body** | **str**|  | 

### Return type

[**OnboardDevices202Response**](OnboardDevices202Response.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_state**
> update_device_state(device_id, device_state_input)

UpdateDeviceState

Modify the device's state as stored in its shadow. You do not have to pass the entire shadow. You can update a specific portion by setting the correct JSON field path:
```sh
export DEVICE_VERSION=$(curl $API_HOST/v1/devices/$DEVICE_ID -H "Authorization: Bearer $API_KEY" | jq -r '.["$meta"].version')
curl -X PATCH $API_HOST/v1/devices/$DEVICE_ID/state -d '{ "reported": { "device": { "serviceInfo": { "fota_v1": ["BOOT"] } } } }' -H "Authorization: Bearer $API_KEY" -H "Content-Type: application/json" -H "If-Match: $DEVICE_VERSION"
```

### Example

* Bearer Authentication (Simple Token):
* Bearer Authentication (JSON Web Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.device_state_input import DeviceStateInput
from nrf_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nrfcloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nrf_cloud_client.Configuration(
    host = "https://api.nrfcloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Simple Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure Bearer authorization: JSON Web Token
configuration = nrf_cloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nrf_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nrf_cloud_client.IPDevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    device_state_input = nrf_cloud_client.DeviceStateInput() # DeviceStateInput | 

    try:
        # UpdateDeviceState
        api_instance.update_device_state(device_id, device_state_input)
    except Exception as e:
        print("Exception when calling IPDevicesApi->update_device_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **device_state_input** | [**DeviceStateInput**](DeviceStateInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[Simple Token](../README.md#Simple Token), [JSON Web Token](../README.md#JSON Web Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

