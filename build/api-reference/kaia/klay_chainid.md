---
description: Returns the chain ID of the chain.
---

# kaia\_chainID

#### **Parameters**

None

#### **Return Value**

| Type     | Description                           |
| -------- | ------------------------------------- |
| QUANTITY | Integer of the chain ID of the chain. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_chainID","id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
    "jsonrpc":"2.0",
    "id":1,
    "result":"0x7e2"
}
```
{% endcode %}
