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
curl  https://polygon.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest", true],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "baseFeePerGas": "0xcd6f5",
        "difficulty": "0x19",
        "extraData": "0xd482021083626f7286676f312e3139856c696e7578000000000000000000000027ae26c6222b0620a1e8f58c3d40cdf19c1ed3aac726fab883d6ae9d4c66aa00220f38037e15375d21e3a6345455f531a2f5f5966446731141ca74433cef758800",
        "gasLimit": "0x1b4b65c",
        "gasUsed": "0xeef748",
        "hash": "0x62fb6f40ce116ec45700f1e72601d982295dd679702ec5b5bf39ebd025d720d2",
        "logsBloom": "0x59ee9002c4895c82160c083cb8e564e08993b38485084039d7791a5a01502040454838a59164e8491423b07176a68c15e779881734daa6402eb80a17027676d90c0f25441bc848a888323c09ad28fbe8c35a24efcfe4dc04f63b241ca426e303d295c8cb4328c9029b213f980d34a86145040059f913b6b9f46c6073108c22aa813f4540a01deec784c85550cd2843e800872c9188c8190e2ac0f2508cc200152342c9e2d0c2054921210132b8a178da537d09e3a1d08b23f9054026007de945820294bfde8a7e871109bb71ef7e4ea94b7c2f0d880ba195547db39eec96a256203539aeb3439c8e1201aa400d0d8831c0a80325cccca4d3c3d0780156396aad",
        "miner": "0x0000000000000000000000000000000000000000",
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x0000000000000000",
        "number": "0x20945ef",
        "parentHash": "0xd4d8e98c7560d1e9b7acfb307194264fa4c86930517bc9f6d9ee2756b16ff2ae",
        "receiptsRoot": "0x0447cb64592e720222bd0fb6cef885f37710e276751016e498e0eae1901aed40",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "size": "0xbf06",
        "stateRoot": "0x472dcac19b886052443ab8675c4dc77a3df986bd3b860008ed1446faae228ecb",
        "timestamp": "0x6343e0e1",
        "totalDifficulty": "0x1f1344e5",
        "transactions": [{
            "blockHash": "0x62fb6f40ce116ec45700f1e72601d982295dd679702ec5b5bf39ebd025d720d2",
            "blockNumber": "0x20945ef",
            "from": "0x324ec7743a70212299ae82ad674f7547e6b4069d",
            "gas": "0xaae60",
            "gasPrice": "0x1bf08eb000",
            "hash": "0xa7b57393e5a854d29ce852d0c7545527a4f54c283bbdb10c64a4ceda3e45ede6",
            "input": "0x8803dbee000000000000000000000000000000000000000000000003e7cba3f2da10e610000000000000000000000000000000000000000000000000000000000122fced00000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000138cd43c3c8d934b96a0a1d404a706b2a2d5c84f000000000000000000000000000000000000000000000000000000006343e0ec00000000000000000000000000000000000000000000000000000000000000030000000000000000000000002791bca1f2de4661ed88a30c99a7a9449aa84174000000000000000000000000c168e40227e4ebd8c1cae80f7a55a4f0e6d66c97000000000000000000000000f6f85b3f9fd581c2ee717c404f7684486f057f95",
            "nonce": "0x61f3",
            "to": "0xa102072a4c07f06ec3b4900fdc4c7b80b6c57429",
            "transactionIndex": "0x0",
            "value": "0x0",
            "type": "0x0",
            "v": "0x135",
            "r": "0x24c2adcb9fe5938931051027e8c3c47368bccf49415d0476e1bbb5c467da66c",
            "s": "0x6c0fd7bc5d6521df05a486fe0e80aabfd41c282e412380c52cd67cbb92d089bb"
        }, {
            "blockHash": "0x62fb6f40ce116ec45700f1e72601d982295dd679702ec5b5bf39ebd025d720d2",
            "blockNumber": "0x20945ef",
            "from": "0x03e98572d5cea14c07e8eedd7076e704e90dcb27",
            "gas": "0x493ee",
            "gasPrice": "0x174883bef5",
            "maxFeePerGas": "0x17488785cc",
            "maxPriorityFeePerGas": "0x174876e800",
            "hash": "0x76503903d65cb57e270aa5248092f3749b28e2b520c932b1ce079556d465107a",
            "input": "0x768ac73b000000000000000000000000000000000000000000000001158e460913d00000000000000000000000000000000000000000000000000002ef30971d0829c0000000000000000000000000001807cac8576468d96a09a2c04fbdf6fdf0ed2a1d00000000000000000000000050b728d8d964fd00c2d0aad81718b71311fef68a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000000000000",
            "nonce": "0x130c9",
            "to": "0xfa1fd291d6b235d32eaf4117058c824714c302f7",
            "transactionIndex": "0x1",
            "value": "0x0",
            "type": "0x2",
            "accessList": [],
            "chainId": "0x89",
            "v": "0x0",
            "r": "0x6146d9d0fdb5876269cb7e2e0e57feeea3c1eede0e4ae185ae4ee2fa6ce19ab7",
            "s": "0x4a558402a4d41434fd58e0488854102e7a6163396ae7745a509a4bc474a2872a"
        }, 
        ......
        {
            "blockHash": "0x62fb6f40ce116ec45700f1e72601d982295dd679702ec5b5bf39ebd025d720d2",
            "blockNumber": "0x20945ef",
            "from": "0xa53fe3e7644dec5c22e08bfd4bcf508671b2f911",
            "gas": "0x36f0a",
            "gasPrice": "0x6fc3082f5",
            "maxFeePerGas": "0x6fc30a250",
            "maxPriorityFeePerGas": "0x6fc23ac00",
            "hash": "0xd0624233db37a88e594d2bd512a1921b8bba3d164f1fbb643583a8541d88173d",
            "input": "0x9d6df6a80000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000202bdba8a06407f4feb3071c908fe277990d9a0ef581b0a13b9dfa904d37e31d4f000000000000000000000000a53fe3e7644dec5c22e08bfd4bcf508671b2f9110000000000000000000000009dab278a36fa81b0d7b630a4936d13984105224a00000000000000000000000000000000000000000000000000000000000f4240000000000000000000000000000000000000000000000000000000006343e1ea000000000000000000000000000000000000000000000000000000000000008900000000000000000000000000000000000000000000000000000000000000e0000000000000000000000000000000000000000000000000000000000000004104ddc2a33debc1f1f00d744c3313d430f686cc8eb6d924d9e3969f60af084e972409e13afe9741843e73027d347053ed5064850b18ff6b110d19438ff9d9fc111c00000000000000000000000000000000000000000000000000000000000000",
            "nonce": "0x0",
            "to": "0xffb9f1907f827709b0ed09b37956cd3c7462abdb",
            "transactionIndex": "0x55",
            "value": "0x0",
            "type": "0x2",
            "accessList": [],
            "chainId": "0x89",
            "v": "0x0",
            "r": "0xeb804fdfa10e53a4a73af31e4ddd3af5cba971c3165c2d6b0ce5b31bb4e0909b",
            "s": "0x374289838ffec54263160c8cf34ba4e9fe4ef64baf7e4aa1be9b8700d99aeea4"
        }],
        "transactionsRoot": "0x6f477838b21f9edaa571df707b85eb0f2544ee40c0449fbb7bc170234ce8ee42",
        "uncles": []
    }
}
```
{% endcode %}
