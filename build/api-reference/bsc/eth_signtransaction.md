---
description: >-
  Signs a transaction that can be submitted to the network at a later time using
  with eth_sendRawTransaction.
---

# eth\_signTransaction

#### **Parameters:**

Object - The transaction object.

* **from: DATA, 20 Bytes** - The address the transaction is sent from.
* **to: DATA, 20 Bytes** - (optional when creating new contract) The address the transaction is directed to.
* **gas: QUANTITY** - (optional, default: 90000) Integer of the gas provided for the transaction execution. It will return unused gas.
* **gasPrice: QUANTITY** - (optional, default: To-Be-Determined) Integer of the gasPrice used for each paid gas, in Wei.
* **value: QUANTITY** - (optional) Integer of the value sent with this transaction, in Wei.
* **data: DATA** - The compiled code of a contract OR the hash of the invoked method signature and encoded parameters.
* **nonce: QUANTITY** - Integer of a nonce. This allows to overwrite your own pending transactions that use the same nonce.

#### **Returns:**

**DATA** - The signed transaction object.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://bsc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"id": 1,"jsonrpc": "2.0","method": "eth_signTransaction","params": [{"data":"0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675","from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155","gas": "0x76c0","gasPrice": "0x9184e72a000","to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567","value": "0x9184e72a", "nonce": "0x224668765"}]}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": []
}
```
{% endcode %}
