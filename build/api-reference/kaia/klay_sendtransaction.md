---
description: >-
  Constructs a transaction with given parameters, signs the transaction with a
  sender's private key and propagates the transaction to Klaytn network.
---

# kaia\_sendTransaction

#### **Parameters**

The required parameters depend on the transaction type. Check the proper parameters in [Klaytn Docs](https://docs.klaytn.foundation/dapp/json-rpc/api-references/klay/transaction/transaction-type-support).

#### **Return Value**

| Type         | Description          |
| ------------ | -------------------- |
| 32-byte DATA | The transaction hash |

#### Example

{% code overflow="wrap" %}
```json
params: [{
  "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
  "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
  "gas": "0x76c0",
  "gasPrice": "0x5d21dba00",
  "value": "0x9184e72a",
  "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
}]
```
{% endcode %}

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_sendTransaction","params":[{see above}],"id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0","id":1,
  "result": "0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331"
}
```
{% endcode %}
