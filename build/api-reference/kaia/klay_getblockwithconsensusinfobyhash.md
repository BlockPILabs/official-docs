---
description: Returns a block with consensus information that matches the given hash.
---

# kaia\_getBlockWithConsensusInfoByHash

#### **Parameters**

| Type         | Description      |
| ------------ | ---------------- |
| 32-byte DATA | Hash of a block. |

#### **Return Value**

See [Klaytn Docs](https://docs.klaytn.foundation/dapp/json-rpc/api-references/klay/block#klay_getblockwithconsensusinfobyhash)

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "method":"kaia_getBlockWithConsensusInfoByHash", "params":["0x7d68d09a7a571cdf8a3b6a5ef6e037265b3e3093cf145b0954d22bde5c1d4f61"],"id":73}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id": 73,
  "result": {
    "baseFeePerGas":"0x0",
    "blockscore": "0x1",
    "committee": [ ...
    ],
    "transactionsRoot": "0x020a2156bb4b29dc84f26887efae79e07a3d738b2856a66bbaab8aee18d507b5",
    "voteData": "0x"
  }
}
```
{% endcode %}
