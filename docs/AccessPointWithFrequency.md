# AccessPointWithFrequency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_address** | **str** | String comprised of 6 hexadecimal pairs, separated by colons or dashes. When used in a positioning request, it must be universally assigned. See &lt;a href&#x3D;\&quot;https://docs.nordicsemi.com/bundle/nrf-cloud/page/LocationServices/Guides/LocationTroubleshooting.html#my-wi-fi-request-returns-the-error-mac-address-mac-is-a-local-mac-address\&quot; target&#x3D;\&quot;_blank\&quot;&gt;this help page&lt;/a&gt; for details. | 
**ssid** | **str** |  | [optional] 
**signal_strength** | **float** | Signal strength in dBm, between -128 and 0 | [optional] 
**age** | **float** | The number of milliseconds since this access point was detected. | [optional] 
**signal_to_noise_ratio** | **float** | The current signal to noise ratio measured in dB. | [optional] 
**frequency** | **float** | Channel frequency in MHz | [optional] 

## Example

```python
from nrf_cloud_client.models.access_point_with_frequency import AccessPointWithFrequency

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPointWithFrequency from a JSON string
access_point_with_frequency_instance = AccessPointWithFrequency.from_json(json)
# print the JSON string representation of the object
print(AccessPointWithFrequency.to_json())

# convert the object into a dict
access_point_with_frequency_dict = access_point_with_frequency_instance.to_dict()
# create an instance of AccessPointWithFrequency from a dict
access_point_with_frequency_from_dict = AccessPointWithFrequency.from_dict(access_point_with_frequency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


