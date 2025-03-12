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
curl https://mantle.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"debug_traceCall","params":[{"from":"0xDAFEA492D9c6733ae3d56b7Ed1ADB60692c98Bc5","to":"0x4675C7e5BaAFBFFbca748158bEcBA61ef3b0a263","data":"0xf00d4b5d00000000000000000000000001291230982139282304923482304912923823920000000000000000000000001293123098123928310239129839291010293810"}, "latest"],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "gas": 95051304,
        "failed": false,
        "returnValue": "",
        "structLogs": []
    }
}
```
{% endcode %}
