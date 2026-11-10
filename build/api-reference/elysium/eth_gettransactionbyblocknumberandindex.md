# eth\_gettransactionbyblocknumberandindex

#### **Parameters:**

**QUANTITY|TAG** - a block number, or the string "earliest", "latest" or "pending".

**QUANTITY** - the transaction index position.

#### **Returns:**

**Object** - A transaction object, or null when no transaction was found.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["0x379ede","0x0"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "blockHash": "0x2eb03f8c3c8379c1e5004f1cca58a7a88c9895efe856316d69793912b823db46",
    "blockNumber": "0x379ede",
    "blockTimestamp": "0x6af27341",
    "from": "0x00000000000000000000000000000000000a4b05",
    "gas": "0x0",
    "gasPrice": "0x0",
    "hash": "0x609f6b44e2f5959d591a8bf3f6ec8543ae05e931fe58c3b3f69055a28b078e97",
    "input": "0x6bf6a42d00000000000000000000000000000000000000000000000000...",
    "nonce": "0x0",
    "to": "0x00000000000000000000000000000000000a4b05",
    "transactionIndex": "0x0",
    "value": "0x0",
    "type": "0x6a",
    "chainId": "0x1863d",
    "v": "0x0",
    "r": "0x0",
    "s": "0x0"
  }
}
```
{% endcode %}
