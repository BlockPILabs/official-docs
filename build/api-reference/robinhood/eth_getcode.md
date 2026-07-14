# eth\_getcode

#### **Parameters:**

**DATA, 20 Bytes** - address.

**QUANTITY|TAG** - integer block number, or the string "latest", "earliest" or "pending".

#### **Returns:**

**DATA** - the code from the given address.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getCode","params":["0x0000000000000000000000000000000000000000", "latest"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
```
{% endcode %}
