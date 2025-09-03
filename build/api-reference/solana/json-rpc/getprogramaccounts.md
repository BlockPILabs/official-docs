---
description: Returns all accounts owned by the provided program Pubkey
---

# getProgramAccounts

#### **Parameters:**

string - required - Pubkey of program, as base-58 encoded string

object - optional - Configuration object

#### **Returns:**

array - By default, returns an array of JSON objects. If `withContext` flag is set, the array will be wrapped in an RpcResponse JSON object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getProgramAccounts",
     "params": [
       "4Nd1mBQtrMJVYVfKf2PJy9NZUZdTAsp7D4xWLs4gDB4T",
       {
         "commitment": "finalized",
         "filters": [
           { "dataSize": 17 },
           {
             "memcmp": {
               "offset": 4,
               "bytes": "3Mc6vR"
             }
           }
         ]
       }
     ]
   }
'

// Result

```
{% endcode %}
