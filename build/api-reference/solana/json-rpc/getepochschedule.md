---
description: Returns the epoch schedule information from this cluster
---

# getEpochSchedule

#### **Parameters:**

None

#### **Returns:**

object - The result field will be an object&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getEpochSchedule"
   }
'

// Result

```
{% endcode %}
