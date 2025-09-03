---
description: Returns the slot leaders for a given slot range
---

# getSlotLeaders

#### **Parameters:**

u64 - required - Start slot, as u64 integer

u64 - required - Limit, as u64 integer (between 1 and 5,000)

#### **Returns:**

array - Array of Node identity public keys as base-58 encoded strings.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getSlotLeaders",
     "params": [
       100,
       10
     ]
   }
'

// Result

```
{% endcode %}
