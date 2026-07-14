# eth\_getblockreceipts

#### **Parameters:**

**QUANTITY|TAG** - integer of a block number, or the string "earliest", "latest" or "pending".

#### **Returns:**

**Array** - Array of transaction receipt objects for the given block. Receipts include Arbitrum-specific fields: `effectiveGasPrice`, `gasUsedForL1`, `l1BlockNumber`.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockReceipts","params":["0x90a6f2"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "blockHash": "0x34c951125a0b42f16fa981ab9f82ff340acb2b4ae4b76d9cca9fa17cf084bf73",
      "blockNumber": "0x90a6f2",
      "contractAddress": null,
      "cumulativeGasUsed": "0x0",
      "effectiveGasPrice": "0x2a9b3a0",
      "from": "0x00000000000000000000000000000000000a4b05",
      "gasUsed": "0x0",
      "gasUsedForL1": "0x0",
      "l1BlockNumber": "0x1859069",
      "logs": [],
      "status": "0x1",
      "to": "0x00000000000000000000000000000000000a4b05",
      "transactionHash": "0xaa4995a87c6375d17b178c5c9e5b9615b2c107043cae49366c6a3cb21d71fe4c",
      "transactionIndex": "0x0",
      "type": "0x6a"
    }
  ]
}
```
{% endcode %}
