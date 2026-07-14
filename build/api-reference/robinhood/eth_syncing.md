# eth\_syncing

#### **Parameters:**

None

#### **Returns:**

**Object|Boolean** - An object with sync status data or `false` when not syncing.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": false
}
```
{% endcode %}
