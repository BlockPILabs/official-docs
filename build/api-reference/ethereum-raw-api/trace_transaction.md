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
curl https://arc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"trace_transaction","params":["0xbc5f082a915fdad2cf2a550360489825a24d24d8e46895ff8e3cda28cbef6b29"],"id":1,"jsonrpc":"2.0"}'
      
// Result
{
      "jsonrpc":"2.0",
      "id":1,
      "result":{}
}
```
{% endcode %}
