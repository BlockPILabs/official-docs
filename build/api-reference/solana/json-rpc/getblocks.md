---
description: Returns a list of confirmed blocks between two slots
---

# getBlocks

#### **Parameters:**

u64 - required - Start slot

u64 - optional - End slot (must be no more than 500,000 blocks higher than the `start_slot`)

object - optional - Configuration object

#### **Returns:**

array - An array of u64 integers listing confirmed blocks between `start_slot` and either `end_slot` - if provided, or latest confirmed slot, inclusive. Max range allowed is 500,000 slots.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getBlocks",
     "params": [
       5,
       10,
       {
         "commitment": "finalized"
       }
     ]
   }
'

// Result

```
{% endcode %}
