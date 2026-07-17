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
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"debug_traceCall","params":[{"to":"0x00000000000000000000000000000000000a4b05"},"latest",{"tracer":"callTracer"}],"id":1}'

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
        "purpose": "feeCollection",
        "from": null,
        "to": "0x5a2B80a9b7effc06129bD5462D77BC20A8A59BE7",
        "value": "0x38d7ea4c68000"
      }
    ],
    "from": "...",
    "gas": "0x...",
    "gasUsed": "0x...",
    "input": "0x...",
    "to": "...",
    "type": "CALL",
    "value": "0x0"
  }
}
```
{% endcode %}
