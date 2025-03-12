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
curl https://fantom.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0x0002cd1b00000002c49530f0cb42883a2ba875674f7d6c9731754cb2fa23d2e0", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x0002cd1b00000002c49530f0cb42883a2ba875674f7d6c9731754cb2fa23d2e0",
        "blockNumber": "0x3315cf2",
        "from": "0x13c032093e328ec3fd69d2f1387b7b024feeef42",
        "gas": "0x895440",
        "gasPrice": "0x773594000",
        "hash": "0x3ed42ac6fd8420ac738b792d5309ecc93e7cec7ab942d11e9f7baf21eb66bf2f",
        "input": "0xa0712d68000000000000000000000000000000000000000000000000000000000000004d",
        "nonce": "0x35",
        "to": "0x97faab98f1a9e5c803c43a6293759fcc7ed000b9",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x0",
        "v": "0x217",
        "r": "0x2e7c3caaa817a63bb22f864a5657500edcc834c7b5aafe7116d002d2bf33bcb3",
        "s": "0x3e6f9f7cb3c1ee4dc892042ed4aca8dc5a5f552d764a96f77e084de89d1ce9c0"
    }
}
```
{% endcode %}
