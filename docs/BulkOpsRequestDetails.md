# BulkOpsRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_ops_request_id** | **str** | Universally Unique Lexicographically Sortable Identifier (using Crockford&#39;s alphabet). | 
**endpoint** | [**BulkOpsRequestEndpoint**](BulkOpsRequestEndpoint.md) |  | 
**status** | [**BulkOpsRequestStatus**](BulkOpsRequestStatus.md) |  | 
**requested_at** | **datetime** | HTML-encoded ISO-8601 date-time string denoting the start or end of a date range. If the string includes only a date, the time is the beginning of the day (00:00:00). | 
**completed_at** | **datetime** | HTML-encoded ISO-8601 date-time string denoting the start or end of a date range. If the string includes only a date, the time is the beginning of the day (00:00:00). | [optional] 
**uploaded_data_url** | **str** | The URL at which you can retrieve the data you originally uploaded to an endpoint that supports bulk operations. | 
**result_data_url** | **str** | The URL at which you can retrieve the result, if available, for the data you originally uploaded to an endpoint that supports bulk operations. | [optional] 
**error_summary_url** | **str** | The URL at which you can retrieve a summary of errors and the row indices they occurred at for a failed bulk ops request job. | [optional] 

## Example

```python
from nrf_cloud_client.models.bulk_ops_request_details import BulkOpsRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOpsRequestDetails from a JSON string
bulk_ops_request_details_instance = BulkOpsRequestDetails.from_json(json)
# print the JSON string representation of the object
print(BulkOpsRequestDetails.to_json())

# convert the object into a dict
bulk_ops_request_details_dict = bulk_ops_request_details_instance.to_dict()
# create an instance of BulkOpsRequestDetails from a dict
bulk_ops_request_details_from_dict = BulkOpsRequestDetails.from_dict(bulk_ops_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


