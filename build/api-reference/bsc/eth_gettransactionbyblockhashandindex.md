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
curl https://bsc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0xa8d01d6d5e70cb3bd8cd423eaa11714b89adef041141e4ca31bcdc6879543b23", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xcd3d2d7f7d4beedcfddcc2cdf4758f911f44400fad5e50ef95154127ece62371",
        "blockNumber": "0x16c92e2",
        "from": "0xad5ef36ff278f23935a3938b8e7bdac93c09b8bc",
        "gas": "0x9c40",
        "gasPrice": "0x28fa6ae00",
        "hash": "0x9c362aaea45824456000af776f3c43a3084d0468480b6bd611472268ee170657",
        "input": "0x",
        "nonce": "0x3",
        "to": "0x9239df3e9996c776d539eb9f01a8ae8e7957b3c3",
        "transactionIndex": "0x0",
        "value": "0x8a00557fa7e3f8",
        "type": "0x0",
        "chainId": "0x38",
        "v": "0x93",
        "r": "0x4db978af2a1e3c73931dcb8f919a52a2ae8be8f26071787181ecf93750d6e8cc",
        "s": "0x772657d4d5e95e3c3409d6016d0b4d944d7ab1e35c748242a0f1d166da3a6ecb"
    }
}
```
{% endcode %}
