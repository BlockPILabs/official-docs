# userFunding

#### Parameters

type: userFunding user: address (42-char hex) startTime: timestamp (ms) endTime: timestamp (ms)

#### Returns

Funding payments for the user's positions with coin, fundingRate, premium, time.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"userFunding"}'

// Result
[]
```
{% endcode %}
