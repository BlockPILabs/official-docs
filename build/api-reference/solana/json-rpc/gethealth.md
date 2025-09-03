---
description: >-
  Returns the current health of the node. A healthy node is one that is within
  HEALTH_CHECK_SLOT_DISTANCE slots of the latest cluster confirmed slot.
---

# getHealth

#### **Parameters:**

None

#### **Returns:**

string - If the node is healthy: "ok"

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getHealth"
   }
'

// Result

```
{% endcode %}
