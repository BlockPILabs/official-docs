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
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"candleSnapshot","req":{"coin":"BTC","interval":"1h","startTime":1785000000000,"endTime":1785500000000}}'


// Result
[
  {
    "t": 1784998800000,
    "T": 1785002399999,
    "s": "BTC",
    "i": "1h",
    "o": "64184.0",
    "c": "64240.0",
    "h": "64314.0",
    "l": "64170.0",
    "v": "505.08496",
    "n": 5893
  },
......
```
{% endcode %}
