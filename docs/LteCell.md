# LteCell

LTE cell information. Use the 'nmr' property to send neighbor cell measurements for increased accuracy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsrp** | **float** | Reference Signal Received Power. Measured in dBm. See &lt;a href&#x3D;\&quot;https://www.rfwireless-world.com/Terminology/LTE-RSRP-vs-RSRQ.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;this page&lt;/a&gt; for more details. Range -157..-44 | [optional] 
**rsrq** | **float** | Reference Signal Received Quality. Measured in dB. See &lt;a href&#x3D;\&quot;https://www.rfwireless-world.com/Terminology/LTE-RSRP-vs-RSRQ.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;this page&lt;/a&gt; for more details. Range -34.5..3.5 | [optional] 
**mcc** | **int** | Mobile Country Code. As defined in &lt;a href&#x3D;\&quot;https://www.itu.int/dms_pub/itu-t/opb/sp/T-SP-E.212B-2018-PDF-E.pdf\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ITU-T E.212&lt;/a&gt;. | 
**mnc** | [**Mnc**](Mnc.md) |  | 
**eci** | **int** | E-UTRA Cell Identifier (ECI), 28 bits (20 bits eNodeB and 8 bits Cell ID). Calculated using \&quot;(eNodeB-ID * 256) + Sector-ID\&quot;. Range 0 .. 268435455. See &lt;a href&#x3D;\&quot;https://www.etsi.org/deliver/etsi_ts/123000_123099/123003/17.09.00_60/ts_123003v170900p.pdf\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ETSI TS 123 003, section 19.6&lt;/a&gt; for more details. | 
**tac** | **int** | Tracking Area Code (TAC). Identifies a group of LTE cells in a certain region (Tracking Area). See &lt;a href&#x3D;\&quot;https://www.etsi.org/deliver/etsi_ts/123000_123099/123003/17.09.00_60/ts_123003v170900p.pdf\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ETSI TS 123 003, section 19.4.2.3&lt;/a&gt; for more details. | 
**pci** | **int** | Physical Cell Identity (PCI). Used in the physical layer of E-UTRA systems to identify a cell. Range: 0..503 | [optional] 
**earfcn** | **int** | Evolved Absolute Radio Frequency Channel (E-ARFCN). Range: 0..262143. See &lt;a href&#x3D;\&quot;https://www.etsi.org/deliver/etsi_ts/136100_136199/136106/17.00.00_60/ts_136106v170000p.pdf\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ETSI TS 136 106, section 5.7.3&lt;/a&gt; for more details. | [optional] 
**adv** | **float** | The length of time a signal takes to reach the base station from a mobile phone (half of rtt&#x3D;round trip time). The units are symbols (Ts) as specified in 3GPP TS 36.211 (LTE). The expected resolution for nRF Cloud API is 1 Ts. Range 0..20512. | [optional] 
**nmr** | [**List[LteNeighborMeasurement]**](LteNeighborMeasurement.md) |  | [optional] 

## Example

```python
from nrf_cloud_client.models.lte_cell import LteCell

# TODO update the JSON string below
json = "{}"
# create an instance of LteCell from a JSON string
lte_cell_instance = LteCell.from_json(json)
# print the JSON string representation of the object
print(LteCell.to_json())

# convert the object into a dict
lte_cell_dict = lte_cell_instance.to_dict()
# create an instance of LteCell from a dict
lte_cell_from_dict = LteCell.from_dict(lte_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


