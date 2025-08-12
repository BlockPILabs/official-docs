---
description: >-
  It will attempt to run the transaction in the exact same manner as it was
  executed on the network.
---

# debug\_traceTransaction

#### **Parameters:**

**String** - The hash of a transaction.

**Object** - tracer

* **tracer: string** - the type of tracer. Currently supports `callTracer` and `prestateTracer`

#### **Returns:**

**Array** - Block traces

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://flow-evm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceTransaction","params":["0x9f2a696055fd384535905af4340406ef7169182f6c890183e35827385e48edaa", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": -
}
```
{% endcode %}
