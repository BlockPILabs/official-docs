# meta

#### Parameters

| Name | Type   | Required | Description |
| ---- | ------ | -------- | ----------- |
| type | String | Yes      | `"meta"`    |

#### Returns

**Object** - Contains `universe` (array of asset configs with `name`, `szDecimals`, `maxLeverage`, `marginTableId`).

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"meta"}'

// Result
{"universe":[{"szDecimals":5,"name":"BTC","maxLeverage":40,"marginTableId":56},{"szDecimals":4,"name":"ETH","maxLeverage":25,"marginTableId":55},{"szDecimals":2,"name":"ATOM","maxLeverage":5,"marginTableId":5},{"szDecimals":1,"name":"MATIC","maxLeverage":20,"marginTableId":20,"isDelisted":true},{"szDecimals":1,"name":"DYDX","maxLeverage":5,"marginTableId":5},{"szDecimals":2,"name":"SOL","maxLeverage":20,"marginTableId":54},{"szDecimals":2,"name":"AVAX","maxLeverage":10,"marginTableId":52},{"szDecimals":3,"name":"BNB","maxLeverage":10,"marginTableId":51},{"szDecimals":1,"name":"APE","maxLeverage":5,"marginTableId":5},{"szDecimals":1,"name":"OP","maxLeverage":5,"marginTableId":5},{"szDecimals":2,"name":"LTC","maxLeverage":10,"marginTableId":52},{"szDecimals":1,"name":"ARB","maxLeverage":10,"marginTableId":51},{"szDecimals":0,"name":"DOGE","maxLeverage":10,"marginTableId":52},{"szDecimals":1,"name":"INJ","maxLeverage":5,"marginTableId":5},{"szDecimals":1,"name":"SUI","maxLeverage":10,"mar
  ...
```
{% endcode %}
