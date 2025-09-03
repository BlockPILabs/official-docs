---
description: Returns the total supply of an SPL Token type.
---

# getTokenSupply

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
     "method": "getTokenSupply",
     "params": [
       "3wyAj7Rt1TWVPZVteFJPLa26JmLvdb1CAKEFZm3NY75E",
       {
         "commitment": "finalized"
       }
     ]
   }
'

// Result

```
{% endcode %}
