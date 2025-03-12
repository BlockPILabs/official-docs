---
description: Returns all traces of given transaction.
---

# trace\_transaction

#### **Parameters:**

**DATA, 32 Bytes** - Transaction hash.

#### **Returns:**

**Array**- Trace object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://fantom.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"trace_transaction","params":["0xa455c9030e7083763f0a71c2e2eda11f417d0ffadec9e64d482226f71585ea97"],"id":1,"jsonrpc":"2.0"}'
      
// Result
{
      "jsonrpc":"2.0",
      "id":1,
      "result": as described above
}
```
{% endcode %}
