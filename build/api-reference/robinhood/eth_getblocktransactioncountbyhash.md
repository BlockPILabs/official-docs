# eth\_getblocktransactioncountbyhash

#### **Parameters:**

**DATA, 32 Bytes** - hash of a block.

#### **Returns:**

**QUANTITY** - integer of the number of transactions in this block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0x34c951125a0b42f16fa981ab9f82ff340acb2b4ae4b76d9cca9fa17cf084bf73"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x7"
}
```
{% endcode %}
