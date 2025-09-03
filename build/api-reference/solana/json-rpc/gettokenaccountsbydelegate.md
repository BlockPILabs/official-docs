---
description: Returns all SPL Token accounts by approved Delegate.
---

# getTokenAccountsByDelegate

#### **Parameters:**

string - required - Pubkey of Token account to query, as base-58 encoded string

object - required - A JSON object

#### **Returns:**

array - An array of JSON objects

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getTokenAccountsByDelegate",
     "params": [
       "4Nd1mBQtrMJVYVfKf2PJy9NZUZdTAsp7D4xWLs4gDB4T",
       {
         "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
       },
       {
         "commitment": "finalized",
         "encoding": "jsonParsed"
       }
     ]
   }
'

// Result

```
{% endcode %}
