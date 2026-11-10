# eth\_call

#### **Parameters:**

**Object** - The transaction call object:

* **from: DATA, 20 Bytes** - (optional) The address the transaction is sent from.
* **to: DATA, 20 Bytes** - The address the transaction is directed to.
* **gas: QUANTITY** - (optional) Integer of the gas provided for the transaction execution.
* **gasPrice: QUANTITY** - (optional) Integer of the gasPrice used for each paid gas.
* **value: QUANTITY** - (optional) Integer of the value sent with this transaction.
* **data: DATA** - (optional) Hash of the method signature and encoded parameters.

**QUANTITY|TAG** - integer block number, or the string "latest", "earliest" or "pending".

#### **Returns:**

**DATA** - the return value of executed contract.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_call","params":[{"to":"0x063f7cc5339f92a5fd7baf3d22233044fda1f327","data":"0x18160ddd"},"latest"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x0000000000000000000000000000000000000000033b2e3c9fd0803ce7fc8c62"
}
```
{% endcode %}
