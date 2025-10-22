---
description: Returns the number of most recent block.
---

# kaia\_blockNumber

#### **Parameters**

None

#### **Return Value**

| Type     | Description                                           |
| -------- | ----------------------------------------------------- |
| QUANTITY | Integer of the current block number the client is on. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_blockNumber","params":[],"id":83}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id":83,
  "result": "0xc94"
}
```
{% endcode %}
