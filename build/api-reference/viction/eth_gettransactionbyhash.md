---
description: Returns the information about a transaction requested by transaction hash.
---

# eth\_getTransactionByHash

#### **Parameters:**

**DATA, 32 Bytes** - hash of a transaction

#### **Returns:**

**Object** - A transaction object, or null when no transaction was found:

* **blockHash: DATA, 32 Bytes** - hash of the block where this transaction was in.
* **blockNumber: QUANTITY** - block number where this transaction was in.
* **from: DATA, 20 Bytes** - address of the sender.
* **gas: QUANTITY** - gas provided by the sender.
* **gasPrice: QUANTITY** - gas price provided by the sender in Wei.
* **hash: DATA, 32 Bytes** - hash of the transaction.
* **input: DATA** - the data send along with the transaction.
* **nonce: QUANTITY** - the number of transactions made by the sender prior to this one.
* **to: DATA, 20 Bytes** - address of the receiver. null when its a contract creation transaction.
* **transactionIndex: QUANTITY** - integer of the transactions index position in the block.
* **value: QUANTITY** - value transferred in Wei.
* **v: QUANTITY** - ECDSA recovery id
* **r: DATA, 32 Bytes** - ECDSA signature r
* **s: DATA, 32 Bytes** - ECDSA signature s

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://viction.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xe989f85cd3f4ff61c7b687e74609702773d7eac3f10fea2433cd875e9d89ab5c"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x744a3dac0d390c212fbc318972bc9200d8c9aff01ae4f063634343457d30fbc9",
        "blockNumber": "0x41b123f",
        "from": "0x806d90e6087cee9288e7beda6294fd0138b5897a",
        "gas": "0x2625a00",
        "gasPrice": "0x0",
        "hash": "0xe989f85cd3f4ff61c7b687e74609702773d7eac3f10fea2433cd875e9d89ab5c",
        "input": "0xd279eebfd852efdc89662a7655ff504847639042205edf379970b4c4d6627033a4b83a97a63b3a879373bc957b9634e62884604b6435f14901ec2db41bc24ce7",
        "nonce": "0x32f1a6",
        "to": "0x0000000000000000000000000000000000000092",
        "transactionIndex": "0x0",
        "value": "0x0",
        "v": "0xd4",
        "r": "0x2452a33020d7d022aa973c13feb84b35c1d29f982fc6ebdff83496f6c677d7a1",
        "s": "0x5db50bd11bd29fa7a2e24da9757b684a32b5b646266e713b069b2e9e8517f194"
    }
}
```
{% endcode %}
