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
curl https://base.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceBlockByHash","params":["0x33b3f51da4bb4d0753b6860c591e08890048adce5388f43cbc795c4d91eb5890", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result":{as described above}
}
```
{% endcode %}
