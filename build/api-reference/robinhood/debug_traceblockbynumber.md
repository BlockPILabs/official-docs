# debug\_traceblockbynumber

#### **Parameters:**

**QUANTITY|TAG** - integer block number, or the string "latest", "earliest" or "pending".

**Object** - (optional) Tracer configuration. Supported tracers: `callTracer`.

#### **Returns:**

**Array** - Array of trace results, one per transaction in the block. Each result includes `txHash` and trace output from the specified tracer.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"debug_traceBlockByNumber","params":["0x90a6f2",{"tracer":"callTracer"}],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "txHash": "0xaa4995a87c6375d17b178c5c9e5b9615b2c107043cae49366c6a3cb21d71fe4c",
      "result": {
        "beforeEVMTransfers": [],
        "afterEVMTransfers": [],
        "from": "0x00000000000000000000000000000000000a4b05",
        "gas": "0x0",
        "gasUsed": "0x0",
        "to": "0x00000000000000000000000000000000000a4b05",
        "input": "0x6bf6a42d...",
        "calls": [],
        "value": "0x0",
        "type": "CALL"
      }
    },
    "..."
  ]
}
```
{% endcode %}
