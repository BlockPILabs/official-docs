---
description: Returns the latest blockhash
---

# getLatestBlockhash

#### **Parameters:**

object - optional - Configuration object

#### **Returns:**

object - RpcResponse JSON object with `value` field set to a JSON object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getLatestBlockhash",
     "params": [
       {
         "commitment": "processed"
       }
     ]
   }
'

// Result

```
{% endcode %}
