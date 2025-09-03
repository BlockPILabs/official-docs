---
description: >-
  Returns recent block production information from the current or previous
  epoch.
---

# getBlockProduction

#### **Parameters:**

object - optional - Configuration object.

#### **Returns:**

object - The result will be an RpcResponse JSON object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getBlockProduction",
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
