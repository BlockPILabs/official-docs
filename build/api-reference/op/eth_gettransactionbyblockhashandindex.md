---
description: Returns the information about a transaction requested by Block hash and index.
---

# eth\_getTransactionByBlockHashAndIndex

#### **Parameters:**

**DATA , 32 Bytes** - Hash of a block.

**QUANTITY** - A hex of the integer representing the position in the block.

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
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0x3b32dd164f1eb2b1f925c214e7180bf35280cf233a01f7e3a5d70203912e6808", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xcf0f82ad6366f4d0cb6e86f2bfec25cdc24f9a131a9f040997d731967ea17973",
        "blockNumber": "0x2b65591",
        "from": "0xafa00726af4abc5e68225a18419d6658f5eb7168",
        "gas": "0xe4e1c0",
        "gasPrice": "0xf4240",
        "hash": "0xfd6a199ca98aa785f8b70fc862f2b148615a43df5c09d7e85069cefe87848972",
        "input": "0xb6b1b6c300000000000000000000000077d0cc9568605bfff32f918c8ffaa53f729014160000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000059fd20b4f16c7000000000000000000000000000000000000000000000000000015af8965e6655afa38ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00000000000000000000000000000000000000000000000000000000000000003166363939373461393700000000000000000000000000000000000000000000",
        "nonce": "0x3ea4",
        "to": "0x82ac2ce43e33683c58be4cdc40975e73aa50f459",
        "transactionIndex": "0x0",
        "value": "0x0",
        "v": "0x37",
        "r": "0x30d7c2e06e8af311bc1b61a7119293b14eb877d2d17fef2871d634dc1019371",
        "s": "0x4d8d79f62c295e7e9415d799cdd1bbcc8fdb644c53c58860124ba6c03c78ec16",
        "queueOrigin": "sequencer",
        "l1TxOrigin": null,
        "l1BlockNumber": "0xf5e9a3",
        "l1Timestamp": "0x638d71fb",
        "index": "0x2b65590",
        "queueIndex": null,
        "rawTransaction": "0xf9016b823ea4830f424083e4e1c09482ac2ce43e33683c58be4cdc40975e73aa50f45980b90104b6b1b6c300000000000000000000000077d0cc9568605bfff32f918c8ffaa53f729014160000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000059fd20b4f16c7000000000000000000000000000000000000000000000000000015af8965e6655afa38ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000000000000000316636393937346139370000000000000000000000000000000000000000000037a0030d7c2e06e8af311bc1b61a7119293b14eb877d2d17fef2871d634dc1019371a04d8d79f62c295e7e9415d799cdd1bbcc8fdb644c53c58860124ba6c03c78ec16"
    }
}
```
{% endcode %}
