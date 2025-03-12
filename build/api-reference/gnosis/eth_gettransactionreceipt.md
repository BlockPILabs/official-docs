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
curl https://gnosis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0x4182c1c7e7075a984c7c99af3563356128a3ecbb5848c651ae1462eb0e0f0a89"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "transactionHash": "0x4182c1c7e7075a984c7c99af3563356128a3ecbb5848c651ae1462eb0e0f0a89",
        "transactionIndex": "0x0",
        "blockHash": "0xf763dcf18ee553e1ca8bd5360d065e9ce3453383502a6a2c9dadf1646bb6a2e7",
        "blockNumber": "0x189bee7",
        "cumulativeGasUsed": "0x5208",
        "gasUsed": "0x5208",
        "effectiveGasPrice": "0xb2d05e00",
        "from": "0x72d9e579f691d62aa7e0703840db6dd2fa9fae21",
        "to": "0x33006564bb686b7635a77c3be3bceb0e50bd2eb7",
        "contractAddress": [],
        "logs": [],
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "status": "0x1",
        "type": "0x0"
    },
    "id": 1
}
```
{% endcode %}

{% hint style="info" %}
Due to the defects in the node client, the "contractAddress" is missing for full node with Websocket RPC request. If you specifically need the return of this parameter with Websocket, please enable the Archive Mode. HTTPS requests do not have this problem.&#x20;
{% endhint %}
