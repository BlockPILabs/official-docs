---
description: Returns block information by hash.
---

# eth\_getBlockByHash

#### **Parameters:**

**DATA , 32 Bytes** - Hash of a block.

**Boolean** - If true it returns the full transaction objects, if false only the hashes of the transactions.

#### **Returns:**

Object - A block object, or null when no block was found:

* **number: QUANTITY** - the block number.
* **hash: DATA, 32 Bytes** - hash of the block.
* **parentHash: DATA, 32 Bytes** - hash of the parent block.
* **nonce: DATA, 8 Bytes** - hash of the generated proof-of-work.
* **sha3Uncles: DATA, 32 Bytes** - SHA3 of the uncles data in the block.
* **logsBloom: DATA, 256 Bytes** - the bloom filter for the logs of the block.
* **transactionsRoot: DATA, 32 Bytes** - the root of the transaction trie of the block.
* **stateRoot: DATA, 32 Bytes** - the root of the final state trie of the block.
* **receiptsRoot: DATA, 32 Bytes** - the root of the receipts trie of the block.
* **miner: DATA, 20 Bytes** - the address of the beneficiary to whom the mining rewards were given.
* **difficulty: QUANTITY** - integer of the difficulty for this block.
* **totalDifficulty: QUANTITY** - integer of the total difficulty of the chain until this block.
* **extraData: DATA** - the “extra data” field of this block.
* **size: QUANTITY** - integer the size of this block in bytes.
* **gasLimit: QUANTITY** - the maximum gas allowed in this block.
* **gasUsed: QUANTITY** - the total used gas by all transactions in this block.
* **timestamp: QUANTITY** - the unix timestamp for when the block was collated.
* **transactions: Array** - Array of transaction objects, or 32 Bytes transaction hashes depending on the last given parameter.
* **uncles: Array** - Array of uncle hashes.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["0x9639114abbde6058f5fa4fa8c6db0a67be88bde27e37c825f47b462f716ef5cc",false],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "baseFeePerGas": "0xee6b280",
        "difficulty": "0x0",
        "extraData": "0x",
        "gasLimit": "0xffffffff",
        "gasUsed": "0x22aa64",
        "hash": "0x9639114abbde6058f5fa4fa8c6db0a67be88bde27e37c825f47b462f716ef5cc",
        "l1BatchNumber": null,
        "l1BatchTimestamp": null,
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "miner": "0x0000000000000000000000000000000000000000",
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x0000000000000000",
        "number": "0x92e869",
        "parentHash": "0x73836c8c3c1cdb110a4eeaf6a827f99a3811de1e915694d235b3e9d637b11c40",
        "receiptsRoot": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "sealFields": [],
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "size": "0x0",
        "stateRoot": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "timestamp": "0x64b0e914",
        "totalDifficulty": "0x0",
        "transactions": [
            "0x32e69225d68e2d3969776b33011c984b0ab030a71907008ff88d4757922883e2",
            "0x4dd440b8f69f1b395a245692fd5ff288d44359a0239e3a51df4bc53b7b525b6f"
        ],
        "transactionsRoot": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "uncles": []
    }
}
```
{% endcode %}
