---
description: Returns the token balance of an SPL Token account.
---

# getTokenAccountBalance

#### **Parameters:**

string - required - Pubkey of Token account to query, as base-58 encoded string

object - optional - Configuration object

#### **Returns:**

object - The result will be a JSON object&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getTokenAccountBalance",
     "params": [
       "7fUAJdStEuGbc3sM84cKRL6yYaaSstyLSU4ve5oovLS7",
       {
         "commitment": "finalized"
       }
     ]
   }
'

// Result

```
{% endcode %}
