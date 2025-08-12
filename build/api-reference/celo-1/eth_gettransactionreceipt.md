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
curl https://flow-evm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0xbd9aa0d6fe973743632e8db8e37d5c92787610a61e1c020881955bb8129a4917"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xff63ea7998b11170179aeb65dad9b137a36dea2a99bd97999cc2eee4ccbf0efc",
        "blockNumber": "0x1aef73c",
        "contractAddress": null,
        "cumulativeGasUsed": "0x16303b",
        "effectiveGasPrice": "0x106af3bcc0",
        "from": "0x4403cbfae2b4571718b4d2e43ba7efaa9086e6be",
        "gasUsed": "0x761b6",
        "logs": [],
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "status": "0x0",
        "to": "0xe2ef41a93dab1878310e81617da47995f6ec01fe",
        "transactionHash": "0xbd9aa0d6fe973743632e8db8e37d5c92787610a61e1c020881955bb8129a4917",
        "transactionIndex": "0x1",
        "type": "0x0"
    }
}
```
{% endcode %}
