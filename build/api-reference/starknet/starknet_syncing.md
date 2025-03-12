---
description: Returns an object about the sync status, or false if the node is not synching
---

# starknet\_syncing

#### **Parameters:**

None

#### **Returns:**

The status of the node, if it is currently synchronizing state. FALSE otherwise

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc":"2.0","method":"starknet_syncing","params":[],"id":0}'

// Result
{
    "id": 0,
    "jsonrpc": "2.0",
    "result": false
}
```
{% endcode %}
