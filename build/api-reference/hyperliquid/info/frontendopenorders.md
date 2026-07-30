# frontendOpenOrders

#### Parameters

type: frontendOpenOrders user: address (42-char hex)

#### Returns

Open orders with additional metadata (orderType, reduceOnly, triggerCondition, origSz).

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"frontendOpenOrders"}'

// Result
[]
```
{% endcode %}
