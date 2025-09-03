---
description: >-
  Returns signatures for confirmed transactions that include the given address
  in their accountKeys list. Returns signatures backwards in time from the
  provided signature or most recent confirmed block
---

# getSignaturesForAddress

#### **Parameters:**

string - required - Account address as base-58 encoded string

#### **Returns:**

array - An array of transaction signature information objects, ordered from **newest** to **oldest** transaction

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getSignaturesForAddress",
     "params": [
       "Vote111111111111111111111111111111111111111",
       {
         "commitment": "finalized",
         "limit": 1
       }
     ]
   }
'

// Result

```
{% endcode %}
