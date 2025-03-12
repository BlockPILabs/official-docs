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
curl https://viction.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0x9f2a3cc38610f5a208357dd78550b36bd4e982fb8e4447badf5cb983967a39dd", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x9f2a3cc38610f5a208357dd78550b36bd4e982fb8e4447badf5cb983967a39dd",
        "blockNumber": "0x41b1a6d",
        "from": "0x7a3181f4e1c9be0f67bb142e797ae6fd3bf89bb7",
        "gas": "0x2625a00",
        "gasPrice": "0x0",
        "hash": "0x26f42b2fdc7e22cad9b806b7b93b2b12867b84e5ccc3bc1cdf1d04110d872d9d",
        "input": "0xd279eebfd852efdc89662a7655ff504847639042205edf379970b4c4d6627033a4b83a97a63b3a879373bc957b9634e62884604b6435f14901ec2db41bc24ce7",
        "nonce": "0x34a292",
        "to": "0x0000000000000000000000000000000000000092",
        "transactionIndex": "0x0",
        "value": "0x0",
        "v": "0xd3",
        "r": "0xb5b651d2f7c8a1d72214ded21ea343c40eac42721a9dfea328f7a77850b08209",
        "s": "0x48fc741bc42de0ca116b577bb410fd99515226126fb677aac173dbd568e762e1"
    }
}
```
{% endcode %}
