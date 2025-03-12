---
description: Returns trace at given position.
---

# trace\_get

#### **Parameters:**

**DATA, 32 Bytes** - Transaction hash.

**Array** - Index positions of the traces.

#### **Returns:**

**Object**- Trace object

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"trace_get","params":["0x023b70dc940203684ef33fa8292973f159c6ddd46a9190224472dae9175986aa",["0x0"]],"id":1,"jsonrpc":"2.0"}'
      
// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": null
}
```
{% endcode %}
