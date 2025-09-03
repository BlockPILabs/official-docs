---
description: Returns transaction details for a confirmed transaction
---

# getTransaction

#### **Parameters:**

string - required - Pubkey of account owner to query, as base-58 encoded string

object - optional - Configuration object

#### **Returns:**

object - Returns `null` if transaction is not found or not confirmed

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getTransaction",
     "params": [
       "5Pj5fCupXLUePYn18JkY8SrRaWFiUctuDTRwvUy2ML9yvkENLb1QMYbcBGcBXRrSVDjp7RjUwk9a3rLC6gpvtYpZ",
       {
         "commitment": "confirmed",
         "maxSupportedTransactionVersion": 0,
         "encoding": "json"
       }
     ]
   }
'

// Result

```
{% endcode %}
