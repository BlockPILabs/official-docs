---
description: Returns the information about a transaction requested by transaction hash.
---

# eth\_getTransactionByHash

#### **Parameters:**

**DATA, 32 Bytes** - hash of a transaction

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
curl https://gnosis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0x4182c1c7e7075a984c7c99af3563356128a3ecbb5848c651ae1462eb0e0f0a89"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "hash": "0x4182c1c7e7075a984c7c99af3563356128a3ecbb5848c651ae1462eb0e0f0a89",
        "nonce": "0x1f0047",
        "blockHash": "0xf763dcf18ee553e1ca8bd5360d065e9ce3453383502a6a2c9dadf1646bb6a2e7",
        "blockNumber": "0x189bee7",
        "transactionIndex": "0x0",
        "from": "0x72d9e579f691d62aa7e0703840db6dd2fa9fae21",
        "to": "0x33006564bb686b7635a77c3be3bceb0e50bd2eb7",
        "value": "0x5404be191810c00",
        "gasPrice": "0xb2d05e00",
        "gas": "0x5208",
        "data": "0x",
        "input": "0x",
        "type": "0x0",
        "v": "0xec",
        "s": "0x2229fac1939a581d4b24d1a7cd07233d52733fe9a5fa21b04f89edd1f0f7a626",
        "r": "0xd8458ab0f7f9608731fe025e26bd632e27800ee463b81ffb7f5b6d10d7689cfa"
    },
    "id": 1
}
```
{% endcode %}
