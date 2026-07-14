# eth\_gettransactionbyblockhashandindex

#### **Parameters:**

**DATA, 32 Bytes** - hash of a block.

**QUANTITY** - integer of the transaction index position.

#### **Returns:**

**Object** - A transaction object, or null when no transaction was found.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0x34c951125a0b42f16fa981ab9f82ff340acb2b4ae4b76d9cca9fa17cf084bf73", "0x0"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "blockHash": "0x34c951125a0b42f16fa981ab9f82ff340acb2b4ae4b76d9cca9fa17cf084bf73",
    "blockNumber": "0x90a6f2",
    "from": "0x00000000000000000000000000000000000a4b05",
    "gas": "0x0",
    "gasPrice": "0x0",
    "hash": "0xaa4995a87c6375d17b178c5c9e5b9615b2c107043cae49366c6a3cb21d71fe4c",
    "input": "0x6bf6a42d...",
    "nonce": "0x0",
    "to": "0x00000000000000000000000000000000000a4b05",
    "transactionIndex": "0x0",
    "value": "0x0",
    "type": "0x6a",
    "chainId": "0x1237",
    "v": "0x0",
    "r": "0x0",
    "s": "0x0"
  }
}
```
{% endcode %}
