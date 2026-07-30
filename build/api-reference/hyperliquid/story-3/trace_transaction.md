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
```python
// Request
curl https://hyperliquid.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"trace_transaction","params":["0x358ab7164eefdffaa8e4fc171c9289905d09834af5ec59f8faa0964137ae0f3e"],"id":1,"jsonrpc":"2.0"}'
      
// Result
{
      "jsonrpc":"2.0",
      "id":1,
      "result":[.....]
}
```
{% endcode %}
