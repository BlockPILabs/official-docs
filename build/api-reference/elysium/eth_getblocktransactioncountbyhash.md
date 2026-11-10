# eth\_getblocktransactioncountbyhash

#### **Parameters:**

**DATA, 32 Bytes** - hash of a block.

#### **Returns:**

**QUANTITY** - integer of the number of transactions in this block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0x2eb03f8c3c8379c1e5004f1cca58a7a88c9895efe856316d69793912b823db46"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x7"
}
```
{% endcode %}
