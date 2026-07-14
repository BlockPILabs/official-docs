# eth\_getbalance

#### **Parameters:**

**DATA, 20 Bytes** - address to check for balance.

**QUANTITY|TAG** - integer block number, or the string "latest"

#### **Returns:**

**QUANTITY** - integer of the current balance in wei.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0x0000000000000000000000000000000000000000", "latest"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x19a1c0529137bbd"
}
```
{% endcode %}
