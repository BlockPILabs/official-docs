---
description: Returns the Klaytn protocol version of the node.
---

# kaia\_protocolVersion

#### **Parameters**

None

#### **Return Value**

| Type   | Description                              |
| ------ | ---------------------------------------- |
| String | The Klaytn protocol version of the node. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_protocolVersion","params":[],"id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
   "jsonrpc":"2.0",
   "id":1,
   "result":"0x40"
}
```
{% endcode %}
