---
description: Returns all SPL Token accounts by token owner.
---

# getTokenAccountsByOwner

#### **Parameters:**

string - required - Pubkey of account owner to query, as base-58 encoded string

object - optional - Configuration object

#### **Returns:**

array - An array of JSON objects&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getTokenAccountsByOwner",
     "params": [
       "A1TMhSGzQxMr1TboBKtgixKz1sS6REASMxPo1qsyTSJd",
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
