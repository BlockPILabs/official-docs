---
description: Executes the given call and returns a number of possible traces for it.
---

# trace\_call

#### **Parameters:**

**Object** - The transaction call object

* **from: DATA, 20 Bytes** - (optional) The address the transaction is sent from.
* **to: DATA, 20 Bytes** - The address the transaction is directed to.
* **gas: QUANTITY** - (optional) Integer of the gas provided for the transaction execution. eth\_call consumes zero gas, but this parameter may be needed by some executions.
* **gasPrice: QUANTITY** - (optional) Integer of the gasPrice used for each paid gas
* **value: QUANTITY** - (optional) Integer of the value sent with this transaction
* **data: DATA** - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI in the Solidity documentation
* **QUANTITY|TAG** - integer block number, or the string "latest", see the default block parameter

#### **Returns:**

**Array** - Block traces

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl https://hyperliquid.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" -d '{"method":"trace_call","params":[{"from": "0x6f1FB6EFDf50F34bFA3F2bC0E5576EdD71631638","to": "0x1E0447b19BB6EcFdAe1e4AE1694b0C3659614e4e","value": "0x0","data": "0xa67a6a45000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000"},["trace"]],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc":"2.0",
    "id":1,
    "result":{ ..... }
}
```
{% endcode %}
