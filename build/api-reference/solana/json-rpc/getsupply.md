---
description: Returns information about the current supply.
---

# getSupply

#### **Parameters:**

object - optional - Configuration object

#### **Returns:**

object - The result will be a JSON object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getSupply",
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
