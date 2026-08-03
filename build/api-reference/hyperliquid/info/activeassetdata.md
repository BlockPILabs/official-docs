# activeAssetData

#### Parameters

type: activeAssetData user: address coin: string

| Name | Type   | Required | Description                        |
| ---- | ------ | -------- | ---------------------------------- |
| type | String | Yes      | "activeAssetData"                  |
| user | String | Yes      | Address in 42-character hex format |
| coin | String | Yes      | Asset name (e.g., "BTC", "ETH")    |

#### Returns

**Object** - Active position data for the user on the specified asset.

| Field            | Type   | Description                        |
| ---------------- | ------ | ---------------------------------- |
| user             | String | User address                       |
| coin             | String | Asset name                         |
| leverage         | Object | \`{type: "cross"                   |
| maxTradeSzs      | Array  | Maximum trade sizes \[short, long] |
| availableToTrade | Array  | Available to trade \[short, long]  |
| markPx           | String | Current mark price                 |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"activeAssetData","user":"0x82c32b1410173eb115864adc95bcc58dec7afccc","coin":"BTC"}'

// Result
{
  "user": "0x82c32b1410173eb115864adc95bcc58dec7afccc",
  "coin": "BTC",
  "leverage": {
    "type": "cross",
    "value": 20
  },
  "maxTradeSzs": [
    "0.0",
    "0.00517"
  ],
  "availableToTrade": [
    "0.0",
    "16.182177"
  ],
  "markPx": "62600.3"
}
```
{% endcode %}
