---
description: >-
  Generates and returns an estimate of how much gas is necessary to allow the
  transaction to complete. The transaction will not be added to the blockchain.
---

# eth\_estimateGas

#### **Parameters:**

Expect that all properties are optional.

**Object** - The transaction call object

* **from: DATA, 20 Bytes** - The address the transaction is sent from.
* **to: DATA, 20 Bytes** - The address the transaction is directed to.
* **gas: QUANTITY** - Integer of the gas provided for the transaction execution. eth\_call consumes zero gas, but this parameter may be needed by some executions.
* **gasPrice: QUANTITY** - Integer of the gasPrice used for each paid gas
* **value: QUANTITY** - Integer of the value sent with this transaction
* **data: DATA** - Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI in the Solidity documentation
* **QUANTITY|TAG** - integer block number, or the string "latest", see the default block paramete

#### **Returns:**

**QUANTITY** - the amount of gas used.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://etherlink.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_estimateGas","params":[{see above}],"id":1}'

// Result

```
{% endcode %}
