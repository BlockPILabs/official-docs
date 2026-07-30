# delegations

#### Parameters

type: delegations user: address (42-char hex)

#### Returns

Current active staking delegations with validator and amount.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"delegations"}'

// Result
[]
```
{% endcode %}
