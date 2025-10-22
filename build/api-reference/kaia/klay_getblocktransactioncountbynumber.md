---
description: Returns the number of transactions in a block matching the given block number.
---

# kaia\_getBlockTransactionCountByNumber

#### **Parameters**

| Type             | Description                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------- |
| QUANTITY \| TAG  | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`. |

#### **Return Value**

| Type     | Description                                          |
| -------- | ---------------------------------------------------- |
| QUANTITY | Integer of the number of transactions in this block. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_getBlockTransactionCountByNumber","params":["0xe8"],"id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id":1,
  "result": "0xa" // 10
}
```
{% endcode %}
