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
curl https://base.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["0x7896799aa9972636ce6621f5099fb0b541406337e33f6b16d733ebfec9f68fe7",false],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "baseFeePerGas": "0x54",
        "difficulty": "0x0",
        "extraData": "0x",
        "gasLimit": "0x17d7840",
        "gasUsed": "0x1f03ee",
        "hash": "0x7896799aa9972636ce6621f5099fb0b541406337e33f6b16d733ebfec9f68fe7",
        "logsBloom": "0x00200000000000000008010080000000010008000001000020000008010900000400021400040000000002004200000090400000040800000080300008300000000400000082220000000008040008200000000480c00200020000000200000000000000000800000204000008a00000000000080010040480020010004000200400000200000800000000200000000840000804004110580000004100000000020000002000800240000000000000000000000000000000002040000004000000000002000000000000082100300000000200000000201000000012000000000030400000000802064000000200800000000020000094000000000000400000",
        "miner": "0x4200000000000000000000000000000000000011",
        "mixHash": "0xf63f2a2b0e7885d78381a05ab3b73896e961b238b6020a5162fc95f2fb1bc276",
        "nonce": "0x0000000000000000",
        "number": "0x5f1dae",
        "parentHash": "0x06e43080ef7d2bb7170967993aba670ba5edafbac5481236fcfbbe6f3559c01f",
        "receiptsRoot": "0x7e0c7c49523dffe24039a225811227cc4c5ecc843baa5118b0c8d4d7e65a8f17",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "size": "0xef5",
        "stateRoot": "0x56bfc7fbac247262f8b4a40bc648c302104b773facf7a1be2388afd2db972064",
        "timestamp": "0x6497a86c",
        "totalDifficulty": "0x0",
        "transactions": [
            "0x57294047f5f7b7eb9aec7a2b414b4fffe89598b26025c9c4bab9d8d363e3ac82",
            "0x5c61d8eb4249238b0fce0f3cd9fb0644d8abfda414faf455658de82c20eb3501",
            "0x8310320caeb78674974c601b4b22e34457b7da5e77bdbd6f5d0508fef6b326bb",
            "0x99050c3d52e3cbd0ee26870dc55f8fc4d29277b860d636aca26833eacba839b4",
            "0x68d75a82952957f80c51beead59c97c52b64c3f7cfe68037adbf632997a457e8",
            "0xebe2b92131c383cbaf3dc760b3612a9f578f240701c3b20c19d0dc03d9c980aa",
            "0x87c7a930f2f6699e6383a67f56c0b7dea10bceca2856ca95f7b1769418e24506",
            "0x0f8ac052f5b2d1b0624f775c1d9e4a15c2aac8c23b2c08532550ed9d4abd871d",
            "0x4493d19e29a374ae0246d92e6e8ce6aa2e5a88399f4e8f16355869316ded9d50",
            "0x5d547321ab8a6824848153517d7c45ca92ec749b4abc43f1d059a922e0e3f32f",
            "0xff5de1e26e15ba1684ae8db72d9283ceabecf16c8edcd620cb5fc834a93b208e",
            "0xbe7036797e2d309d7fbd2cafd4adae6bcf21494de784e7853c3fc1452f3877ff",
            "0xa32e1de1a295ac7e076cf1e6f1b62e5c7fe0d4fc901485fbb261765ed4d92acf",
            "0xf466677132b3ebc8ef5af6c8e124bb7a7ba302f94c08af5a99ad3862490fddc9",
            "0x653c606b1d7da931f4d4f6ab3d85d851246c9da83e6bdbad28dfe2afc4511186",
            "0x16fdfd8791f3bfebc4cb570f9a5ae23a4a1ca32ea891b5210770505ca298a840",
            "0x4bc488e6d0e088efc31b1e21e32c0660330ab511ac7cb90024645eb50c4d08b6",
            "0x1f653c7d716b12e1c397b62ea82c7d41702e99e05e87200b94366fb9b8d1259a",
            "0x0d30600f49e90ee2b6deffe7e9daec7c8fba6401a8ea08e120e868fb5ee09818",
            "0x25e98fc28c6c80780fd38ddbc0edc27567fbf24a1b62d3a29929d1c5299a96c0",
            "0x724c65dc1bf9106523d070d3f1a57070111a4e88a34fe3caddb5e367c5ad2c57",
            "0x689fbc142cb80ed4110934f0a806c94e1f2c7e27fa1b0e66c68ba01e964ea0dd",
            "0xcb273b4a725ddee1479c021f3b4f87e963ba182d8712d5f59c6a01e4a8ef30c4",
            "0x155247f9fc7835050007331d4ce9671839ebe187260af33500f2aaab8cb5fbec"
        ],
        "transactionsRoot": "0x0b7603a38b67a72346491c50e78ac12d02dcd62c7ef2dc2bb6e92c5a19ebff54",
        "uncles": []
    }
}
```
{% endcode %}
