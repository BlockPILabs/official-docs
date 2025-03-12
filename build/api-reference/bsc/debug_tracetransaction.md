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
curl https://bsc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceTransaction","params":["0x023b70dc940203684ef33fa8292973f159c6ddd46a9190224472dae9175986aa", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "type": "CALL",
        "from": "0xa6f79b60359f141df90a0c745125b131caaffd12",
        "to": "0x0000000000000000000000000000000000001000",
        "value": "0xee70a883754ff3",
        "gas": "0x7fffffffffffac47",
        "gasUsed": "0x6a20",
        "input": "0xf340fa01000000000000000000000000a6f79b60359f141df90a0c745125b131caaffd12",
        "output": "0x",
        "calls": [
            {
                "type": "CALL",
                "from": "0x0000000000000000000000000000000000001000",
                "to": "0x000000000000000000000000000000000000dead",
                "value": "0x17d810d9f22198",
                "gas": "0x8fc",
                "gasUsed": "0x0",
                "input": "0x",
                "output": "0x"
            }
        ]
    }
}
```
{% endcode %}
