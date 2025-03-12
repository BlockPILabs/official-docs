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
curl https://meter.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0xdd23ad410574222090d3246a8caa3ab928e5bd09d777f4cfecd18e01ed3db5fe"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "from": "0xb9fe947d6e3c03b190df441da142127878af1343",
        "status": "0x1",
        "transactionHash": "0xa5007c001f18b75b3ff0beb5b394734fcdfcf54fac808f4fefc50fb9aa770ff7",
        "transactionIndex": "0x0",
        "blockNumber": "0x239756b",
        "blockHash": "0x0239756b04ab15911279a75860d93f3867f1de3086b840175351d4d10e2bb50d",
        "cumulativeGasUsed": "0x12650",
        "gasUsed": "0x12650",
        "contractAddress": null,
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "logs": [
            {
                "type": "mined",
                "logIndex": "0x0",
                "transactionIndex": "0x0",
                "transactionHash": "0xa5007c001f18b75b3ff0beb5b394734fcdfcf54fac808f4fefc50fb9aa770ff7",
                "blockHash": "0x0239756b04ab15911279a75860d93f3867f1de3086b840175351d4d10e2bb50d",
                "blockNumber": "0x239756b",
                "address": "0x2c3b31f752bd3bbefec6b1f0e82c47575e42db93",
                "data": "0x",
                "topics": [
                    "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                    "0x000000000000000000000000b9fe947d6e3c03b190df441da142127878af1343",
                    "0x0000000000000000000000000000000000000000000000000000000000000000",
                    "0xc000000000000000000002000000006458bb4c010000000500000000000001ef"
                ]
            },
            {
                "type": "mined",
                "logIndex": "0x1",
                "transactionIndex": "0x0",
                "transactionHash": "0xa5007c001f18b75b3ff0beb5b394734fcdfcf54fac808f4fefc50fb9aa770ff7",
                "blockHash": "0x0239756b04ab15911279a75860d93f3867f1de3086b840175351d4d10e2bb50d",
                "blockNumber": "0x239756b",
                "address": "0x2c3b31f752bd3bbefec6b1f0e82c47575e42db93",
                "data": "0x",
                "topics": [
                    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "0x000000000000000000000000b9fe947d6e3c03b190df441da142127878af1343",
                    "0x0000000000000000000000009b2461f63718cb895a3a29a4eee4f4fcb15dea88",
                    "0xc000000000000000000002000000006458bb4c010000000500000000000001ef"
                ]
            }
        ]
    },
    "id": 1
}
```
{% endcode %}
