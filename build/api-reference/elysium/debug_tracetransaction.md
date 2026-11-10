# debug\_tracetransaction

#### **Parameters:**

**DATA, 32 Bytes** - hash of a transaction.

**Object** - (optional) Tracer configuration. Supported tracers: `callTracer`.

#### **Returns:**

**Object** - The trace result from replaying the transaction. With `callTracer`, returns call traces including nested calls, `beforeEVMTransfers`, and `afterEVMTransfers`.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"debug_traceTransaction","params":["0xc6ed0a1582d665eca7f4d61f87d9ec72c58b6643ec864af2b6ed8dd665356a03",{"tracer":"callTracer"}],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "beforeEVMTransfers": [
      {
        "purpose": "feePayment",
        "from": "0x148dDcEfd47234B60d4fe0463F7497ef7a71A27b",
        "to": null,
        "value": "0x1118ecd0e3800"
      }
    ],
    "afterEVMTransfers": [
      {
        "purpose": "gasRefund",
        "from": null,
        "to": "0x148dDcEfd47234B60d4fe0463F7497ef7a71A27b",
        "value": "0xced9ca48e540"
      },
      {
        "purpose": "tip",
        "from": null,
        "to": "0x6CBb552855CE5Eb70af49B76a8048be8E3799A05",
        "value": "0x2c7dc8a09020"
      },
      "..."
    ],
    "from": "0x148ddcefd47234b60d4fe0463f7497ef7a71a27b",
    "gas": "0x30d40",
    "gasUsed": "0xbe82",
    "to": "0x063f7cc5339f92a5fd7baf3d22233044fda1f327",
    "input": "0x095ea7b3000000000000000000000000ca0d2b3047e547fd256c325db04634fa923aab52000000000000000000000000000000000000000000000d51097a8a84d0836dc5",
    "output": "0x0000000000000000000000000000000000000000000000000000000000000001",
    "calls": [
      {
        "from": "0x063f7cc5339f92a5fd7baf3d22233044fda1f327",
        "gas": "0x2a386",
        "gasUsed": "0x5f5c",
        "to": "0x10b0292fb853966d3039d80bbef98b1a9507f55f",
        "input": "0x095ea7b3000000000000000000000000ca0d2b3047e547fd256c325db04634fa923aab52000000000000000000000000000000000000000000000d51097a8a84d0836dc5",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000001",
        "value": "0x0",
        "type": "DELEGATECALL"
      }
    ],
    "value": "0x0",
    "type": "CALL"
  }
}
```
{% endcode %}
