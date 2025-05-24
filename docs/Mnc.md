# Mnc

Mobile Network Code. A number or string: 120 | 1 | \"001\" | \"01\" | \"000\". As defined in <a href=\"https://www.itu.int/dms_pub/itu-t/opb/sp/T-SP-E.212B-2018-PDF-E.pdf\" target=\"_blank\">ITU-T E.212</a>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from nrf_cloud_client.models.mnc import Mnc

# TODO update the JSON string below
json = "{}"
# create an instance of Mnc from a JSON string
mnc_instance = Mnc.from_json(json)
# print the JSON string representation of the object
print(Mnc.to_json())

# convert the object into a dict
mnc_dict = mnc_instance.to_dict()
# create an instance of Mnc from a dict
mnc_from_dict = Mnc.from_dict(mnc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


