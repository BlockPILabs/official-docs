---
description: >-
  Returns the information about a transaction requested by Block number and
  index.
---

# eth\_getTransactionByBlockNumberAndIndex

#### **Parameters:**

**QUANTITY|TAG** - Integer block number encoded as a hexadecimal, or the string 'latest', 'earliest' or 'pending'.

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
curl https://viction.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["latest", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xb4de89b26d4d8bb77795d8b87c19c374b5513791ca24a860038cd8fd2c4ff9ea",
        "blockNumber": "0x41b1a91",
        "from": "0x07a6033eda9cee42238c7416ad6215d15b7676df",
        "gas": "0x2625a00",
        "gasPrice": "0x0",
        "hash": "0x56b8bbb014f7dedf5b7cce21c394b0093801f523b1bcb6d2350d304ca6d4a80e",
        "input": "0xd279eebfd852efdc89662a7655ff504847639042205edf379970b4c4d6627033a4b83a97a63b3a879373bc957b9634e62884604b6435f14901ec2db41bc24ce7",
        "nonce": "0x2dce8f",
        "to": "0x0000000000000000000000000000000000000092",
        "transactionIndex": "0x0",
        "value": "0x0",
        "v": "0xd3",
        "r": "0xa14c8179700d04a7b9282635715c2622f56a9c9069fb616db039c9eeb2558ac1",
        "s": "0x6a87ae38fc9b44409a9a5b3fc80ba8685d174c2a51e281168b7df61776e63b41"
    }
}
```
{% endcode %}
