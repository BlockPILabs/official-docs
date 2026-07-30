# spotClearinghouseState

#### Parameters

type: spotClearinghouseState user: address (42-char hex)

#### Returns

Spot clearinghouse state including balances and positions.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"spotClearinghouseState","user":"0x563d3f4e57a4982f8cec0d3eaf47c5e6dbbaf337"}'

// Result
{"balances":[]}
```
{% endcode %}
