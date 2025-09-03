---
description: Returns the stake minimum delegation, in lamports.
---

# getStakeMinimumDelegation

#### **Parameters:**

object - optional - Configuration object

#### **Returns:**

u64 - The stake minimum delegation, in lamports

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getStakeMinimumDelegation",
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
