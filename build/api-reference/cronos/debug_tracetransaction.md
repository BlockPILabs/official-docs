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
curl https://cronos.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceTransaction","params":["0x469dfe519740073a1ce424b3eeaf136b4cb29d575e9a155266d7cf117b618844", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "from": "0xf690181fa630f3895643bbe8b0fccf90330ddeeb",
        "gas": "0x8d5d",
        "gasUsed": "0x5ff3",
        "input": "0x095ea7b30000000000000000000000008d13982c702fe7c6537529986df67dabeafc4c19ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000001",
        "to": "0x2d03bece6747adc00e1a131bba1469c15fd11e03",
        "type": "CALL",
        "value": "0x0"
    }
}
```
{% endcode %}
