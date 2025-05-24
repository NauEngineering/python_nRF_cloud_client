# AccessPointWithFrequencyObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_address** | **str** | String comprised of 6 hexadecimal pairs, separated by colons or dashes. When used in a positioning request, it must be universally assigned. See &lt;a href&#x3D;\&quot;https://docs.nordicsemi.com/bundle/nrf-cloud/page/LocationServices/Guides/LocationTroubleshooting.html#my-wi-fi-request-returns-the-error-mac-address-mac-is-a-local-mac-address\&quot; target&#x3D;\&quot;_blank\&quot;&gt;this help page&lt;/a&gt; for details. | 
**ssid** | **str** |  | [optional] 
**signal_strength** | **float** | Signal strength in dBm, between -128 and 0 | [optional] 
**age** | **float** | The number of milliseconds since this access point was detected. | [optional] 
**signal_to_noise_ratio** | **float** | The current signal to noise ratio measured in dB. | [optional] 
**frequency** | **float** | Channel frequency in MHz | [optional] 
**observed_at** | **str** | ISO 8601 format. Example 2021-03-07T21:02:51.907Z | 

## Example

```python
from nrf_cloud_client.models.access_point_with_frequency_observation import AccessPointWithFrequencyObservation

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPointWithFrequencyObservation from a JSON string
access_point_with_frequency_observation_instance = AccessPointWithFrequencyObservation.from_json(json)
# print the JSON string representation of the object
print(AccessPointWithFrequencyObservation.to_json())

# convert the object into a dict
access_point_with_frequency_observation_dict = access_point_with_frequency_observation_instance.to_dict()
# create an instance of AccessPointWithFrequencyObservation from a dict
access_point_with_frequency_observation_from_dict = AccessPointWithFrequencyObservation.from_dict(access_point_with_frequency_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


