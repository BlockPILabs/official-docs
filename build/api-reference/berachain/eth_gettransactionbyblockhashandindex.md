---
description: Returns the information about a transaction requested by Block hash and index.
---

# eth\_getTransactionByBlockHashAndIndex

#### **Parameters:**

**DATA , 32 Bytes** - Hash of a block.

**QUANTITY** - A decimal of the integer representing the position in the block.

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
curl https://berachain-bartio.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0x3838986ac3faa52e0b453d2cb957879181ce40f9f29a23f8af90c9dd6b14a6af", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x3838986ac3faa52e0b453d2cb957879181ce40f9f29a23f8af90c9dd6b14a6af",
        "blockNumber": "0x35cce",
        "from": "0x2da8c7d5118eb36577e80aa28516ed76f1d8214b",
        "gas": "0x5208",
        "gasPrice": "0x141807ee0",
        "hash": "0x9c066fa68ef6bea6358779929a7b43e61ee2083c813ddfcb0b546efa9c675fe8",
        "input": "0x",
        "nonce": "0x2672",
        "to": "0x6d4ce88fe864750b11f5fda496dbc17d5957c843",
        "transactionIndex": "0x0",
        "value": "0x2386f26fc10000",
        "type": "0x0",
        "chainId": "0x138d4",
        "v": "0x271cc",
        "r": "0x32c9cb700f75a3d20d4d2bca6b223f03f5e5fc8126c00418d047d5b8723ab5cd",
        "s": "0x152ca35ea0fb4fcd633b6b36441ba1d1a38a241326a3e8167094b6d47a43d389"
    }
}
```
{% endcode %}
