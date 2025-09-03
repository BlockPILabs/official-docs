---
description: Returns minimum balance required to make account rent exempt.
---

# getMinimumBalanceForRentExemption

#### **Parameters:**

usize - required - The Account's data length

object - optional - Configuration object

#### **Returns:**

u64 - Minimum lamports required in the Account to remain rent free

\


#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getMinimumBalanceForRentExemption",
     "params": [
       50,
       {
         "commitment": "processed",
       }
     ]
   }
'

// Result

```
{% endcode %}
