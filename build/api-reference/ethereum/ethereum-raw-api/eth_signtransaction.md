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
* **nonce: QUANTITY** - (optional) Integer of a nonce. This allows to overwrite your own pending transactions that use the same nonce.

#### **Returns:**

**DATA** - The signed transaction object.

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"id": 1,"jsonrpc": "2.0","method": "eth_signTransaction","params": [{"data":"0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675","from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155","gas": "0x76c0","gasPrice": "0x9184e72a000","to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567","value": "0x9184e72a"}]}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0xa3f20717a250c2b0b729b7e5becbff67fdaef7e0699da4de7ca5895b02a170a12d887fd3b17bfdce3481f10bea41f45ba9f709d39ce8325427b57afcfc994cee1b"
}
```
{% endcode %}
