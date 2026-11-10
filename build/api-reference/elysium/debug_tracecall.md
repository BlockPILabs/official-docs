# debug\_tracecall

#### **Parameters:**

**Object** - The transaction call object (same as eth\_call).

**QUANTITY|TAG** - integer block number, or the string "latest", "earliest" or "pending".

**Object** - (optional) Tracer configuration. Supported tracers: `callTracer`.

#### **Returns:**

**Object** - The trace result. With `callTracer`, returns call traces including `beforeEVMTransfers`, `afterEVMTransfers`, and nested `calls`.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"debug_traceCall","params":[{"to":"0x063f7cc5339f92a5fd7baf3d22233044fda1f327","data":"0x18160ddd"},"latest",{"tracer":"callTracer"}],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "beforeEVMTransfers": [
      {
        "purpose": "feePayment",
        "from": "0x0000000000000000000000000000000000000000",
        "to": null,
        "value": "0x0"
      }
    ],
    "afterEVMTransfers": [
      {
        "purpose": "gasRefund",
        "from": null,
        "to": "0x0000000000000000000000000000000000000000",
        "value": "0x0"
      },
      {
        "purpose": "tip",
        "from": null,
        "to": "0x6CBb552855CE5Eb70af49B76a8048be8E3799A05",
        "value": "0x0"
      },
      "..."
    ],
    "from": "0x0000000000000000000000000000000000000000",
    "gas": "0x2faf080",
    "gasUsed": "0x6656",
    "to": "0x063f7cc5339f92a5fd7baf3d22233044fda1f327",
    "input": "0x18160ddd",
    "output": "0x0000000000000000000000000000000000000000033b2e3c9fd0803ce7fc8c62",
    "calls": [
      {
        "from": "0x063f7cc5339f92a5fd7baf3d22233044fda1f327",
        "gas": "0x2eea9a3",
        "gasUsed": "0x9a4",
        "to": "0x10b0292fb853966d3039d80bbef98b1a9507f55f",
        "input": "0x18160ddd",
        "output": "0x0000000000000000000000000000000000000000033b2e3c9fd0803ce7fc8c62",
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
