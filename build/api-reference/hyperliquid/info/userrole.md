# userRole

#### Parameters

type: userRole user: address (42-char hex)

#### Returns

Role identifier: "missing", "user", "agent", "vault", or "subAccount".

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"userRole","user":"0x563d3f4e57a4982f8cec0d3eaf47c5e6dbbaf337"}'

// Result
{"role":"missing"}
```
{% endcode %}
