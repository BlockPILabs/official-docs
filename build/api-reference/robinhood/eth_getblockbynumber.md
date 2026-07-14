# eth\_getblockbynumber

#### **Parameters:**

**QUANTITY|TAG** - integer of a block number, or the string "earliest", "latest" or "pending".

**Boolean** - If true it returns the full transaction objects, if false only the hashes of the transactions.

#### **Returns:**

**Object** - A block object, or null when no block was found. Block includes Arbitrum-specific fields: `baseFeePerGas`, `l1BlockNumber`, `sendCount`, `sendRoot`.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x90a6f2", false],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "baseFeePerGas": "0x2a9b3a0",
    "difficulty": "0x1",
    "extraData": "0xd741b6ab884fbbc21dd9a96d9f2219ecc4ebbd0c...",
    "gasLimit": "0x4000000000000",
    "gasUsed": "0x6319ca",
    "hash": "0x34c951125a0b42f16fa981ab9f82ff340acb2b4ae4b76d9cca9fa17cf084bf73",
    "l1BlockNumber": "0x1859069",
    "logsBloom": "0x000000000000908101001000...",
    "miner": "0xa4b000000000000000000073657175656e636572",
    "mixHash": "0x00000000000001760000000001859069...",
    "nonce": "0x0000000000006e3a",
    "number": "0x90a6f2",
    "parentHash": "0x8c686369a6ef2e70213547bee2696b3c2d09a87b6dbe35ee78c47ed337c72d1a",
    "receiptsRoot": "0xf742e06a1a672ccc44d81a0b462929c80780e9f85e42dd718b108c3057c1ac75",
    "sendCount": "0x176",
    "sendRoot": "0xd741b6ab884fbbc21dd9a96d9f2219ecc4ebbd0c...",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x197a",
    "stateRoot": "0x755587f2d7826989a021758a2d26381f7b35bcfe308bb9fbe9609eab04f1b1f5",
    "timestamp": "0x6a561826",
    "transactions": [
      "0xaa4995a87c6375d17b178c5c9e5b9615b2c107043cae49366c6a3cb21d71fe4c",
      "..."
    ],
    "transactionsRoot": "0xf810a6afe1a53a65ea91a0c41a6938025d49283e3902397e609c84522e582a6c",
    "uncles": []
  }
}
```
{% endcode %}
