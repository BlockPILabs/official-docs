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
curl https://linea.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0xeb96f72d00ed0831805d41c2b7bfa7305a3c088c238ceb1dbcc0aeb3fed921a9", "0x0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xeb96f72d00ed0831805d41c2b7bfa7305a3c088c238ceb1dbcc0aeb3fed921a9",
        "blockNumber": "0x24d09",
        "from": "0x713c9aa2bdc82febc3b7f0e07f8a19a99bf6e047",
        "gas": "0x13072",
        "gasPrice": "0xa0046b30",
        "maxFeePerGas": "0xa0046b34",
        "maxPriorityFeePerGas": "0xa0046b29",
        "hash": "0x1ec0aba7bbd3040a028c9f67e84c65a79008d815516edc2049e81a33c33a1bfd",
        "input": "0x1249c58b",
        "nonce": "0x2",
        "to": "0xba49765b67ba05070027297e8c6240ab7d1d10fb",
        "transactionIndex": "0x0",
        "value": "0xd12f0c4c6000",
        "type": "0x2",
        "accessList": [],
        "chainId": "0xe708",
        "v": "0x0",
        "r": "0xaa51cbb2c67c4cd83c3984c707059a193e4d24a29e760f3ec620975d5fc1541f",
        "s": "0x708b8b511b7246985e0ce2fed48199315a4c5b2de4401f1b1d85dfd482839302"
    }
}
```
{% endcode %}
