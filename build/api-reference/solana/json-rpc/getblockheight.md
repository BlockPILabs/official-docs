---
description: Returns the current block height of the node
---

# getBlockHeight

#### **Parameters:**

object - optional - Configuration object.

#### **Returns:**

u64 - Current block height.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getBlockHeight",
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
