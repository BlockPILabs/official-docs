# isVip

#### Parameters

type: isVip user: address (42-char hex)

#### Returns

Boolean - whether the user has VIP status.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"isVip","user":"0x563d3f4e57a4982f8cec0d3eaf47c5e6dbbaf337"}'

// Result
false
```
{% endcode %}
