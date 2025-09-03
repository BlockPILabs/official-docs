---
description: Returns all information associated with the account of provided Pubkey
---

# getAccountInfo

#### **Parameters:**

string - required - Pubkey of account to query, as base-58 encoded string.

object - optional - Configuration object.

#### **Returns:**

object - If the requested account doesn't exist result will be `null`.&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
  {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getAccountInfo",
    "params": [
      "vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg",
      {
        "commitment": "finalized",
        "encoding": "base58"
      }
    ]
  }
'

// Result

```
{% endcode %}
