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
curl https://t3rn.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0x8a7c32a1810f6b940bb46aa0c569d3c0f01a6e5fbb2d9f471cb2124b5eccea29", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x8a7c32a1810f6b940bb46aa0c569d3c0f01a6e5fbb2d9f471cb2124b5eccea29",
        "blockNumber": "0x311ace",
        "from": "0x00000000000000000000000000000000000a4b05",
        "gas": "0x0",
        "gasPrice": "0x0",
        "hash": "0x13699866bbf3ee49a65dfa0258c1179786b57f833da2c7ad9c3ef1f2f596afba",
        "input": "0x6bf6a42d000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007a8f910000000000000000000000000000000000000000000000000000000000311ace0000000000000000000000000000000000000000000000000000000000000001",
        "nonce": "0x0",
        "to": "0x00000000000000000000000000000000000a4b05",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x6a",
        "chainId": "0x14e",
        "v": "0x0",
        "r": "0x0",
        "s": "0x0"
    }
}
```
{% endcode %}
