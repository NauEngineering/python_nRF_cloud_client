# PaginatedResultDeviceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeviceMessage]**](DeviceMessage.md) |  | 
**total** | **int** | Reflects the total results returned by the query, which may be less than the total number of items available. If the response contains a &#x60;pageNextToken&#x60; value, you can supply the &#x60;pageNextToken&#x60; in the next request to get more results. The maximum value of &#x60;total&#x60; is the page limit of the request, or ten pages if no page limit is provided. | [optional] 
**page_next_token** | **str** | Token used to retrieve the next page of items in the list. Present in a response only if the total available results exceeds the specified limit on a page. This token does not change between requests. When supplying as a request parameter, use URL-encoding. | [optional] 

## Example

```python
from nrf_cloud_client.models.paginated_result_device_message import PaginatedResultDeviceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultDeviceMessage from a JSON string
paginated_result_device_message_instance = PaginatedResultDeviceMessage.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultDeviceMessage.to_json())

# convert the object into a dict
paginated_result_device_message_dict = paginated_result_device_message_instance.to_dict()
# create an instance of PaginatedResultDeviceMessage from a dict
paginated_result_device_message_from_dict = PaginatedResultDeviceMessage.from_dict(paginated_result_device_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


