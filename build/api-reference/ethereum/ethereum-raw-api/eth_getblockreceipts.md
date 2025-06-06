---
description: Get all transaction receipts for a given block on Ethereum.
---

# eth\_getBlockReceipts

#### **Parameters:**

**QUANTITY|TAG** - Block number (in hex), or one of the following block tags: 'latest', 'earliest', 'finalized', 'safe' or 'pending'.

{% hint style="info" %}
Parameter of block hash is not supported.
{% endhint %}

#### **Returns:**

**Object** - Transactions receipt object, or null when no receipt was found:

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
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"eth_getBlockReceipts","params":["latest"],"id":1,"jsonrpc":"2.0"}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {}
}
```
{% endcode %}
