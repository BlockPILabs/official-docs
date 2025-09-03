---
description: Returns the highest slot information that the node has snapshots for.
---

# getHighestSnapshotSlot

#### **Parameters:**

None

#### **Returns:**

object - When the node has a snapshot

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getHighestSnapshotSlot"
   }
'

// Result

```
{% endcode %}
