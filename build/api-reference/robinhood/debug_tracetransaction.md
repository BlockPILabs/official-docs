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
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"debug_traceTransaction","params":["0xaa4995a87c6375d17b178c5c9e5b9615b2c107043cae49366c6a3cb21d71fe4c",{"tracer":"callTracer"}],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
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
}
```
{% endcode %}
