---
description: >-
  Returns the 20 largest accounts, by lamport balance (results may be cached up
  to two hours)
---

# getLargestAccounts

#### **Parameters:**

object - optional - Configuration object

#### **Returns:**

array - The result will be an RpcResponse JSON object with `value` equal to an array of objects

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getLargestAccounts",
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
