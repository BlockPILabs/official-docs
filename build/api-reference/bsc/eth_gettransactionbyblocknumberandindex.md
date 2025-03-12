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
curl https://bsc.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["0xF2F8D7", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xd6eec8bd479ca3541259493142d7cafaa94aabd9f9d262db6b214eaf25f96bb3",
        "blockNumber": "0xf2f8d7",
        "from": "0xf9a416fdead4a9b7c32eb9d452f8e3428651cf99",
        "gas": "0x8d07",
        "gasPrice": "0x9ac710594",
        "hash": "0x3cf5cd0e9c45681a868555cfb02b7323e6413df46b1baf75ff13de7aff6dbfbe",
        "input": "0xa9059cbb000000000000000000000000f866a2c5e1fa90228f17cdc75bf80138eb5b505c00000000000000000000000000000000000000000000000000588747b5057800",
        "nonce": "0xeb7d",
        "to": "0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x0",
        "chainId": "0x38",
        "v": "0x94",
        "r": "0xa64262f14a2db5db7a56114faa40bfcc47568612cd19710d64c220e04494fb18",
        "s": "0x7b6c5090853004f918e3988444e34632951cec9dcb5491fa8c6ebe414d6c1075"
    }
}
```
{% endcode %}
