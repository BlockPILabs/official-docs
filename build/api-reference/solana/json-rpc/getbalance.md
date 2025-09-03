---
description: Returns the lamport balance of the account of provided Pubkey
---

# getBalance

#### **Parameters:**

string - required - Pubkey of account to query, as base-58 encoded string.

object - optional - Configuration object.

#### **Returns:**

u64 - RpcResponse JSON object with value field set to the balance.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getBalance",
     "params": [
       "83astBRguLMdt2h5U1Tpdq5tjFoJ6noeGwaY3mDLVcri",
       {
         "commitment": "finalized"
       }
     ]
   }
'

// Result

```
{% endcode %}
