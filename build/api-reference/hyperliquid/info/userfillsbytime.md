# userFillsByTime

#### Parameters

type: userFillsByTime user: address (42-char hex) startTime: timestamp (ms) endTime: timestamp (ms)

#### Returns

Fills within the time range, paginated to 500 elements. Each fill includes coin, px, sz, side, time, dir, closedPnl, hash, oid, fee.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"userFillsByTime"}'

// Result
[]
```
{% endcode %}
