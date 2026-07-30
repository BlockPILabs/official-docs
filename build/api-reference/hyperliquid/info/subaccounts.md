# subAccounts

#### Parameters

type: subAccounts user: address (42-char hex)

#### Returns

List of subaccount objects with addresses and metadata.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"subAccounts","user":"0x563d3f4e57a4982f8cec0d3eaf47c5e6dbbaf337"}'

// Result
null
```
{% endcode %}
