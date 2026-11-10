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
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0x148ddcefd47234b60d4fe0463f7497ef7a71a27b","latest"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x11864e608b8c286d2"
}
```
{% endcode %}
