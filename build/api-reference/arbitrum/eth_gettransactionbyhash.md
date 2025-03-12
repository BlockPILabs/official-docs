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
curl https://arbitrum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xa006663075e2d95719083211d31c1c8cca5b9780833538473a2b86fb5e5c8131"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x3b32dd164f1eb2b1f925c214e7180bf35280cf233a01f7e3a5d70203912e6808",
        "blockNumber": "0x27db5e2",
        "hash": "0xa006663075e2d95719083211d31c1c8cca5b9780833538473a2b86fb5e5c8131",
        "accessList": [],
        "chainId": "0xa4b1",
        "from": "0x33259ed1f5e3cd4d740709eec9a55fbd641288a8",
        "gas": "0x329af",
        "gasPrice": "0x5f5e100",
        "input": "0x095ea7b3000000000000000000000000663dc15d3c1ac63ff12e45ab68fea3f0a883c2510000000000000000000000000000000000000000000000000000000000000000",
        "maxFeePerGas": "0x80befc0",
        "maxPriorityFeePerGas": "0x0",
        "nonce": "0xf0",
        "r": "0xfed2dbf20fd4f5d195aa7012bc971592abc5b3b892b2267c14a2b68a7d226555",
        "s": "0xf53f58c6c797eab41c434a097d8fe7dfc921a3297c1c869484058618aa23ac4",
        "to": "0xff970a61a04b1ca14834a43f5de4533ebddb5cc8",
        "transactionIndex": "0x1",
        "type": "0x2",
        "v": "0x1",
        "value": "0x0"
    }
}
```
{% endcode %}
