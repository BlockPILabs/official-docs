# delegatorRewards

#### Parameters

type: delegatorRewards user: address (42-char hex)

#### Returns

Accumulated staking rewards for the delegator.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"delegatorRewards"}'

// Result
[]
```
{% endcode %}
