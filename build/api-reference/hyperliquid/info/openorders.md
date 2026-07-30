# openOrders

#### Parameters

| Name | Type   | Required | Description                        |
| ---- | ------ | -------- | ---------------------------------- |
| type | String | Yes      | `"openOrders"`                     |
| user | String | Yes      | Address in 42-character hex format |

#### Returns

**Array** - List of open order objects with `coin`, `limitPx`, `oid`, `side`, `sz`, `timestamp`.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"openOrders"}'

// Result
Failed to deserialize the JSON body into the target type
```
{% endcode %}
