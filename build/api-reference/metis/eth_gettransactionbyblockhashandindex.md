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
curl https://metis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0xb0586d80b2e552299c5134437f51249a0fcbacb0cc37250f26e22a96aa64c333", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xb0586d80b2e552299c5134437f51249a0fcbacb0cc37250f26e22a96aa64c333",
        "blockNumber": "0x11f4898",
        "from": "0x831503c817053d9769444013d4742779347104a8",
        "gas": "0x5208",
        "gasPrice": "0x4c53d546",
        "hash": "0x5b2e1b2f2822e96cdfeb2103443fef2a7de8794eabe94b44c842bfcc7010431d",
        "input": "0x",
        "nonce": "0x26bd",
        "to": "0x4e001b8900a4db6b22106ebe416cd54eba068009",
        "transactionIndex": "0x0",
        "value": "0x1c6bf526340000",
        "v": "0x8a4",
        "r": "0x907e12fe5b1d2954c78e5a1a3ec334110de9f886712ded336f5be020b6916c29",
        "s": "0xcf0a798a7af9991a0a848d5e9d3593fa45ade27faa0e5fc41ec5d4efbce60cd",
        "queueOrigin": "sequencer",
        "l1TxOrigin": "0x0000000000000000000000000000000000000000",
        "l1BlockNumber": "0x1417b63",
        "l1Timestamp": "0x672058a6",
        "index": "0x11f4897",
        "queueIndex": "0x0",
        "rawTransaction": "0xf86e8226bd844c53d546825208944e001b8900a4db6b22106ebe416cd54eba068009871c6bf526340000808208a4a0907e12fe5b1d2954c78e5a1a3ec334110de9f886712ded336f5be020b6916c29a00cf0a798a7af9991a0a848d5e9d3593fa45ade27faa0e5fc41ec5d4efbce60cd",
        "seqR": "0x4b0a81dbf348f8aeecec9e466a2be684ba6eac0ec29f9e753ad4bdb77e909823",
        "seqS": "0x3a560f5ef2cce68c550fda5bd264504acfe44a8600e760e575d5bc094b957bc1",
        "seqV": "0x1"
    }
}
```
{% endcode %}
