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
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0x32e69225d68e2d3969776b33011c984b0ab030a71907008ff88d4757922883e2"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x9639114abbde6058f5fa4fa8c6db0a67be88bde27e37c825f47b462f716ef5cc",
        "blockNumber": "0x92e869",
        "contractAddress": null,
        "cumulativeGasUsed": "0x0",
        "effectiveGasPrice": "0xee6b280",
        "from": "0xcb6f7e93f0fcbadee2fe746001eab7107069c1fe",
        "gasUsed": "0x115532",
        "l1BatchNumber": "0x1d4f2",
        "l1BatchTxIndex": "0x5f",
        "l2ToL1Logs": [],
        "logs": [
            {
                "address": "0x000000000000000000000000000000000000800a",
                "blockHash": "0x9639114abbde6058f5fa4fa8c6db0a67be88bde27e37c825f47b462f716ef5cc",
                "blockNumber": "0x92e869",
                "data": "0x00000000000000000000000000000000000000000000000000d529ae9e860000",
                "l1BatchNumber": "0x1d4f2",
                "logIndex": "0x0",
                "logType": null,
                "removed": false,
                "topics": [
                    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "0x000000000000000000000000cb6f7e93f0fcbadee2fe746001eab7107069c1fe",
                    "0x0000000000000000000000000000000000000000000000000000000000008001"
                ],
                "transactionHash": "0x32e69225d68e2d3969776b33011c984b0ab030a71907008ff88d4757922883e2",
                "transactionIndex": "0x0",
                "transactionLogIndex": "0x0"
            },
            {
                "address": "0x000000000000000000000000000000000000800a",
                "blockHash": "0x9639114abbde6058f5fa4fa8c6db0a67be88bde27e37c825f47b462f716ef5cc",
                "blockNumber": "0x92e869",
                "data": "0x00000000000000000000000000000000000000000000000000ba8478cab54000",
                "l1BatchNumber": "0x1d4f2",
                "logIndex": "0x1",
                "logType": null,
                "removed": false,
                "topics": [
                    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "0x0000000000000000000000000000000000000000000000000000000000008001",
                    "0x000000000000000000000000cb6f7e93f0fcbadee2fe746001eab7107069c1fe"
                ],
                "transactionHash": "0x32e69225d68e2d3969776b33011c984b0ab030a71907008ff88d4757922883e2",
                "transactionIndex": "0x0",
                "transactionLogIndex": "0x1"
            },
            {
                "address": "0x000000000000000000000000000000000000800a",
                "blockHash": "0x9639114abbde6058f5fa4fa8c6db0a67be88bde27e37c825f47b462f716ef5cc",
                "blockNumber": "0x92e869",
                "data": "0x0000000000000000000000000000000000000000000000000019a2ee76fd6300",
                "l1BatchNumber": "0x1d4f2",
                "logIndex": "0x2",
                "logType": null,
                "removed": false,
                "topics": [
                    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "0x0000000000000000000000000000000000000000000000000000000000008001",
                    "0x000000000000000000000000cb6f7e93f0fcbadee2fe746001eab7107069c1fe"
                ],
                "transactionHash": "0x32e69225d68e2d3969776b33011c984b0ab030a71907008ff88d4757922883e2",
                "transactionIndex": "0x0",
                "transactionLogIndex": "0x2"
            }
        ],
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "root": "0x9639114abbde6058f5fa4fa8c6db0a67be88bde27e37c825f47b462f716ef5cc",
        "status": "0x1",
        "to": "0x01767c7f08e2ac33df97cb74e80bbd184058c8cc",
        "transactionHash": "0x32e69225d68e2d3969776b33011c984b0ab030a71907008ff88d4757922883e2",
        "transactionIndex": "0x0",
        "type": "0x0"
    }
}
```
{% endcode %}
