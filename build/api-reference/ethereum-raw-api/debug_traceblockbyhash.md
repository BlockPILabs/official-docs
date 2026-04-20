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
```python
// Request
curl https://arc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceBlockByHash","params":["0xb84173b6534d0cee34905b621f21e5e518c464feb549f1372640b3fec137b3b2", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result":{as described above}
}
```
{% endcode %}
