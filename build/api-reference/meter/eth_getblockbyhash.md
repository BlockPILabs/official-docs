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
curl https://meter.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["0x0239748ee2ba3c1802497f88a792123a58b1a6ba57129c0b8bc47ffc4ae9101c",false],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "number": "0x239748e",
        "hash": "0x0239748ee2ba3c1802497f88a792123a58b1a6ba57129c0b8bc47ffc4ae9101c",
        "size": "0x312",
        "parentHash": "0x0239748d392c0cd248bf40a519e815eb4b3b1b4483b4332959c42d7df637f469",
        "timestamp": "0x645aff44",
        "gasLimit": "0xbebc200",
        "beneficiary": "0x56d5e48a27ad442a02201150e4dfb134d7bf618d",
        "gasUsed": "0x0",
        "totalScore": "0x239748e",
        "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "txsFeatures": 0,
        "stateRoot": "0xa3979e001624ec29da691fa69a78a115e6d0dd8fb9ebc94242f070e57fca4c84",
        "receiptsRoot": "0x45b0cfc220ceec5b7c1c62c4d4193d38e4eba48e8815729ce75f9c0ab0e4c1c0",
        "miner": "0x60611436fe66d68476a7139e05717fb8ecaa8743",
        "isTrunk": true,
        "isKBlock": false,
        "lastKBlockHeight": 37318651,
        "nonce": "0x0000000000000000",
        "epoch": 23745,
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "transactions": [],
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "difficulty": "0x0",
        "extraData": "0x",
        "baseFeePerGas": "0x746a528800"
    },
    "id": 1
}
```
{% endcode %}
