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
curl https://gnosis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["latest", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "hash": "0x1796fd0b42ca7f2e13dfaf3dd2e6c2f9eb8af86e34587849b716b65da08c33cb",
        "nonce": "0x1e273",
        "blockHash": "0x42457ab4c7496120303b37078d056d9292b5801345bb0c93bd0e48256286bd73",
        "blockNumber": "0x189bf3e",
        "transactionIndex": "0x0",
        "from": "0xacde7dbabc00fe8c578bdbf15c8a56bdca7e797a",
        "to": "0x4fe6a9e47db94a9b2a4ffede8db1602fd1fdd37d",
        "value": "0x0",
        "gasPrice": "0xb2d05e00",
        "maxPriorityFeePerGas": "0xb2d05e00",
        "maxFeePerGas": "0xb2d05e00",
        "gas": "0x68460",
        "data": "0xa0cd403a000000000000000000000000000000000000000000000000066c9af310dc329f0000000000000000000000000000000000000000000000000000000000001e26",
        "input": "0xa0cd403a000000000000000000000000000000000000000000000000066c9af310dc329f0000000000000000000000000000000000000000000000000000000000001e26",
        "chainId": "0x64",
        "type": "0x2",
        "v": "0x1",
        "s": "0x547c008f499afb5fc25c9f8f5863d2ff28a128ecae0e56cabb4d91664e7fffb3",
        "r": "0xe4c55e9b5e73cbc1e301b795ae331b2da4a6bf67c962d2f0c6c3a46e9d5416f0",
        "yParity": "0x1"
    },
    "id": 1
}
```
{% endcode %}
