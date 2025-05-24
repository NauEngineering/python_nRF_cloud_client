# nrf_cloud_client.AccountApi

All URIs are relative to *https://api.nrfcloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_account_info**](AccountApi.md#fetch_account_info) | **GET** /account | FetchAccountInfo
[**fetch_api_usage_summary**](AccountApi.md#fetch_api_usage_summary) | **GET** /account/usage/summary | FetchApiUsageSummary
[**generate_service_evaluation_token**](AccountApi.md#generate_service_evaluation_token) | **POST** /account/service-evaluation-token | GenerateServiceEvaluationToken
[**generate_service_key_and_token**](AccountApi.md#generate_service_key_and_token) | **POST** /account/service-key-and-token | GenerateServiceKeyAndToken
[**get_service_evaluation_token**](AccountApi.md#get_service_evaluation_token) | **GET** /account/service-evaluation-token | GetServiceEvaluationToken
[**get_service_token**](AccountApi.md#get_service_token) | **GET** /account/service-token | GetServiceToken
[**list_api_usage**](AccountApi.md#list_api_usage) | **GET** /account/usage | ListApiUsage
[**list_invoices**](AccountApi.md#list_invoices) | **GET** /account/invoices | ListInvoices
[**list_tags**](AccountApi.md#list_tags) | **GET** /account/tags | ListTags


# **fetch_account_info**
> AccountInfoArgs fetch_account_info()

FetchAccountInfo

Fetch information about your team (also known as tenant), your team's current plan, and your user role and permissions for that team. Only team owners are allowed to view current month costs.
The API key you use as the Bearer token in this request is specific to one team. You have one API key for each team of which you are a member.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.account_info_args import AccountInfoArgs
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
    api_instance = nrf_cloud_client.AccountApi(api_client)

    try:
        # FetchAccountInfo
        api_response = api_instance.fetch_account_info()
        print("The response of AccountApi->fetch_account_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->fetch_account_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountInfoArgs**](AccountInfoArgs.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains account information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_api_usage_summary**
> ApiUsageMetricsSummary fetch_api_usage_summary()

FetchApiUsageSummary

Fetch a summary of your usage of nRF Cloud commercial services for the current and previous month.

In the response, `currentDevices` is the current number for each main type of device in your account. It is thus a snapshot metric, and can fluctuate. The other metrics are cumulative for the month, and reset on the first of each month.

```sh
curl -G $API_HOST/v1/account/usage/summary -H "Authorization: Bearer $API_KEY" -H "Content-Type: application/json"
```

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.api_usage_metrics_summary import ApiUsageMetricsSummary
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
    api_instance = nrf_cloud_client.AccountApi(api_client)

    try:
        # FetchApiUsageSummary
        api_response = api_instance.fetch_api_usage_summary()
        print("The response of AccountApi->fetch_api_usage_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->fetch_api_usage_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiUsageMetricsSummary**](ApiUsageMetricsSummary.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains a summary of current API usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_service_evaluation_token**
> ServiceKeyTokenResponse generate_service_evaluation_token()

GenerateServiceEvaluationToken

Generates a JSON Web Token (JWT) for evaluating nRF Cloud Location Services by proxy servers. You may use this token to authenticate proxy server requests to any of the Location Service endpoints that indicate `Service Evaluation Token` among their Authorizations.

Calling this endpoint for the first time will start your 30-day evaluation period,
after which you will need to contact [Nordic Sales](https://www.nordicsemi.com/About-us/Contact-Us) if you want to extend your evaluation period, or enter into a business agreement for commercial cloud-to-cloud use.

The JWT claims are set automatically by nRF Cloud when this token is generated. Although it can be regenerated upon request, the initial 30-day trial period remains unchanged.

For more information see
[JWT authentication for nRF Cloud](https://docs.nordicsemi.com/bundle/nrf-cloud/page/Devices/Security/JWT.html).

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.service_key_token_response import ServiceKeyTokenResponse
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
    api_instance = nrf_cloud_client.AccountApi(api_client)

    try:
        # GenerateServiceEvaluationToken
        api_response = api_instance.generate_service_evaluation_token()
        print("The response of AccountApi->generate_service_evaluation_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->generate_service_evaluation_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceKeyTokenResponse**](ServiceKeyTokenResponse.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains newly generated Service Evaluation Token for evaluation purposes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_service_key_and_token**
> GenerateServiceKeyAndToken200Response generate_service_key_and_token()

GenerateServiceKeyAndToken

Creates a new service key pair for authenticating REST endpoints that support JWTs. The public key is stored in nRF Cloud for use in JWT verification. The response contains the private key and a JWT signed by it, with a one year expiry. The private key can be used to generate additional JWTs with an expiry of your choice.

<div style="background-color: #fff3cd; color: #856404; text-align: center; border: 1px solid #ffeeba; border-radius: .25rem; padding: .75rem 1.25rem">Calling this endpoint will overwrite an existing service key, causing any JWTs signed by the previous key to fail verification!</div>

<div style="background-color: #fff3cd; color: #856404; text-align: center; border: 1px solid #ffeeba; border-radius: .25rem; padding: .75rem 1.25rem; margin-top: 10px;">You will not be allowed to use this service key unless you have declared proxy usage declarations for the service you intend to use.</div>

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.generate_service_key_and_token200_response import GenerateServiceKeyAndToken200Response
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
    api_instance = nrf_cloud_client.AccountApi(api_client)

    try:
        # GenerateServiceKeyAndToken
        api_response = api_instance.generate_service_key_and_token()
        print("The response of AccountApi->generate_service_key_and_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->generate_service_key_and_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GenerateServiceKeyAndToken200Response**](GenerateServiceKeyAndToken200Response.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a token (JWT) and the private key that signed it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_evaluation_token**
> ServiceKeyTokenResponse get_service_evaluation_token()

GetServiceEvaluationToken

Returns an existing Service Evaluation Token. Calling this endpoint will not start your evaluation period.
You may create one by calling the [GenerateServiceEvaluationToken](#operation/GenerateServiceEvaluationToken) endpoint.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.service_key_token_response import ServiceKeyTokenResponse
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
    api_instance = nrf_cloud_client.AccountApi(api_client)

    try:
        # GetServiceEvaluationToken
        api_response = api_instance.get_service_evaluation_token()
        print("The response of AccountApi->get_service_evaluation_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_service_evaluation_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceKeyTokenResponse**](ServiceKeyTokenResponse.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains Service Evaluation Token for evaluation purposes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_token**
> GetServiceToken200Response get_service_token()

GetServiceToken

Gets the service token. The returned token is usable for all services.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.get_service_token200_response import GetServiceToken200Response
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
    api_instance = nrf_cloud_client.AccountApi(api_client)

    try:
        # GetServiceToken
        api_response = api_instance.get_service_token()
        print("The response of AccountApi->get_service_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_service_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetServiceToken200Response**](GetServiceToken200Response.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a service token (JWT). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_usage**
> PaginatedResultOmitApiUsageMetricRecordTenantId list_api_usage(inclusive_start, exclusive_end, page_sort=page_sort, page_limit=page_limit, page_next_token=page_next_token)

ListApiUsage

Retrieve a list of your daily or monthly usage of nRF Cloud commercial services for a specified date range. For daily usage metrics,
pass a date range in YYYY-MM-DD format. Otherwise, use the YYYY-MM format to receive monthly usage metrics.

The format of `inclusiveStart` and `exclusiveEnd` must match. Both must be YYYY-MM or YYYY-MM-DD format.

The list will not contain any records for 0 usage. In other words, a daily (or monthly) record is only returned if usage occurred on that day (or during that month).

As of June 2022 we do not keep a record of the number of devices in your account at the end of each day. Therefore, the response will only
contain usage records for Location Services, Firmware-over-the-air (FOTA) job executions, and stored device messages. This may change
in the future.

The following example illustrates how to retrieve a list of daily metrics. If you prefer monthly metrics, you would change this example to use `inclusiveStart=2022-01&exclusiveEnd=2022-03`.
```sh
curl -G $API_HOST/v1/account/usage -d "inclusiveStart=2022-01-01&exclusiveEnd=2022-03-01" -H "Authorization: Bearer $API_KEY" -H "Content-Type: application/json"
```
By default records are sorted by date in ascending order. Set `pageSort=desc` to sort in descending order.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.page_sort import PageSort
from nrf_cloud_client.models.paginated_result_omit_api_usage_metric_record_tenant_id import PaginatedResultOmitApiUsageMetricRecordTenantId
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
    api_instance = nrf_cloud_client.AccountApi(api_client)
    inclusive_start = nrf_cloud_client.UsageMetricDate() # UsageMetricDate | 
    exclusive_end = nrf_cloud_client.UsageMetricDate() # UsageMetricDate | 
    page_sort = desc # PageSort |  (optional) (default to desc)
    page_limit = 56 # int |  (optional)
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # ListApiUsage
        api_response = api_instance.list_api_usage(inclusive_start, exclusive_end, page_sort=page_sort, page_limit=page_limit, page_next_token=page_next_token)
        print("The response of AccountApi->list_api_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->list_api_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inclusive_start** | [**UsageMetricDate**](.md)|  | 
 **exclusive_end** | [**UsageMetricDate**](.md)|  | 
 **page_sort** | [**PageSort**](.md)|  | [optional] [default to desc]
 **page_limit** | **int**|  | [optional] 
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultOmitApiUsageMetricRecordTenantId**](PaginatedResultOmitApiUsageMetricRecordTenantId.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains a detailed list of API usage data for a specified date range |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> PaginatedResultInvoiceResponse list_invoices(page_limit=page_limit, page_next_token=page_next_token)

ListInvoices

List invoices for your team (also known as tenant). Only team owners and admins are allowed to view invoices.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.paginated_result_invoice_response import PaginatedResultInvoiceResponse
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
    api_instance = nrf_cloud_client.AccountApi(api_client)
    page_limit = 56 # int |  (optional)
    page_next_token = 'page_next_token_example' # str |  (optional)

    try:
        # ListInvoices
        api_response = api_instance.list_invoices(page_limit=page_limit, page_next_token=page_next_token)
        print("The response of AccountApi->list_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->list_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_limit** | **int**|  | [optional] 
 **page_next_token** | **str**|  | [optional] 

### Return type

[**PaginatedResultInvoiceResponse**](PaginatedResultInvoiceResponse.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> PaginatedResultDeviceTag list_tags()

ListTags

List all team tags for your account.

### Example

* Bearer Authentication (Simple Token):

```python
import nrf_cloud_client
from nrf_cloud_client.models.paginated_result_device_tag import PaginatedResultDeviceTag
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
    api_instance = nrf_cloud_client.AccountApi(api_client)

    try:
        # ListTags
        api_response = api_instance.list_tags()
        print("The response of AccountApi->list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->list_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaginatedResultDeviceTag**](PaginatedResultDeviceTag.md)

### Authorization

[Simple Token](../README.md#Simple Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

