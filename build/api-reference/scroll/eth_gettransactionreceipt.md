---
description: >-
  Returns the receipt of a transaction by transaction hash. Note That the
  receipt is not available for pending transactions.
---

# eth\_getTransactionReceipt

#### **Parameters:**

**DATA, 32 Bytes** - hash of a transaction

#### **Returns:**

**Object** - A transaction receipt object, or null when no receipt was found:

* **transactionHash : DATA, 32 Bytes** - hash of the transaction.
* **transactionIndex: QUANTITY** - integer of the transactions index position in the block.
* **blockHash: DATA, 32 Bytes** - hash of the block where this transaction was in.
* **blockNumber: QUANTITY** - block number where this transaction was in.
* **from: DATA, 20 Bytes** - address of the sender.
* **to: DATA, 20 Bytes** - address of the receiver. null when its a contract creation transaction.
* **cumulativeGasUsed : QUANTITY** - The total amount of gas used when this transaction was executed in the block.
* **gasUsed : QUANTITY** - The amount of gas used by this specific transaction alone.
* **contractAddress : DATA, 20 Bytes** - The contract address created, if the transaction was a contract creation, otherwise null.
* **logs: Array** - Array of log objects, which this transaction generated.
* **logsBloom: DATA, 256 Bytes** - Bloom filter for light clients to quickly retrieve related logs.

It also returns either :

* **root : DATA 32 bytes** - post-transaction stateroot (pre Byzantium)
* **status: QUANTITY** - either 1 (success) or 0 (failure)

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://scroll.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0xa006663075e2d95719083211d31c1c8cca5b9780833538473a2b86fb5e5c8131"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x3d3443a85596bfa9baa32ec9ee826ccc726a34574cffe43474f1fe6a368b5b3a",
        "blockNumber": "0xe5e54",
        "contractAddress": null,
        "cumulativeGasUsed": "0xc06a",
        "effectiveGasPrice": "0x77359407",
        "from": "0x097258f96d538164c1434f4c0ff692a4cee3fe6f",
        "gasUsed": "0xc06a",
        "logs": [
            {
                "address": "0x80732890c93c6d9c6c23e06f888ed0cb88a06018",
                "topics": [
                    "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                    "0x000000000000000000000000097258f96d538164c1434f4c0ff692a4cee3fe6f",
                    "0x00000000000000000000000048235a4b7d02f5874dc82f7419cbeaeb0043ef2f"
                ],
                "data": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
                "blockNumber": "0xe5e54",
                "transactionHash": "0x7f3471705371d394ffe3627c6a7f19f6f399a6b2fa6908143dac04a42e5c04ab",
                "transactionIndex": "0x0",
                "blockHash": "0x3d3443a85596bfa9baa32ec9ee826ccc726a34574cffe43474f1fe6a368b5b3a",
                "logIndex": "0x0",
                "removed": false
            }
        ],
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000100000000000000000040000000002000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080020000000000000000000400000000000000000000000000000000000000000000000000000000000000000000010000000400000000000000000000000000000410000000000000000000000000000000000000000000000000000000000000",
        "status": "0x1",
        "to": "0x80732890c93c6d9c6c23e06f888ed0cb88a06018",
        "transactionHash": "0x7f3471705371d394ffe3627c6a7f19f6f399a6b2fa6908143dac04a42e5c04ab",
        "transactionIndex": "0x0",
        "type": "0x2"
    }
}
```
{% endcode %}
