# eth\_getfilterchanges

#### **Parameters:**

**QUANTITY** - the filter id.

#### **Returns:**

**Array** - Array of log objects, or an empty array if nothing has changed since last poll.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getFilterChanges","params":["0x1"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": []
}
```
{% endcode %}
