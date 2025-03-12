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
curl https://scroll.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xa006663075e2d95719083211d31c1c8cca5b9780833538473a2b86fb5e5c8131"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x3d3443a85596bfa9baa32ec9ee826ccc726a34574cffe43474f1fe6a368b5b3a",
        "blockNumber": "0xe5e54",
        "from": "0x097258f96d538164c1434f4c0ff692a4cee3fe6f",
        "gas": "0xc1cd",
        "gasPrice": "0x77359407",
        "maxFeePerGas": "0x77359408",
        "maxPriorityFeePerGas": "0x77359400",
        "hash": "0x7f3471705371d394ffe3627c6a7f19f6f399a6b2fa6908143dac04a42e5c04ab",
        "input": "0x095ea7b300000000000000000000000048235a4b7d02f5874dc82f7419cbeaeb0043ef2fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
        "nonce": "0x1",
        "to": "0x80732890c93c6d9c6c23e06f888ed0cb88a06018",
        "transactionIndex": "0x0",
        "value": "0x0",
        "type": "0x2",
        "accessList": [],
        "chainId": "0x82752",
        "v": "0x1",
        "r": "0x89df90d8afd9f275759d588b1cbd05326d8919887ee30c664ea8e3e0dc5d3cb4",
        "s": "0x63d3021ed4f030060cf4ed538ee72fd4424f2ac44a5368509786b3734da37f5d"
    }
}
```
{% endcode %}
