---
description: >-
  Returns true if the node is writing blockchain data in parallel manner. It is
  enabled by default.
---

# klay\_isParallelDBWrite

#### **Parameters**

None

#### **Return Value**

| Type    | Description                                                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Boolean | `true` means the node is writing blockchain data in parallel manner. It is `false` if the node is writing the data in serial manner. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_isParallelDBWrite","id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
```
{% endcode %}
