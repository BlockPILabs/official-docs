---
description: Returns block information by number.
---

# eth\_getBlockByNumber

#### **Parameters:**

**QUANTITY|TAG** - integer of a block number, or the string "latest"

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
curl  https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest", true],"id":1}'

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
            {
                "blockHash": "0x9639114abbde6058f5fa4fa8c6db0a67be88bde27e37c825f47b462f716ef5cc",
                "blockNumber": "0x92e869",
                "chainId": "0x118",
                "from": "0xcb6f7e93f0fcbadee2fe746001eab7107069c1fe",
                "gas": "0x1c9c380",
                "gasPrice": "0xee6b280",
                "hash": "0x32e69225d68e2d3969776b33011c984b0ab030a71907008ff88d4757922883e2",
                "input": "0xbb2cd72800000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000100000000000000000000000020b28b1e4665fff290650586ad76e977eab90c5d00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000002ecb1f7bac",
                "maxFeePerGas": "0x77359400",
                "maxPriorityFeePerGas": "0x77359400",
                "nonce": "0xd867c",
                "r": "0xcdd1147205d06b432f165fb76ee1020d35ee153f7ac1b75372dd5641e6bfc35b",
                "s": "0x547271a525a171225f6407e77717a123201f800ee6d142eb582e8e83c1616e43",
                "to": "0x01767c7f08e2ac33df97cb74e80bbd184058c8cc",
                "transactionIndex": "0x0",
                "type": "0x0",
                "v": "0x0",
                "value": "0x0"
            },
            {
                "blockHash": "0x9639114abbde6058f5fa4fa8c6db0a67be88bde27e37c825f47b462f716ef5cc",
                "blockNumber": "0x92e869",
                "chainId": "0x118",
                "from": "0xcb6f7e93f0fcbadee2fe746001eab7107069c1fe",
                "gas": "0x1c9c380",
                "gasPrice": "0xee6b280",
                "hash": "0x4dd440b8f69f1b395a245692fd5ff288d44359a0239e3a51df4bc53b7b525b6f",
                "input": "0xbb2cd72800000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000100000000000000000000000020b28b1e4665fff290650586ad76e977eab90c5d00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000002ecb1f7bac",
                "maxFeePerGas": "0x77359400",
                "maxPriorityFeePerGas": "0x77359400",
                "nonce": "0xd867d",
                "r": "0x42524dcec547179e45c5768f69e3905a048af08ba7932e7e15560fc875b66354",
                "s": "0x3bb0249dcd5fb4ef73443e93d3a0f726019f6e2ca53ebd5ac5c19abbb1707b79",
                "to": "0x01767c7f08e2ac33df97cb74e80bbd184058c8cc",
                "transactionIndex": "0x1",
                "type": "0x0",
                "v": "0x0",
                "value": "0x0"
            }
        ],
        "transactionsRoot": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "uncles": []
    }
}
```
{% endcode %}
