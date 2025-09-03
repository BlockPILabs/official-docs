---
description: Returns whether a blockhash is still valid or not
---

# isBlockhashValid

#### **Parameters:**

string - required - The blockhash of the block to evaluate, as base-58 encoded string

object - optional - Configuration object

#### **Returns:**

object - optional - Configuration object&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 45,
     "method": "isBlockhashValid",
     "params": [
       "J7rBdM6AecPDEZp8aPq5iPSNKVkU5Q76F3oAV4eW5wsW",
       {
         "commitment": "processed"
       }
     ]
   }
'

// Result

```
{% endcode %}
