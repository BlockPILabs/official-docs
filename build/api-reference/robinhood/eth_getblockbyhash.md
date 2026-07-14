# eth\_getblockbyhash

#### **Parameters:**

**DATA, 32 Bytes** - hash of a block.

**Boolean** - If true it returns the full transaction objects, if false only the hashes of the transactions.

#### **Returns:**

**Object** - A block object, or null when no block was found. Block includes Arbitrum-specific fields: `baseFeePerGas`, `l1BlockNumber`, `sendCount`, `sendRoot`.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["0x34c951125a0b42f16fa981ab9f82ff340acb2b4ae4b76d9cca9fa17cf084bf73", false],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "baseFeePerGas": "0x2a9b3a0",
    "difficulty": "0x1",
    "gasLimit": "0x4000000000000",
    "gasUsed": "0x6319ca",
    "hash": "0x34c951125a0b42f16fa981ab9f82ff340acb2b4ae4b76d9cca9fa17cf084bf73",
    "l1BlockNumber": "0x1859069",
    "number": "0x90a6f2",
    "parentHash": "0x8c686369a6ef2e70213547bee2696b3c2d09a87b6dbe35ee78c47ed337c72d1a",
    "sendCount": "0x176",
    "sendRoot": "0xd741b6ab884fbbc21dd9a96d9f2219ecc4ebbd0c...",
    "timestamp": "0x6a561826",
    "transactions": [
      "0xaa4995a87c6375d17b178c5c9e5b9615b2c107043cae49366c6a3cb21d71fe4c",
      "..."
    ],
    "uncles": []
  }
}
```
{% endcode %}
