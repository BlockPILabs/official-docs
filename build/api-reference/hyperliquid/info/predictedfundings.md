# predictedFundings

#### Parameters

type: predictedFundings

#### Returns

Predicted funding rates for upcoming funding rounds.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"predictedFundings"}'

// Result
[["0G",[["BinPerp",{"fundingRate":"0.00005","nextFundingTime":1785412800000,"fundingIntervalHours":4}],["HlPerp",{"fundingRate":"-0.0000561913","nextFundingTime":1785402000000,"fundingIntervalHours":1}],["BybitPerp",{"fundingRate":"0.00005","nextFundingTime":1785412800000,"fundingIntervalHours":4}]]],["2Z",[["BinPerp",{"fundingRate":"0.00005","nextFundingTime":1785412800000,"fundingIntervalHours":4}],["HlPerp",{"fundingRate":"-0.000032848","nextFundingTime":1785402000000,"fundingIntervalHours":1}],["BybitPerp",{"fundingRate":"0.00005","nextFundingTime":1785412800000,"fundingIntervalHours":4}]]],["AAVE",[["BinPerp",{"fundingRate":"0.00002164","nextFundingTime":1785427200000,"fundingIntervalHours":8}],["HlPerp",{"fundingRate":"0.0000125","nextFundingTime":1785402000000,"fundingIntervalHours":1}],["BybitPerp",{"fundingRate":"0.00006656","nextFundingTime":1785427200000,"fundingIntervalHours":8}]]],["ACE",[["BinPerp",{"fundingRate":"-0.00024825","nextFundingTime":1785412800000,"fundingIntervalHours":4}],["HlPerp",{"fundingRate":"-0.0000494361","nextFundingTime":1785402000000,"fundingIntervalHours":1}],["BybitPerp",{"fundingRate":"-0.00009463","nextFundingTime":1785412800000,"fundingIntervalHours":4}]]],["ADA",[["BinPerp",{"fundingRate":"0.00008966","nextFundingTime":1785427200000,"fundingIntervalHours":8}],["HlPerp",{"fundingRate":"0.0000125","nextFundingTime":1785402000000,"fundingIntervalHours":1}],["BybitPerp",{"fundingRate":"0.0001","nextFundingTime":1785427200000,"fundingInte
  ...
```
{% endcode %}
