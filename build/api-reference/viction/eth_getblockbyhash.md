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
curl https://viction.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["0x934939ecbe2e632be985bf07a160414c5ba54f3bed20edbb43497315f1f2fef2",false],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "difficulty": "0x69",
        "extraData": "0xd88302030084746f6d6f88676f312e31372e33856c696e757800000000000000b1d7e6fd0b7b27227e95161a944f187ca6ff75cd2188ce09e6d9a81eec973e442d728c83466351e455cc6163fa8aad30b1421d17f4e74d234feca0f7155fc61900",
        "gasLimit": "0x32116200",
        "gasUsed": "0x0",
        "hash": "0x972794bb327a13710bb2f6f3ebed5dc1d88bf4079ba4def2ef7a0dcef9a74261",
        "logsBloom": "0x01000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000",
        "miner": "0x0000000000000000000000000000000000000000",
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x0000000000000000",
        "number": "0x41b11ae",
        "parentHash": "0x0bc66b5cd61bc9f27886720058d0c14e8ec495ab64c1c3c540ef8768134d309c",
        "penalties": "0x",
        "receiptsRoot": "0xbcd2a51669cdca54e5f28517bcd09ca95007951a7d7ec181cb3f361f783cde4a",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "size": "0x351",
        "stateRoot": "0x7e8574656e91e36b2c2407055d8a0b623a942c669be042bc41b53d5c05e4b632",
        "timestamp": "0x64e6fea5",
        "totalDifficulty": "0x231d90772",
        "transactions": [
            "0xc5b4d6979e82af27053a7c178895759ce77d536d22fe593a9587a06be1afeff8"
        ],
        "transactionsRoot": "0xff78a077bfbd1f7597982339992992ea62df6b3329daf84d014f0acbb5dbc4c0",
        "uncles": [],
        "validator": "0x30b1699f5f8e414d2ea949882d20fab5c2ed308f7a6c6d874030aa77c76f0b0c4636cba658cb3dbda4e5fcdb29b07e562f49df5cb9e5fe76723fb0221f27a34501",
        "validators": "0x"
    }
}
```
{% endcode %}
