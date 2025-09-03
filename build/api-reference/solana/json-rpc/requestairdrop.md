---
description: Requests an airdrop of lamports to a Pubkey
---

# requestAirdrop

#### **Parameters:**

string - required - Pubkey of account to receive lamports, as a base-58 encoded string

u64 - required - Amount of lamports to airdrop

object - optional - Configuration object

#### **Returns:**

string - Transaction Signature of the airdrop, as a base-58 encoded string

Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "requestAirdrop",
     "params": [
       "83astBRguLMdt2h5U1Tpdq5tjFoJ6noeGwaY3mDLVcri",
       1000000000,
       {
         "commitment": "finalized"
       }
     ]
   }
'

// Result

```
{% endcode %}
