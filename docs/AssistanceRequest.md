# AssistanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[NrfMessageType]**](NrfMessageType.md) | Type of assistance data (see description above). Defaults to [1, 2, 3, 4, 6, 7, 9] | [optional] 
**mcc** | **int** | Mobile Country Code. As defined in &lt;a href&#x3D;\&quot;https://www.itu.int/dms_pub/itu-t/opb/sp/T-SP-E.212B-2018-PDF-E.pdf\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ITU-T E.212&lt;/a&gt;. | [optional] 
**mnc** | [**Mnc**](Mnc.md) |  | [optional] 
**tac** | **int** | Tracking Area Code (TAC). Identifies a group of LTE cells in a certain region (Tracking Area). See &lt;a href&#x3D;\&quot;https://www.etsi.org/deliver/etsi_ts/123000_123099/123003/17.09.00_60/ts_123003v170900p.pdf\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ETSI TS 123 003, section 19.4.2.3&lt;/a&gt; for more details. | [optional] 
**eci** | **int** | E-UTRA Cell Identifier (ECI), 28 bits (20 bits eNodeB and 8 bits Cell ID). Calculated using \&quot;(eNodeB-ID * 256) + Sector-ID\&quot;. Range 0 .. 268435455. See &lt;a href&#x3D;\&quot;https://www.etsi.org/deliver/etsi_ts/123000_123099/123003/17.09.00_60/ts_123003v170900p.pdf\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ETSI TS 123 003, section 19.6&lt;/a&gt; for more details. | [optional] 
**rsrp** | **float** | Reference Signal Received Power. Measured in dBm. See &lt;a href&#x3D;\&quot;https://www.rfwireless-world.com/Terminology/LTE-RSRP-vs-RSRQ.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;this page&lt;/a&gt; for more details. Range -157..-44 | [optional] 
**filtered** | **bool** | Send this flag if you want to receive ephemeris for only satellites in view. nRF Cloud will return ephemeris for up to 16 satellites. Cell data (eci, mcc, mnc, tac) is required. Defaults to false. | [optional] 
**mask** | **float** | Filtered ephemeris mask angle. Only works in conjunction with the filtered flag. Controls the mask angle for which the satellites are filtered. Range 0..90 Defaults to 5 | [optional] 

## Example

```python
from nrf_cloud_client.models.assistance_request import AssistanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssistanceRequest from a JSON string
assistance_request_instance = AssistanceRequest.from_json(json)
# print the JSON string representation of the object
print(AssistanceRequest.to_json())

# convert the object into a dict
assistance_request_dict = assistance_request_instance.to_dict()
# create an instance of AssistanceRequest from a dict
assistance_request_from_dict = AssistanceRequest.from_dict(assistance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


