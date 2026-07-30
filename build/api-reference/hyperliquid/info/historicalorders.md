# historicalOrders

#### Parameters

type: historicalOrders user: address (42-char hex)

#### Returns

Historical order data with pagination. Each order includes status, fill info, and timestamps.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"historicalOrders"}'

// Result
[]
```
{% endcode %}
