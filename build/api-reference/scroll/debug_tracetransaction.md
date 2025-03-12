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
curl https://scroll.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceTransaction","params":["0x051de401ea642ac93a2f6a7168bce659b59f48d9e56d7199e3a6c504dd5a712b", {"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "type": "CALL",
        "from": "0x097258f96d538164c1434f4c0ff692a4cee3fe6f",
        "to": "0x80732890c93c6d9c6c23e06f888ed0cb88a06018",
        "value": "0x0",
        "gas": "0x6c21",
        "gasUsed": "0x6abe",
        "input": "0x095ea7b300000000000000000000000048235a4b7d02f5874dc82f7419cbeaeb0043ef2fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000001",
        "calls": [
            {
                "type": "DELEGATECALL",
                "from": "0x80732890c93c6d9c6c23e06f888ed0cb88a06018",
                "to": "0xc18cc36288f0b91021a42693715b38dda83e30f6",
                "gas": "0x6048",
                "gasUsed": "0x6048",
                "input": "0x095ea7b300000000000000000000000048235a4b7d02f5874dc82f7419cbeaeb0043ef2fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
                "output": "0x0000000000000000000000000000000000000000000000000000000000000001"
            }
        ]
    }
}
```
{% endcode %}
