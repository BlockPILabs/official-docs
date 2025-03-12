---
description: >-
  The method lets you run an eth_call within the context of the given block
  execution using the final state of parent block as the base.
---

# debug\_traceCall

#### **Parameters:**

**Object** - The transaction call object

* **from: DATA, 20 Bytes** - String of the address the transaction is sent from
* **to: DATA, 20 Bytes** - String of the address the transaction is directed to
* **gas: QUANTITY** - Integer of the gas provided for the transaction execution&#x20;
* **gasPrice: QUANTITY** - Integer of the gasPrice used for each paid gas
* **value: QUANTITY** - Integer of the value sent with this transaction
* **data: DATA** - Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI in the Solidity documentation
* **QUANTITY|TAG** - integer block number, or the string "latest"

**Object** - tracer

* **tracer: string** - the type of tracer. Currently supports `callTracer` and `prestateTracer`

#### **Returns:**

**Array** - Block traces

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceCall","params": [{"to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567"},"finalized",{"tracer": "callTracer"}],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": -
}
```
{% endcode %}
