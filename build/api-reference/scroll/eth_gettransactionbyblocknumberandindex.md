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
curl https://scroll.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["latest", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xfcae4feabe3a1ee2611e71048a51eff0eb493078adfde885c31741fa98f30448",
        "blockNumber": "0xe5f15",
        "from": "0x6648362723bc0e071d75caea3bad65527c12ddb3",
        "gas": "0x294d0",
        "gasPrice": "0x59682f07",
        "hash": "0x418f2a406581ca4d56a46943269e45dfaae57551c40becfc64ea752419e198fc",
        "input": "0x9e353c7000000000000000000000000094cf11667b017e9fef7ab557e2ef9eff6fdfedc30000000000000000000000008318ed43dd6760da6a01b7605c408841e706241900000000000000000000000000000000000000000000000000c0168841939400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000639a95a5000000000000000000000000000000000000000000000000000000000008a6ac00000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000000a4232e87480000000000000000000000005ac2085c7ebddb5fb5e4c126f7e73637da7ab4050000000000000000000000005ac2085c7ebddb5fb5e4c126f7e73637da7ab40500000000000000000000000000000000000000000000000000c01688419394000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x58c90",
        "to": "0xe06f3c8076dcf99bc7b9f7a552fe9d18e4c5e85c",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x1",
        "accessList": [],
        "chainId": "0x82752",
        "v": "0x0",
        "r": "0x9fce67259f579e81018353f475cb334b4bb011080a913111d22be2f15a1ea90c",
        "s": "0x365f1d30e7e3c6ce2b8d86b5481bf3f0afcae9c9b90e031c3dde0aaabdcd707c"
    }
}
```
{% endcode %}
