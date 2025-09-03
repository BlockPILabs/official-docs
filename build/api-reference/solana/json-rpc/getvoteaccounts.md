---
description: >-
  Returns the account info and associated stake for all the voting accounts in
  the current bank.
---

# getVoteAccounts

#### **Parameters:**

object - optional - Configuration object

#### **Returns:**

object - The result field will be a JSON object of `current` and `delinquent` accounts, each containing an array of JSON objects

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getVoteAccounts",
     "params": [
       {
         "commitment": "finalized",
         "votePubkey": "i7NyKBMJCA9bLM2nsGyAGCKHECuR2L5eh4GqFciuwNT"
       }
     ]
   }
'

// Result

```
{% endcode %}
