---
description: Gets a block with extra information for a given number
---

# zkevm\_getFullBlockByNumber

**Parameters:**

**QUANTITY|TAG** - integer of a block number, or the string "latest"

**Boolean** - If true it returns the full transaction objects, if false only the hashes of the transactions.

**Returns:**

Object - A block object, or null when no block was found

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://merlin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
'{
    "jsonrpc": "2.0",
    "method": "zkevm_getFullBlockByNumber",
    "params": [
        "latest",
        true
    ],
    "id": 1
}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "parentHash": "0x3ae5f5094930b184922d37fdb9f2dc811254efb8f0d1d5267a8666886c6e0d14",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "miner": "0xf73d921aa8f2dbe77adca8466127b392ede89dc9",
        "stateRoot": "0x165f7bde13e72961dbbd92af1d34e837199b52c36835852fd148665fb4e253c0",
        "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "difficulty": "0x0",
        "totalDifficulty": "0x0",
        "size": "0x204",
        "number": "0x123df8b",
        "gasLimit": "0x4000000000000",
        "gasUsed": "0x0",
        "timestamp": "0x67b7fbbf",
        "extraData": "0x",
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x0000000000000000",
        "hash": "0x461ac8aad0edc0b732611434256696fddf640b58e3f798f4a9295d0062e58674",
        "transactions": [],
        "uncles": [],
        "globalExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "blockInfoRoot": "0xbd5d365df46fbd50f8d824baac263995d691f5b30523a142cf13373e5b725636"
    }
}
```
{% endcode %}
