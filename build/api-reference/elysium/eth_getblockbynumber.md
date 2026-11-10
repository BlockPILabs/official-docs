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
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x379ede",false],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "baseFeePerGas": "0x1de13b20",
    "difficulty": "0x1",
    "extraData": "0x6e637d4b6946875108177480873c5ae33aba9915edc5c90afa96b0d3a04f363b",
    "gasLimit": "0x4000000000000",
    "gasUsed": "0x94569",
    "hash": "0x2eb03f8c3c8379c1e5004f1cca58a7a88c9895efe856316d69793912b823db46",
    "l1BlockNumber": "0x307ec4b",
    "logsBloom": "0x0000000000000000000000000000000000000000000000000000000000...",
    "miner": "0xa4b000000000000000000073657175656e636572",
    "mixHash": "0x0000000000000eef000000000307ec4b000000000000003d0001000000000000",
    "nonce": "0x000000000026c9d0",
    "number": "0x379ede",
    "parentHash": "0xfbdd3983ab36600affd0b0c781a7d77ae309e4b5c1ae94d50d1da59493d5221d",
    "receiptsRoot": "0x63994f9588fb964f0b4644ab56810d4697c7dbd0d3e846fd52ab801bb1eb84b3",
    "sendCount": "0xeef",
    "sendRoot": "0x6e637d4b6946875108177480873c5ae33aba9915edc5c90afa96b0d3a04f363b",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x10ce",
    "stateRoot": "0x36d31189112bbfe220a80e7402607404143acbff253869aeae95a2036f339b3e",
    "timestamp": "0x6af27341",
    "transactions": [
      "0x609f6b44e2f5959d591a8bf3f6ec8543ae05e931fe58c3b3f69055a28b078e97",
      "0x49d216c1808bdb7ec960c3b720dc20c337160150eb0ad748ca12a4efd5fa21b7",
      "..."
    ],
    "transactionsRoot": "0xcfa0d0f3f4f517d5acf2e47ddbb737efa65f8b92b0957401bdaddfaa6e46558d",
    "uncles": []
  }
}
```
{% endcode %}
