# userFills

#### Parameters

| Name            | Type    | Required | Description                        |
| --------------- | ------- | -------- | ---------------------------------- |
| type            | String  | Yes      | `"userFills"`                      |
| user            | String  | Yes      | Address in 42-character hex format |
| aggregateByTime | Boolean | No       | When true, combines partial fills  |

#### Returns

**Array** - Up to 2000 most recent fills with `coin`, `px`, `sz`, `side`, `time`, `dir`, `closedPnl`, `hash`, `oid`, `fee`, `feeToken`, `tid`.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"userFills"}'

// Result
Failed to deserialize the JSON body into the target type
```
{% endcode %}
