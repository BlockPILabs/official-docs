---
description: Gets a block with extra information for a given hash
---

# zkevm\_getFullBlockByHash

**Parameters:**

**DATA , 32 Bytes** - Hash of a block.

**Boolean** - If true it returns the full transaction objects, if false only the hashes of the transactions.

**Returns:**

Object - A block object, or null when no block was found

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://merlin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
{
    "jsonrpc": "2.0",
    "method": "zkevm_getFullBlockByHash",
    "params": [
        "0x11af5461a3d1cbaa19ddcfdafee335b5a96995c54610392cddbcdb4630be21a5",
        true
    ],
    "id": 1
}

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "parentHash": "0x52ccc4feb099f49d4bdcbcb2b09d04143fafe6d8b3e2a28e95c2af12ccb2a43b",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "miner": "0xf73d921aa8f2dbe77adca8466127b392ede89dc9",
        "stateRoot": "0x42bbd50e08aae31466e6819c5cae2da983e6bd1a980cf4fbe540a5d92b37f184",
        "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "difficulty": "0x0",
        "totalDifficulty": "0x0",
        "size": "0x204",
        "number": "0x123dcaa",
        "gasLimit": "0x4000000000000",
        "gasUsed": "0x0",
        "timestamp": "0x67b7f2e6",
        "extraData": "0x",
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x0000000000000000",
        "hash": "0x11af5461a3d1cbaa19ddcfdafee335b5a96995c54610392cddbcdb4630be21a5",
        "transactions": [],
        "uncles": [],
        "globalExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "blockInfoRoot": "0x85182894a4e0a1942bdc589c5e7e71d59b6b56b2cc8aafa1155ef5f34b41ea86"
    }
}
```
{% endcode %}
