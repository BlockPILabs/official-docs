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
curl https://taiko-hekla.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceBlockByHash","params":["0x9ed304f0736ba4acaa45a33a31ae15e81ac4e8a4eaaec8cfd5b080d46fa1acc9", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result":{as described above}
}
```
{% endcode %}
