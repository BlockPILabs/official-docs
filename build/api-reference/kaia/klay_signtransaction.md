---
description: >-
  Constructs a transaction with given parameters and signs the transaction with
  a sender's private key.
---

# kaia\_signTransaction

#### **Parameters**

The required parameters depend on the transaction type. Check the proper parameters in [Klaytn Docs](https://docs.klaytn.foundation/dapp/json-rpc/api-references/klay/transaction/transaction-type-support).

#### **Return Value**

| Type | Description                                         |
| ---- | --------------------------------------------------- |
| raw  | Signed raw transaction                              |
| tx   | Transaction object including the sender's signature |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "method":"kaia_signTransaction", "params":[{"from":"0x77982323172e5b6182539d3522d5a33a944206d4", "to":"0xcd6bfdb523a4d030890d28bf1eb6ef36307c9aaa", "value":"0x10000", "gas":"0x1000000", "nonce":"0x2", "gasprice":"0x25000000000"}],"id":73}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc":"2.0",
  "id":73,
  "result":{
    "raw":"0xf86c0286025000000000840100000094cd6bfdb523a4d030890d28bf1eb6ef36307c9aaa8301000080820fe8a056d2ddd231c3c111687ab351d339240db18cd721e5aa33c601dd4fc3927fb4d1a03443443392517aa7da082aa0a00b9ee5e3e1ee007d22e57cd9ff55b5ddbf4a64",
    "tx":{
      "nonce":"0x2",
      "gasPrice":"0x5d21dba00",
      "gas":"0x1000000",
      "to":"0xcd6bfdb523a4d030890d28bf1eb6ef36307c9aaa",
      "value":"0x10000",
      "input":"0x",
      "v":"0xfe8",
      "r":"0x56d2ddd231c3c111687ab351d339240db18cd721e5aa33c601dd4fc3927fb4d1",
      "s":"0x3443443392517aa7da082aa0a00b9ee5e3e1ee007d22e57cd9ff55b5ddbf4a64",
      "hash":"0xb53cc9128a19c3916c0de1914725b7337bba84666c2556d8682c72ca34c6874c"
    }
  }
}
```
{% endcode %}
