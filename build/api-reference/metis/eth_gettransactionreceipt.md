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
curl https://metis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0x98affa80b5e5bcec38793376d7f61a6df1614b150e319af82d13f8d0c29ab83c"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x55eb3c6891ba58a318000bf4faaf74c0a4c09aeafdbf095ad63ab3d91d907b1a",
        "blockNumber": "0x11f4880",
        "contractAddress": null,
        "cumulativeGasUsed": "0x1d960",
        "from": "0xccd77d7c2ad41115b6dd60c2b8c87ea3b1b117ff",
        "gasUsed": "0x1d960",
        "l1Fee": "0x0",
        "l1FeeScalar": "8",
        "l1GasPrice": "0x0",
        "l1GasUsed": "0x1bc2",
        "logs": [
            {
                "address": "0xfbae1eab52af0ea3d35cb12f1221ce32d377d08e",
                "topics": [
                    "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                    "0x000000000000000000000000ccd77d7c2ad41115b6dd60c2b8c87ea3b1b117ff",
                    "0x00000000000000000000000014679d1da243b8c7d1a4c6d0523a2ce614ef027c"
                ],
                "data": "0x0000000000000000000002ac3a4edbbfb7fffffffeac3f4c16b89b94a2aa5c80",
                "blockNumber": "0x11f4880",
                "transactionHash": "0x98affa80b5e5bcec38793376d7f61a6df1614b150e319af82d13f8d0c29ab83c",
                "transactionIndex": "0x0",
                "blockHash": "0x55eb3c6891ba58a318000bf4faaf74c0a4c09aeafdbf095ad63ab3d91d907b1a",
                "logIndex": "0x0",
                "removed": false
            },
            {
                "address": "0xfbae1eab52af0ea3d35cb12f1221ce32d377d08e",
                "topics": [
                    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "0x000000000000000000000000ccd77d7c2ad41115b6dd60c2b8c87ea3b1b117ff",
                    "0x000000000000000000000000fb7deda2823115d3263472408adf3fa2d9d92e7f"
                ],
                "data": "0x00000000000000000000000000000000000000000002425cfa2a72b13e886300",
                "blockNumber": "0x11f4880",
                "transactionHash": "0x98affa80b5e5bcec38793376d7f61a6df1614b150e319af82d13f8d0c29ab83c",
                "transactionIndex": "0x0",
                "blockHash": "0x55eb3c6891ba58a318000bf4faaf74c0a4c09aeafdbf095ad63ab3d91d907b1a",
                "logIndex": "0x1",
                "removed": false
            },
            {
                "address": "0x75cb093e4d61d2a2e65d8e0bbb01de8d89b53481",
                "topics": [
                    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "0x000000000000000000000000fb7deda2823115d3263472408adf3fa2d9d92e7f",
                    "0x00000000000000000000000014679d1da243b8c7d1a4c6d0523a2ce614ef027c"
                ],
                "data": "0x0000000000000000000000000000000000000000000000001d6ce9b2d7b5d112",
                "blockNumber": "0x11f4880",
                "transactionHash": "0x98affa80b5e5bcec38793376d7f61a6df1614b150e319af82d13f8d0c29ab83c",
                "transactionIndex": "0x0",
                "blockHash": "0x55eb3c6891ba58a318000bf4faaf74c0a4c09aeafdbf095ad63ab3d91d907b1a",
                "logIndex": "0x2",
                "removed": false
            },
            {
                "address": "0xfb7deda2823115d3263472408adf3fa2d9d92e7f",
                "topics": [
                    "0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1"
                ],
                "data": "0x0000000000000000000000000000000000000000000000d59203c6cf6fa1415200000000000000000000000000000000000000001063d4ebde81b302c3480748",
                "blockNumber": "0x11f4880",
                "transactionHash": "0x98affa80b5e5bcec38793376d7f61a6df1614b150e319af82d13f8d0c29ab83c",
                "transactionIndex": "0x0",
                "blockHash": "0x55eb3c6891ba58a318000bf4faaf74c0a4c09aeafdbf095ad63ab3d91d907b1a",
                "logIndex": "0x3",
                "removed": false
            },
            {
                "address": "0xfb7deda2823115d3263472408adf3fa2d9d92e7f",
                "topics": [
                    "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822",
                    "0x00000000000000000000000014679d1da243b8c7d1a4c6d0523a2ce614ef027c",
                    "0x00000000000000000000000014679d1da243b8c7d1a4c6d0523a2ce614ef027c"
                ],
                "data": "0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002425cfa2a72b13e8863000000000000000000000000000000000000000000000000001d6ce9b2d7b5d1120000000000000000000000000000000000000000000000000000000000000000",
                "blockNumber": "0x11f4880",
                "transactionHash": "0x98affa80b5e5bcec38793376d7f61a6df1614b150e319af82d13f8d0c29ab83c",
                "transactionIndex": "0x0",
                "blockHash": "0x55eb3c6891ba58a318000bf4faaf74c0a4c09aeafdbf095ad63ab3d91d907b1a",
                "logIndex": "0x4",
                "removed": false
            },
            {
                "address": "0x75cb093e4d61d2a2e65d8e0bbb01de8d89b53481",
                "topics": [
                    "0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65",
                    "0x00000000000000000000000014679d1da243b8c7d1a4c6d0523a2ce614ef027c"
                ],
                "data": "0x0000000000000000000000000000000000000000000000001d6ce9b2d7b5d112",
                "blockNumber": "0x11f4880",
                "transactionHash": "0x98affa80b5e5bcec38793376d7f61a6df1614b150e319af82d13f8d0c29ab83c",
                "transactionIndex": "0x0",
                "blockHash": "0x55eb3c6891ba58a318000bf4faaf74c0a4c09aeafdbf095ad63ab3d91d907b1a",
                "logIndex": "0x5",
                "removed": false
            }
        ],
        "logsBloom": "0x00200000000000000000000080000020000000000000000000000000000004000000000000000000000004000210000000000000000000000000000000200000000000000000000008000008000000200000000000400000000000000000000000000020000000008000000000000008000000000000040000000010000000000002000000000000000000000000000040000000000040080000004100000000020000000000024000000000000000000000000000000000000000000000000000000002000000000000000000000000020000000000001000040002000000000010000004000000000000000000000000000000000000000000000000000000",
        "status": "0x1",
        "to": "0x14679d1da243b8c7d1a4c6d0523a2ce614ef027c",
        "transactionHash": "0x98affa80b5e5bcec38793376d7f61a6df1614b150e319af82d13f8d0c29ab83c",
        "transactionIndex": "0x0"
    }
}
```
{% endcode %}
