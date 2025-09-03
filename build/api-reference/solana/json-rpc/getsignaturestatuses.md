---
description: >-
  Returns the statuses of a list of signatures. Each signature must be a txid,
  the first signature of a transaction.
---

# getSignatureStatuses

#### **Parameters:**

arrayr - equired - An array of transaction signatures to confirm, as base-58 encoded strings (up to a maximum of 256)

object - optional - Configuration object

#### **Returns:**

array - An array of `RpcResponse<object>` consisting of either `null` or an object&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getSignatureStatuses",
     "params": [
       [
         "5VERv8NMvzbJMEkV8xnrLkEaWRtSz9CosKDYjCJjBRnbJLgp8uirBgmQpjKhoR4tjF3ZpRzrFmBV6UjKdiSZkQUW"
       ],
       {
         "searchTransactionHistory": true
       }
     ]
   }
'

// Result

```
{% endcode %}
