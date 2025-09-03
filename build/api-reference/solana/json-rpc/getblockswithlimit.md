---
description: Returns a list of confirmed blocks starting at the given slot
---

# getBlocksWithLimit

#### **Parameters:**

u64 - required - Start slot

u64 - optional - Limit (must be no more than 500,000 blocks higher than the `start_slot`)

object - optional - Configuration object

#### **Returns:**

array - An array of u64 integers listing confirmed blocks starting at `start_slot` for up to `limit` blocks, inclusive.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getBlocksWithLimit",
     "params": [
       5,
       3
     ],
     {
       "commitment": "finalized"
     }
   }
'

// Result

```
{% endcode %}
