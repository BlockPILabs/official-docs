---
description: >-
  Returns the slot of the lowest confirmed block that has not been purged from
  the ledger
---

# getFirstAvailableBlock

#### **Parameters:**

None

#### **Returns:**

u64 - Slot

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getFirstAvailableBlock"
   }
'

// Result

```
{% endcode %}
