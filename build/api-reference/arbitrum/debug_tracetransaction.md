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
curl https://arbitrum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceTransaction","params":["0x051de401ea642ac93a2f6a7168bce659b59f48d9e56d7199e3a6c504dd5a712b", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

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
