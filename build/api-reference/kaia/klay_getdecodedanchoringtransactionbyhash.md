---
description: >-
  Returns the decoded anchored data in the transaction for the given transaction
  hash.
---

# klay\_getDecodedAnchoringTransactionByHash

#### **Parameters**

| Type         | Description            |
| ------------ | ---------------------- |
| 32-byte DATA | Hash of a transaction. |

#### **Return Value**

<table><thead><tr><th width="323">Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td>BlockHash</td><td>32-byte DATA</td><td>Hash of the child chain block that this anchoring transaction was performed.</td></tr><tr><td>BlockNumber</td><td>QUANTITY</td><td>The child chain block number that this anchoring transaction was performed.</td></tr><tr><td>ParentHash</td><td>32-byte DATA</td><td>Hash of the parent block.</td></tr><tr><td>TxHash</td><td>32-byte DATA</td><td>The root of the transaction trie of the block.</td></tr><tr><td>StateRootHash</td><td>32-byte DATA</td><td>The root of the final state trie of the block.</td></tr><tr><td>ReceiptHash</td><td>32-byte DATA</td><td>The root of the receipts trie of the block.</td></tr><tr><td>BlockCount</td><td>QUANTITY</td><td>The number of blocks generated during this anchoring period. In most cases, this number is equal to the child chain's <code>SC_TX_PERIOD</code>, with the exception of the case that this transaction was the first anchoring tx after turning on the anchoring.</td></tr><tr><td>TxCount</td><td>QUANTITY</td><td>The number of transactions generated in the child chain during this anchoring period.</td></tr></tbody></table>

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_getDecodedAnchoringTransactionByHash","params":["0x499350bc5e2f6fee1ba78b4d40a7a1db0a64f3c091112e6798a02ed9a4140084"],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
   "jsonrpc":"2.0",
   "id":1,
   "result":{
      "BlockCount":1,
      "BlockHash":"0xcf5f591836d70a1da8e6bb8e5b2c5739329ca0e535b91e239b332af2e1b7f1f4",
      "BlockNumber":1055,
      "ParentHash":"0x70f6115a5b597f29791d3b5e3f129df54778f69ae669842cc81ec8c432fee37c",
      "ReceiptHash":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
      "StateRootHash":"0x654773348f77a6788c76c93946340323c9b39399d0aa173f6b23fe082848d056",
      "TxCount":0,
      "TxHash":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421"
   }
}
```
{% endcode %}
