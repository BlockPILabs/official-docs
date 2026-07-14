# eth\_getblocktransactioncountbynumber

#### **Parameters:**

**QUANTITY|TAG** - integer of a block number, or the string "earliest", "latest" or "pending".

#### **Returns:**

**QUANTITY** - integer of the number of transactions in this block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params":["0x90a6f2"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x7"
}
```
{% endcode %}
