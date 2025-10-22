---
description: >-
  Constructs a transaction with given parameters, signs the transaction with a
  fee payer's private key and propagates the transaction to Klaytn network.
---

# klay\_sendTransactionAsFeePayer

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
  "typeInt": 18,
  "from": "0xcd01b2b44584fb143824c1ea0231bebaea826b9d",
  "to": "0x44711E89b0c23845b5B2ed9D3716BA42b8a3e075",
  "gas": "0x4a380",
  "gasPrice": "0x5d21dba00",
  "nonce": "0x2c",
  "value": "0xf4",
  "input": "0xb3f98adc0000000000000000000000000000000000000000000000000000000000000001",
  "feePayer": "0xcd01b2b44584fb143824c1ea0231bebaea826b9d",
  "feeRatio": 30,
  "signatures": [{
    "V": "0x4e43", 
    "R": "0xd3ff5ca7bdd0120d79e8aa875593d05022fe74ce2b7a0594218d53c0fdca7fa9", 
    "S": "0x2c100e69d2455afc9393e017514063da18b18db6f7e811d0aeaf6002515b58ef"
  }]
}]
```
{% endcode %}

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_sendTransactionAsFeePayer","params":[{see above}],"id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0","id":1,
  "result": "0x77ec2d910d0b96585373e2d6508f2b2d8c2af7d0060d2012e1cb2f0ee9d74830"
}
```
{% endcode %}
