---
description: Returns the account information for a list of Pubkeys.
---

# getMultipleAccounts

#### **Parameters:**

array - required - An array of Pubkeys to query, as base-58 encoded strings (up to a maximum of 100)

object - optional - Configuration object

#### **Returns:**

array - the result will be an array containing either

* `null` - if the account at that Pubkey doesn't exist, or
* Account objects&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getMultipleAccounts",
     "params": [
       [
         "vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg",
         "4fYNw3dojWmQ4dXtSGE9epjRGy9pFSx62YypT7avPYvA"
       ],
       {
         "encoding": "base58",
         "commitment": "finalized"
       }
     ]
   }
'

// Result

```
{% endcode %}
