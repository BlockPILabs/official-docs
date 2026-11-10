# eth\_getblockreceipts

#### **Parameters:**

**QUANTITY|TAG** - integer of a block number, or the string "earliest", "latest" or "pending".

#### **Returns:**

**Array** - Array of transaction receipt objects for the given block. Receipts include Arbitrum-specific fields: `effectiveGasPrice`, `gasUsedForL1`, `l1BlockNumber`.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockReceipts","params":["0x379ede"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "blockHash": "0x2eb03f8c3c8379c1e5004f1cca58a7a88c9895efe856316d69793912b823db46",
      "blockNumber": "0x379ede",
      "contractAddress": null,
      "cumulativeGasUsed": "0x0",
      "effectiveGasPrice": "0x0",
      "from": "0x00000000000000000000000000000000000a4b05",
      "gasUsed": "0x0",
      "gasUsedForL1": "0x0",
      "l1BlockNumber": "0x307ec4b",
      "logs": [],
      "logsBloom": "0x0000000000000000000000000000000000000000000000000000000000...",
      "status": "0x1",
      "to": "0x00000000000000000000000000000000000a4b05",
      "transactionHash": "0x609f6b44e2f5959d591a8bf3f6ec8543ae05e931fe58c3b3f69055a28b078e97",
      "transactionIndex": "0x0",
      "type": "0x6a"
    },
    {
      "blockHash": "0x2eb03f8c3c8379c1e5004f1cca58a7a88c9895efe856316d69793912b823db46",
      "blockNumber": "0x379ede",
      "contractAddress": null,
      "cumulativeGasUsed": "0xd1ee",
      "effectiveGasPrice": "0x1de1622f",
      "from": "0xf4a94564b91030cfac709cf210f28bc4ec7bdbe2",
      "gasUsed": "0xd1ee",
      "gasUsedForL1": "0x0",
      "l1BlockNumber": "0x307ec4b",
      "logs": [],
      "logsBloom": "0x0000000000000000000000000000000000000000000000000000000000...",
      "status": "0x1",
      "to": "0xf290da81a29a11e9e19ee5dae1e2e3addc34cf10",
      "transactionHash": "0x49d216c1808bdb7ec960c3b720dc20c337160150eb0ad748ca12a4efd5fa21b7",
      "transactionIndex": "0x1",
      "type": "0x2"
    },
    "..."
  ]
}
```
{% endcode %}
