---
description: Returns the slot that has reached the given or default commitment level
---

# getSlot

#### **Parameters:**

object - optional - Configuration object

#### **Returns:**

u64 - Current slot

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getSlot",
     "params": [
       {
         "commitment": "finalized"
       }
     ]
   }
'

// Result

```
{% endcode %}
