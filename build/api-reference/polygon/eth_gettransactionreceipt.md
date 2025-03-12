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
curl https://polygon.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0xdd23ad410574222090d3246a8caa3ab928e5bd09d777f4cfecd18e01ed3db5fe"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x62630cbece5d0b6791150760c1a36196bcb36f5393fe93603b7b45d818b16688",
        "blockNumber": "0x209482d",
        "contractAddress": null,
        "cumulativeGasUsed": "0xa17fdd",
        "effectiveGasPrice": "0x6fc23ac0f",
        "from": "0x30ccf7338f608f68d3d20ab878a1be5f902047df",
        "gasUsed": "0x118f9",
        "logs": [{
            "address": "0xdb46d1dc155634fbc732f92e853b10b288ad5a1d",
            "topics": ["0x22baaec4952f35f59e45bd2ddb287e1ccc6d319375770c09428eb8f8d604e065", "0x0000000000000000000000000000000000000000000000000000000000011f8c", "0x000000000000000000000000d1feccf6881970105dfb2b654054174007f0e07e"],
            "data": "0x000000000000000000000000000000000000000000000000000000006343e581",
            "blockNumber": "0x209482d",
            "transactionHash": "0xdd23ad410574222090d3246a8caa3ab928e5bd09d777f4cfecd18e01ed3db5fe",
            "transactionIndex": "0x47",
            "blockHash": "0x62630cbece5d0b6791150760c1a36196bcb36f5393fe93603b7b45d818b16688",
            "logIndex": "0x145",
            "removed": false
        }, {
            "address": "0x0000000000000000000000000000000000001010",
            "topics": ["0x4dfe1bbbcf077ddc3e01291eea2d5c70c2b422b415d95645b9adcfd678cb1d63", "0x0000000000000000000000000000000000000000000000000000000000001010", "0x00000000000000000000000030ccf7338f608f68d3d20ab878a1be5f902047df", "0x00000000000000000000000073d378cfeaa5cbe8daed64128ebdc91322aa586b"],
            "data": "0x0000000000000000000000000000000000000000000000000007aa9242d24c000000000000000000000000000000000000000000000000000fa8dbe848c044550000000000000000000000000000000000000000000002f2cdec3428d95201170000000000000000000000000000000000000000000000000fa1315605edf8550000000000000000000000000000000000000000000002f2cdf3debb1c244d17",
            "blockNumber": "0x209482d",
            "transactionHash": "0xdd23ad410574222090d3246a8caa3ab928e5bd09d777f4cfecd18e01ed3db5fe",
            "transactionIndex": "0x47",
            "blockHash": "0x62630cbece5d0b6791150760c1a36196bcb36f5393fe93603b7b45d818b16688",
            "logIndex": "0x146",
            "removed": false
        }],
        "logsBloom": "0x00000000000000000000000000000000000080000000000201400000000000000000000000000040000000000000000000008000000000000000000000000000000000000000000000000000000000800000000000000000000100000000000200000000000000000000000000000000000000000000000080100000000080000000000004020000000000000000000000010000000000000000000000000000200000000000000000000000000000000000000000000004000000000000004000000000000000000001000000000000000000000000040000100000000000008200400000000000000000000000000100000001000000000000000000100000",
        "status": "0x1",
        "to": "0xdb46d1dc155634fbc732f92e853b10b288ad5a1d",
        "transactionHash": "0xdd23ad410574222090d3246a8caa3ab928e5bd09d777f4cfecd18e01ed3db5fe",
        "transactionIndex": "0x47",
        "type": "0x2"
    }
}
```
{% endcode %}
