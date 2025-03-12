---
description: Returns the current client version of a Klaytn node.
---

# klay\_clientVersion

#### **Parameters**

`None`

#### **Return Value**

| Type   | Description                                  |
| ------ | -------------------------------------------- |
| String | The current client version of a Klaytn node. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_clientVersion","id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
    "jsonrpc":"2.0",
    "id":1,
    "result":"Klaytn/v0.9.1+3518232250/linux-amd64/go1.11.2"
}
```
{% endcode %}
