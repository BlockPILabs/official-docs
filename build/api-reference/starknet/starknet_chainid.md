---
description: Return the currently configured StarkNet chain id
---

# starknet\_chainId

#### **Parameters:**

**None**

#### **Returns:**

The chain id the node is connected to

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc":"2.0","method":"starknet_chainId","params":[],"id":0}'

// Result
{
    "id": 0,
    "jsonrpc": "2.0",
    "result": "0x534e5f4d41494e"
}
```
{% endcode %}
