---
description: >-
  Returns identity and transaction information about a confirmed block in the
  ledger
---

# getBlock

#### **Parameters:**

u64 - required - Slot number.

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
     "method": "getBlock",
     "params": [
       378967388,
       {
         "commitment": "finalized",
         "encoding": "json",
         "transactionDetails": "full",
         "maxSupportedTransactionVersion": 0,
         "rewards": false
       }
     ]
   }
'

// Result

```
{% endcode %}
