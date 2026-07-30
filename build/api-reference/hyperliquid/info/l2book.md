# l2Book

#### Parameters

| Name | Type   | Required | Description                                                |
| ---- | ------ | -------- | ---------------------------------------------------------- |
| type | String | Yes      | `"l2Book"`                                                 |
| coin | String | Yes      | Asset name (e.g., `"BTC"` for perpetuals, `"@0"` for spot) |

#### Returns

**Object** - Contains `coin`, `time`, `levels` (array of `[px, sz, n]` ask/bid arrays).

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"l2Book"}'

// Result
Failed to deserialize the JSON body into the target type
```
{% endcode %}
