---
description: >-
  Executes a new message call immediately without creating a transaction on the
  blockchain.
---

# eth\_call

#### **Parameters:**

**Object** - The transaction call object

* **from: DATA, 20 Bytes** - (optional) The address the transaction is sent from.
* **to: DATA, 20 Bytes** - The address the transaction is directed to.
* **gas: QUANTITY** - (optional) Integer of the gas provided for the transaction execution. eth\_call consumes zero gas, but this parameter may be needed by some executions.
* **gasPrice: QUANTITY** - (optional) Integer of the gasPrice used for each paid gas
* **value: QUANTITY** - (optional) Integer of the value sent with this transaction
* **data: DATA** - (optional) Hash of the method signature and encoded parameters. Data size is limited to 20KB. For details see Ethereum Contract ABI in the Solidity documentation
* **QUANTITY|TAG** - integer block number, or the string "latest", see the default block paramete

#### **Returns:**

**DATA** - the return value of executed contract.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://flow-evm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_call","params":[{see above}],"id":1}'

// Result

```
{% endcode %}
