---
description: Returns commitment for particular block
---

# getBlockCommitment

#### **Parameters:**

u64 - required - Block number, identified by Slot.

#### **Returns:**

object - The result field will be a JSON object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getBlockCommitment",
     "params": [
       5
     ]
   }
'

// Result

```
{% endcode %}
