# candleSnapshot

#### Parameters

| Name | Type   | Required | Description                            |
| ---- | ------ | -------- | -------------------------------------- |
| type | String | Yes      | `"candleSnapshot"`                     |
| req  | Object | Yes      | `{coin, interval, startTime, endTime}` |

#### Returns

**Array** - OHLCV candles with `t`, `T`, `s`, `i`, `o`, `c`, `h`, `l`, `v`, `n`.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"candleSnapshot"}'

// Result
Failed to deserialize the JSON body into the target type
```
{% endcode %}
