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
curl  https://monad.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest", true],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "hash": "0x33b3f51da4bb4d0753b6860c591e08890048adce5388f43cbc795c4d91eb5890",
        "parentHash": "0x7eed8312a0d1fd9b622e0dfebfc14ef13e702e54f11b1332e0d266e61026e1ab",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "miner": "0x0000000000000000000000000000000000000000",
        "stateRoot": "0x3c11b90967d7f7f686dba8fe2a0a5b48a4ac5bbe44d6bf973e86371cf61e8b6f",
        "transactionsRoot": "0x9da19a1386c04285db3bbbf3fe4c0bf595d935d599dac822ae7f589b74bed63d",
        "receiptsRoot": "0x63a81f70a8b5be086f5f6a75ed5f1e904287c42897397e687ff931a5be1f6e62",
        "logsBloom": "0x48630448750030401444020ab40069042230200480882126f68806408040c386540800218a380200009001e40b1402706800110043d00406b3a80011c8a0200032f652e1841177800022063c4317003622c312c191c0900472cc200482000a02002fb220a268600f2062424000250891800010020e040ea1c0068098814004e806204404c1062048cc1904112d1247b800080901502be41ca30420e8254009521a30000382807544020644a488820280a52c20995a0116505c1008000842818002440402c8403108492000308011900a18450900016fe5360a1100969100a0a11056c4469b0042482922809122218024c88100370643806430741a4ca4043260",
        "difficulty": "0x0",
        "number": "0x7c2de7",
        "gasLimit": "0x8f0d180",
        "gasUsed": "0x1e3a5f0",
        "timestamp": "0x67d7d14f",
        "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "mixHash": "0x22b5edd568868340204c2adab08dc65a15ef996b83e3f93f2beb0218caf5762a",
        "nonce": "0x0000000000000000",
        "baseFeePerGas": "0xba43b7400",
        "withdrawalsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "blobGasUsed": "0x0",
        "excessBlobGas": "0x0",
        "parentBeaconBlockRoot": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "totalDifficulty": "0x0",
        "size": "0x30f",
        "uncles": [],
        ......
```
{% endcode %}
