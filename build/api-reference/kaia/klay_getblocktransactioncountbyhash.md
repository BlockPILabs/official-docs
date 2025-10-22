---
description: >-
  Returns the number of transactions in a block from a block that matches the
  given hash.
---

# kaia\_getBlockTransactionCountByHash

#### **Parameters**

| Type         | Description     |
| ------------ | --------------- |
| 32-byte DATA | Hash of a block |

#### **Return Value**

| Type     | Description                                          |
| -------- | ---------------------------------------------------- |
| QUANTITY | Integer of the number of transactions in this block. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_getBlockTransactionCountByHash","params":["0x0c11803ab36110db993e7520908b9ba9336cca2f2dcc9b6130c481a3ccdc2621"],"id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id":1,
  "result": "0x0"
}
```
{% endcode %}
