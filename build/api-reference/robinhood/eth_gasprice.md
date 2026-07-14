# eth\_gasprice

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - integer of the current gas price in wei.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x2a7cf40"
}
```
{% endcode %}
