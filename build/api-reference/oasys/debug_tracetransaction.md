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
curl https://oasys.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceTransaction","params":["0xed6e4d07686102382d4e42f6afaf1ddf8a93862ca3e6311ada8a3fc7cb35b5dd", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "type": "CALL",
        "from": "0xa0802796357f38cd3fc2eee9ee8ed2698b2768df",
        "to": "0x8ce03750afe5ec733ca4590c612d652ee28d43f2",
        "value": "0x7abb4ea652b5455000",
        "gas": "0x169158",
        "gasUsed": "0x0",
        "input": "0x",
        "output": "0x"
    }
}
```
{% endcode %}
