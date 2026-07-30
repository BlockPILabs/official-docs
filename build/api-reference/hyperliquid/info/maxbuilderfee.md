# maxBuilderFee

#### Parameters

type: maxBuilderFee user: address (42-char hex) builder: address (42-char hex)

#### Returns

Maximum builder fee configuration and approval status.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"maxBuilderFee","user":"0x563d3f4e57a4982f8cec0d3eaf47c5e6dbbaf337","builder":"0x0000000000000000000000000000000000000000"}'

// Result
0
```
{% endcode %}
