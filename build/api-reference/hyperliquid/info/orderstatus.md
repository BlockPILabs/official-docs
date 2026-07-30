# orderStatus

#### Parameters

type: orderStatus user: address (42-char hex) oid: number (or cloid: string)

#### Returns

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"orderStatus","user":"0x563d3f4e57a4982f8cec0d3eaf47c5e6dbbaf337","oid":91490942}'

// Result
{"status":"unknownOid"}
```
{% endcode %}
