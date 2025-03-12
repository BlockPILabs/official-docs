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
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0x8bd46aa04770b3c0e1b0b3631bd340068ffb8a840dfc3f7ae407439193830a01"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "transactionHash": "0x8bd46aa04770b3c0e1b0b3631bd340068ffb8a840dfc3f7ae407439193830a01",
        "blockHash": "0x50abcc4ff596bf57cef3cba2687b8429630e80b5912f4d8237b462964c5369d0",
        "blockNumber": "0x2b65895",
        "logs": [
            {
                "transactionHash": "0x8bd46aa04770b3c0e1b0b3631bd340068ffb8a840dfc3f7ae407439193830a01",
                "address": "0x67c10c397dd0ba417329543c1a40eb48aaa7cd00",
                "blockHash": "0x50abcc4ff596bf57cef3cba2687b8429630e80b5912f4d8237b462964c5369d0",
                "blockNumber": "0x2b65895",
                "data": "0x0000000000000000000000000000000000000000000000007a1b6de237e5e8c9",
                "logIndex": "0x0",
                "removed": false,
                "topics": [
                    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "0x000000000000000000000000f44938b0125a6662f9536281ad2cd6c499f22004",
                    "0x00000000000000000000000017281460228691b044e080a5f5257dce8e47f79c"
                ],
                "transactionIndex": "0x0"
            },
            {
                "transactionHash": "0x8bd46aa04770b3c0e1b0b3631bd340068ffb8a840dfc3f7ae407439193830a01",
                "address": "0x7f5c764cbc14f9669b88837ca1490cca17c31607",
                "blockHash": "0x50abcc4ff596bf57cef3cba2687b8429630e80b5912f4d8237b462964c5369d0",
                "blockNumber": "0x2b65895",
                "data": "0x0000000000000000000000000000000000000000000000000000000000c8d029",
                "logIndex": "0x1",
                "removed": false,
                "topics": [
                    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "0x000000000000000000000000f44938b0125a6662f9536281ad2cd6c499f22004",
                    "0x00000000000000000000000017281460228691b044e080a5f5257dce8e47f79c"
                ],
                "transactionIndex": "0x0"
            },
            {
                "transactionHash": "0x8bd46aa04770b3c0e1b0b3631bd340068ffb8a840dfc3f7ae407439193830a01",
                "address": "0x2c6d91accc5aa38c84653f28a80aec69325bdd12",
                "blockHash": "0x50abcc4ff596bf57cef3cba2687b8429630e80b5912f4d8237b462964c5369d0",
                "blockNumber": "0x2b65895",
                "data": "0xfffffffffffffffffffffffffffffffffffffffffffffffecfe87f04c1d61e6b",
                "logIndex": "0x2",
                "removed": false,
                "topics": [
                    "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                    "0x00000000000000000000000017281460228691b044e080a5f5257dce8e47f79c",
                    "0x000000000000000000000000f44938b0125a6662f9536281ad2cd6c499f22004"
                ],
                "transactionIndex": "0x0"
            },
            {
                "transactionHash": "0x8bd46aa04770b3c0e1b0b3631bd340068ffb8a840dfc3f7ae407439193830a01",
                "address": "0x2c6d91accc5aa38c84653f28a80aec69325bdd12",
                "blockHash": "0x50abcc4ff596bf57cef3cba2687b8429630e80b5912f4d8237b462964c5369d0",
                "blockNumber": "0x2b65895",
                "data": "0x000000000000000000000000000000000000000000000001301780fb3e29e194",
                "logIndex": "0x3",
                "removed": false,
                "topics": [
                    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "0x00000000000000000000000017281460228691b044e080a5f5257dce8e47f79c",
                    "0x0000000000000000000000000000000000000000000000000000000000000000"
                ],
                "transactionIndex": "0x0"
            },
            {
                "transactionHash": "0x8bd46aa04770b3c0e1b0b3631bd340068ffb8a840dfc3f7ae407439193830a01",
                "address": "0xf44938b0125a6662f9536281ad2cd6c499f22004",
                "blockHash": "0x50abcc4ff596bf57cef3cba2687b8429630e80b5912f4d8237b462964c5369d0",
                "blockNumber": "0x2b65895",
                "data": "0x000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000002c12683cd08766b92a40e00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000007a1b6de237e5e8c90000000000000000000000000000000000000000000000000000000000c8d029",
                "logIndex": "0x4",
                "removed": false,
                "topics": [
                    "0x88d38ed598fdd809c2bf01ee49cd24b7fdabf379a83d29567952b60324d58cef",
                    "0x00000000000000000000000017281460228691b044e080a5f5257dce8e47f79c"
                ],
                "transactionIndex": "0x0"
            }
        ],
        "contractAddress": null,
        "cumulativeGasUsed": "0x22c06",
        "from": "0x17281460228691b044e080a5f5257dce8e47f79c",
        "gasUsed": "0x22c06",
        "logsBloom": "0x00000000000000000000008000000000000000000000000000000000000000000000000000000000000000000000000000000040008000000000000000200800000000000000000000000008010000000000040000000000000000000000000000000200020000000000000000000800010000000000000800000010000010000001000002000000000000000080000000000000000000000000000000000000120001000000000000000000000000000002000000000000000000000000000000080006000000000000000000000000000000000000000000000000000020000010000000000000000000000000000100000000000000008000000000010000",
        "status": "0x1",
        "to": "0xf44938b0125a6662f9536281ad2cd6c499f22004",
        "transactionIndex": "0x0",
        "l1Fee": "0x33931b320a2c",
        "l1FeeScalar": "1",
        "l1GasPrice": "0x2b2ec481d",
        "l1GasUsed": "0x131c"
    }
}
```
{% endcode %}
