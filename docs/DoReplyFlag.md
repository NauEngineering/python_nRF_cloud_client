# DoReplyFlag

Controls the response body. If boolean false or number 0, response body will be empty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from nrf_cloud_client.models.do_reply_flag import DoReplyFlag

# TODO update the JSON string below
json = "{}"
# create an instance of DoReplyFlag from a JSON string
do_reply_flag_instance = DoReplyFlag.from_json(json)
# print the JSON string representation of the object
print(DoReplyFlag.to_json())

# convert the object into a dict
do_reply_flag_dict = do_reply_flag_instance.to_dict()
# create an instance of DoReplyFlag from a dict
do_reply_flag_from_dict = DoReplyFlag.from_dict(do_reply_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


