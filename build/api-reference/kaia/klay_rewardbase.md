---
description: >-
  Returns the rewardbase of the current node. Rewardbase is the address of the
  account where the block rewards goes to. It is only required for CNs.
---

# kaia\_rewardbase

#### **Parameters**

None

#### **Return Value**

| Type         | Description |
| ------------ | ----------- |
| 20-byte DATA | Address.    |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_rewardbase","id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result - If requested from non-CN nodes
{
    "jsonrpc":"2.0",
    "id":1,
    "error":{
        "code":-32000,
        "message":"rewardbase must be explicitly specified"
        }
}

// Result - If requested from CN nodes
{
    "jsonrpc":"2.0",
    "id":1,
    "result":"0x96Fd91f34Cc8da9f6338C106Ba37aA8B48FB4Fa5"
}
```
{% endcode %}
