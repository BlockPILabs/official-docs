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
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0xdd23ad410574222090d3246a8caa3ab928e5bd09d777f4cfecd18e01ed3db5fe"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0xa8d01d6d5e70cb3bd8cd423eaa11714b89adef041141e4ca31bcdc6879543b23",
        "blockNumber": "0xf2f8d7",
        "contractAddress": null,
        "cumulativeGasUsed": "0x2320e",
        "effectiveGasPrice": "0x38d12211e",
        "from": "0x255ed4ae17eff35923cfde87ed6ce81c4ebf8888",
        "gasUsed": "0x2320e",
        "logs": [{
            "address":"0xdac17f958d2ee523a2206206994597c13d831ec7",
            "topics":["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef","0x00000000000000000000000011b815efb8f581194ae79006d24e0d814b7697f6","0x000000000000000000000000703b120f15ab77b986a24c6f9262364d02f9432f"],
            "data":"0x0000000000000000000000000000000000000000000000000000000032394ffc",
            "blockNumber":"0xf2f8d7",
            "transactionHash":"0x4878fb96953eea6db8dee22787214b51fa875a2dbc9fef8984602c60f39f10b6",
            "transactionIndex":"0x0",
            "blockHash":"0xa8d01d6d5e70cb3bd8cd423eaa11714b89adef041141e4ca31bcdc6879543b23",
            "logIndex":"0x0",
            "removed":false
        },{
            "address":"0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "topics":["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef","0x000000000000000000000000703b120f15ab77b986a24c6f9262364d02f9432f","0x00000000000000000000000038a868000000a600a300867c596d400d79970500"],
            "data":"0x00000000000000000000000000000000000000000000000007e5d1a3df71d7a7",
            "blockNumber":"0xf2f8d7",
            "transactionHash":"0x4878fb96953eea6db8dee22787214b51fa875a2dbc9fef8984602c60f39f10b6",
            "transactionIndex":"0x0",
            "blockHash":"0xa8d01d6d5e70cb3bd8cd423eaa11714b89adef041141e4ca31bcdc6879543b23",
            "logIndex":"0x1",
            "removed":false
        },
        ....
        {
            "address":"0x11b815efb8f581194ae79006d24e0d814b7697f6",
            "topics":["0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67","0x00000000000000000000000038a868000000a600a300867c596d400d79970500","0x000000000000000000000000703b120f15ab77b986a24c6f9262364d02f9432f"],
            "data":"0x00000000000000000000000000000000000000000000000007f0fe144fa826e0ffffffffffffffffffffffffffffffffffffffffffffffffffffffffcdc6b0040000000000000000000000000000000000000000000283f36a13a504219c2a9c000000000000000000000000000000000000000000000000159631ad74a3a0a6fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffce597",
            "blockNumber":"0xf2f8d7",
            "transactionHash":"0x4878fb96953eea6db8dee22787214b51fa875a2dbc9fef8984602c60f39f10b6",
            "transactionIndex":"0x0",
            "blockHash":"0xa8d01d6d5e70cb3bd8cd423eaa11714b89adef041141e4ca31bcdc6879543b23",
            "logIndex":"0x5",
            "removed":false
        }],
        "logsBloom": "0x00200000000000000000000080200000000080000000000000000000000000000000000000000000000000000000010002000000080020000000000000000000000000000000000808000008000000200000000000000000020010000800000800000000000000000000000000000000000000000000000000000090000800000000000000000000000000000000000000000400000000080400004000100000000000000000000000000080000000000000000000000000000004000000000000000002000000000000000000000000000000000000001000000000200004000000200000000000000000000000000000000000000000000008001000000000",
        "status": "0x1",
        "to": "0x38a868000000a600a300867c596d400d79970500",
        "transactionHash": "0x4878fb96953eea6db8dee22787214b51fa875a2dbc9fef8984602c60f39f10b6",
        "transactionIndex": "0x0",
        "type": "0x2"
    }
}
```
{% endcode %}
