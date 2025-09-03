---
description: Returns the current Transaction count from the ledger
---

# getTransactionCount

#### **Parameters:**

object - optional - Configuration object

#### **Returns:**

u64 - The current Transaction count from the ledger

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getTransactionCount",
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
