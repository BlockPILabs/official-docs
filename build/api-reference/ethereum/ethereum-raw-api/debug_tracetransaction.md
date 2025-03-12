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
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceTransaction","params":["0xb22833190fe739efe39ee23b2378d54753ffebf4684d00dd5b5c73087ba29701", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "from": "0x34a160f242f4962871b2ff55c4430375d3a9656e",
        "gas": "0x16119",
        "gasUsed": "0x1407c",
        "to": "0x495f947276749ce646f68ac8c248420045cb7b5e",
        "input": "0xf242432a00000000000000000000000034a160f242f4962871b2ff55c4430375d3a9656e00000000000000000000000048a2a576aa8743b9f7f6ed69987e72de3878f4cd34a160f242f4962871b2ff55c4430375d3a9656e000000000000020000000001000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000a00000000000000000000000000000000000000000000000000000000000000000360c6ebe",
        "value": "0x0",
        "type": "CALL"
    }
}
```
{% endcode %}
