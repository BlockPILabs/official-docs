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
curl https://artela-testnet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0x18ae964b3ee99d0beaa22ab7549e817aba57281d461a2f615ec541645db3a95c"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xf0aa3d4d32ae75a1f3433f22a703c4be762475eb2b1822ec71573ff360bb5799",
        "blockNumber": "0x709587",
        "contractAddress": null,
        "cumulativeGasUsed": "0x55e8",
        "effectiveGasPrice": "0x59682f07",
        "from": "0x1c3b7c3f965863cc97b253e1aaef315309923018",
        "gasUsed": "0x55e8",
        "logs": [],
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "status": "0x1",
        "to": "0x1c3b7c3f965863cc97b253e1aaef315309923018",
        "transactionHash": "0x18ae964b3ee99d0beaa22ab7549e817aba57281d461a2f615ec541645db3a95c",
        "transactionIndex": "0x0",
        "type": "0x2"
    }
}
```
{% endcode %}
