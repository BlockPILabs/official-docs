---
description: >-
  It accepts a block hash and will replay the block that is already present in
  the database.
---

# debug\_traceBlockByHash

#### **Parameters:**

**String** - The hash of a block.

**Object** - tracer

* **tracer: string** - the type of tracer. Currently supports `callTracer` and `prestateTracer`

#### **Returns:**

**Array** - Block traces

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zkfair.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
'{"method":"debug_traceBlockByHash","params":["0x109b778ef3bc180756de7e5278e0367bdb880ceb58b0a50ab375cba29232e4d2", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result":{as described above}
}
```
{% endcode %}
