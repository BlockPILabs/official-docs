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
* **QUANTITY|TAG** - integer block number, or the string "latest"

#### **Returns:**

**DATA** - the return value of executed contract.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://gnosis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"eth_call","params":[{"from":null,"to":"0x6b175474e89094c44da98b954eedeac495271d0f","data":"0x70a082310000000000000000000000006E0d01A76C3Cf4288372a29124A26D4353EE51BE"}, "latest"],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x"
}
```
{% endcode %}
