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

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://kaia.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceTransaction","params":["0x023b70dc940203684ef33fa8292973f159c6ddd46a9190224472dae9175986aa", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc":"2.0",
    "id":1,"result":{
        "structLogs":[],
        "gas":21000,
        "failed":false,
        "returnValue":""
    }
}
```
{% endcode %}
