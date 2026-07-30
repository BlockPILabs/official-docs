# fundingHistory

#### Parameters

type: fundingHistory coin: string startTime: timestamp (ms) endTime: timestamp (ms)

#### Returns

Historical funding rates with coin, fundingRate, premium, time.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"fundingHistory","coin":"BTC","startTime":1719700000000,"endTime":1719703600000}'

// Result
[{"coin":"BTC","fundingRate":"0.0000125","premium":"-0.0000707337","time":1719702000121}]
```
{% endcode %}
