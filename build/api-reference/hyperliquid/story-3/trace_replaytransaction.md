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
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"trace_replayTransaction","params":["0x358ab7164eefdffaa8e4fc171c9289905d09834af5ec59f8faa0964137ae0f3e",["trace"]],"id":1,"jsonrpc":"2.0"}'
      
// Result
{
      "jsonrpc":"2.0",
      "id":1,
      "result":{ ... }
}
```
{% endcode %}
