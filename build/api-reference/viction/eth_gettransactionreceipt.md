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
curl https://viction.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0xe989f85cd3f4ff61c7b687e74609702773d7eac3f10fea2433cd875e9d89ab5c"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x744a3dac0d390c212fbc318972bc9200d8c9aff01ae4f063634343457d30fbc9",
        "blockNumber": "0x41b123f",
        "contractAddress": null,
        "cumulativeGasUsed": "0x0",
        "from": "0x806d90e6087cee9288e7beda6294fd0138b5897a",
        "gasUsed": "0x0",
        "logs": [
            {
                "address": "0x0000000000000000000000000000000000000092",
                "topics": [],
                "data": "0x",
                "blockNumber": "0x41b123f",
                "transactionHash": "0xe989f85cd3f4ff61c7b687e74609702773d7eac3f10fea2433cd875e9d89ab5c",
                "transactionIndex": "0x0",
                "blockHash": "0x07e2de8f275e44e24859841526ee7cff0d7356ffa7acf876747be09b3f4d5540",
                "logIndex": "0x0",
                "removed": false
            }
        ],
        "logsBloom": "0x01000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000",
        "status": "0x1",
        "to": "0x0000000000000000000000000000000000000092",
        "transactionHash": "0xe989f85cd3f4ff61c7b687e74609702773d7eac3f10fea2433cd875e9d89ab5c",
        "transactionIndex": "0x0"
    }
}
```
{% endcode %}
