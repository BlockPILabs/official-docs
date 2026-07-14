# eth\_uninstallfilter

#### **Parameters:**

**QUANTITY** - the filter id.

#### **Returns:**

**Boolean** - true if the filter was successfully uninstalled, otherwise false.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_uninstallFilter","params":["0x1"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": true
}
```
{% endcode %}
