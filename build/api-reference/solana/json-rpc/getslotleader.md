---
description: Returns the current slot leader
---

# getSlotLeader

#### **Parameters:**

object - optional - Configuration object

#### **Returns:**

string - Node identity Pubkey as base-58 encoded string

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getSlotLeader",
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
