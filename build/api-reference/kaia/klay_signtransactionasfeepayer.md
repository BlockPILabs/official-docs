---
description: >-
  Constructs a transaction with given parameters and signs the transaction with
  a fee payer's private key.
---

# kaia\_signTransactionAsFeePayer

This method can be used either to generate a fee payer signature or to make a final raw transaction that is ready to submit to Klaytn network. In case you just want to extract the fee-payer signature, simply take the `feePayerSignatures` from the result. Note that the `raw` transaction is not final if the sender's signature is not attached (that is, `signatures` in `tx` is empty).

#### **Parameters**

The required parameters depend on the transaction type. Check the proper parameters in [Klaytn Docs](https://docs.klaytn.foundation/dapp/json-rpc/api-references/klay/transaction/transaction-type-support).

#### **Return Value**

| Type | Description                                            |
| ---- | ------------------------------------------------------ |
| raw  | Signed raw transaction                                 |
| tx   | Transaction object including the fee payer's signature |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "method": "kaia_signTransactionAsFeePayer", "params": [{"typeInt": 17, "from": "0xcd01b2b44584fb143824c1ea0231bebaea826b9d", "to": "0x44711E89b0c23845b5B2ed9D3716BA42b8a3e075", "gas": "0x76c0", "gasPrice": "0x5d21dba00", "value": "0xf4", "input": "0xb3f98adc0000000000000000000000000000000000000000000000000000000000000001", "feePayer": "0xcd01b2b44584fb143824c1ea0231bebaea826b9d"}], "id": 83}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
    "id": 83,
    "jsonrpc": "2.0",
    "result": {
        "raw": "0x11f8ba358505d21dba008276c09444711e89b0c23845b5b2ed9d3716ba42b8a3e07581f494cd01b2b44584fb143824c1ea0231bebaea826b9da4b3f98adc0000000000000000000000000000000000000000000000000000000000000001c094cd01b2b44584fb143824c1ea0231bebaea826b9df847f845824e43a0b34470d1bb588a6afe8f170333ca147e805727aa1911353ed544c31ad4863beca020322c2727091ff79458a87a424b53a4b08cc3d7d485e002e8bf0add13974507",
        "tx": {
            "feePayer": "0xcd01b2b44584fb143824c1ea0231bebaea826b9d",
            "feePayerSignatures": [
                {
                    "R": "0xb34470d1bb588a6afe8f170333ca147e805727aa1911353ed544c31ad4863bec",
                    "S": "0x20322c2727091ff79458a87a424b53a4b08cc3d7d485e002e8bf0add13974507",
                    "V": "0x4e43"
                }
            ],
            "from": "0xcd01b2b44584fb143824c1ea0231bebaea826b9d",
            "gas": "0x76c0",
            "gasPrice": "0x5d21dba00",
            "hash": "0x9e76f754b884d7853814a39c0e51fcefcef6f55b872f00ddad9724c9638128b3",
            "input": "0xb3f98adc0000000000000000000000000000000000000000000000000000000000000001",
            "nonce": "0x35",
            "signatures": [],
            "to": "0x44711e89b0c23845b5b2ed9d3716ba42b8a3e075",
            "type": "TxTypeFeeDelegatedValueTransferMemo",
            "typeInt": 17,
            "value": "0xf4"
        }
    }
}
```
{% endcode %}
