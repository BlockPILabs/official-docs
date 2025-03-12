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
curl https://arbitrum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0xa006663075e2d95719083211d31c1c8cca5b9780833538473a2b86fb5e5c8131"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "transactionHash": "0xa006663075e2d95719083211d31c1c8cca5b9780833538473a2b86fb5e5c8131",
        "blockHash": "0x3b32dd164f1eb2b1f925c214e7180bf35280cf233a01f7e3a5d70203912e6808",
        "blockNumber": "0x27db5e2",
        "logs": [
            {
                "transactionHash": "0xa006663075e2d95719083211d31c1c8cca5b9780833538473a2b86fb5e5c8131",
                "address": "0xff970a61a04b1ca14834a43f5de4533ebddb5cc8",
                "blockHash": "0x3b32dd164f1eb2b1f925c214e7180bf35280cf233a01f7e3a5d70203912e6808",
                "blockNumber": "0x27db5e2",
                "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "logIndex": "0x0",
                "removed": false,
                "topics": [
                    "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                    "0x00000000000000000000000033259ed1f5e3cd4d740709eec9a55fbd641288a8",
                    "0x000000000000000000000000663dc15d3c1ac63ff12e45ab68fea3f0a883c251"
                ],
                "transactionIndex": "0x1"
            }
        ],
        "contractAddress": null,
        "effectiveGasPrice": "0x5f5e100",
        "cumulativeGasUsed": "0x28941",
        "from": "0x33259ed1f5e3cd4d740709eec9a55fbd641288a8",
        "gasUsed": "0x28941",
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000020001000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000200000000000000000000010000000000000000800040000000000000000000400000000000000000000",
        "status": "0x1",
        "to": "0xff970a61a04b1ca14834a43f5de4533ebddb5cc8",
        "transactionIndex": "0x1",
        "type": "0x2",
        "l1BlockNumber": "0xf526c7",
        "gasUsedForL1": "0x1f46e"
    }
}
```
{% endcode %}
