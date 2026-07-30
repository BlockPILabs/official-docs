# delegatorHistory

#### Parameters

type: delegatorHistory user: address (42-char hex)

#### Returns

History of staking delegation changes.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"delegatorHistory"}'

// Result
[]
```
{% endcode %}
