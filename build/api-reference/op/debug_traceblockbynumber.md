---
description: >-
  It accepts a block number and will replay the block that is already present in
  the database.
---

# debug\_traceBlockByNumber

#### **Parameters:**

**QUANTITY|TAG** - integer block number, or the string "latest", "pending"

{% hint style="info" %}
Due to the high block speed of Optimism, this method with "latest" parameter will probably get error code 32000 with message “block #-1 not found”
{% endhint %}

**Object** - tracer

* **tracer: string** - the type of tracer. Currently supports `callTracer` and `prestateTracer`

#### **Returns:**

**Array** - Block traces

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceBlockByNumber","params":["latest", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {as described above}
}
```
{% endcode %}
