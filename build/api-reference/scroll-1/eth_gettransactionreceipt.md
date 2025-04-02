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
curl https://scroll.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0x13699866bbf3ee49a65dfa0258c1179786b57f833da2c7ad9c3ef1f2f596afba"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x8a7c32a1810f6b940bb46aa0c569d3c0f01a6e5fbb2d9f471cb2124b5eccea29",
        "blockNumber": "0x311ace",
        "contractAddress": null,
        "cumulativeGasUsed": "0x0",
        "effectiveGasPrice": "0x989680",
        "from": "0x00000000000000000000000000000000000a4b05",
        "gasUsed": "0x0",
        "gasUsedForL1": "0x0",
        "l1BlockNumber": "0x7a8f91",
        "logs": [],
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "status": "0x1",
        "to": "0x00000000000000000000000000000000000a4b05",
        "transactionHash": "0x13699866bbf3ee49a65dfa0258c1179786b57f833da2c7ad9c3ef1f2f596afba",
        "transactionIndex": "0x0",
        "type": "0x6a"
    }
}
```
{% endcode %}
