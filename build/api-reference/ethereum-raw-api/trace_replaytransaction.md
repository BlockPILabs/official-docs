---
description: >-
  Traces a call to eth_sendRawTransaction without making the call, returning the
  traces.
---

# trace\_replayTransaction

#### **Parameters:**

**DATA, 32 Bytes** - Transaction hash.

**Array** - Type of trace, one or more of: "vmTrace", "trace", "stateDiff".

#### **Returns:**

**Object** - Block traces.

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl https://arc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"trace_replayTransaction","params":["0xbc5f082a915fdad2cf2a550360489825a24d24d8e46895ff8e3cda28cbef6b29",["trace"]],"id":1,"jsonrpc":"2.0"}'
      
// Result
{
      "jsonrpc":"2.0",
      "id":1,
      "result":{   }
}
```
{% endcode %}
