# userRateLimit

#### Parameters

type: userRateLimit user: address (42-char hex)

#### Returns

Rate limit status including remaining requests and reset time.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"userRateLimit","user":"0x563d3f4e57a4982f8cec0d3eaf47c5e6dbbaf337"}'

// Result
{"cumVlm":"0.0","nRequestsUsed":0,"nRequestsCap":10000,"nRequestsSurplus":0}
```
{% endcode %}
