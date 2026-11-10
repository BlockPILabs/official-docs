# eth\_gettransactionreceipt

#### **Parameters:**

**DATA, 32 Bytes** - hash of a transaction.

#### **Returns:**

**Object** - A transaction receipt object, or null when no receipt was found. Receipts include Arbitrum-specific fields: `effectiveGasPrice`, `gasUsedForL1`, `l1BlockNumber`.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0x609f6b44e2f5959d591a8bf3f6ec8543ae05e931fe58c3b3f69055a28b078e97"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
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
  }
}
```
{% endcode %}
