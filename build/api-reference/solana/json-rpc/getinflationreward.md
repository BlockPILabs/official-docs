---
description: Returns the inflation / staking reward for a list of addresses for an epoch
---

# getInflationReward

#### **Parameters:**

array - optional - An array of addresses to query, as base-58 encoded strings

object - optional - Configuration object

#### **Returns:**

array - The result field will be a JSON array of objects

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getInflationReward",
     "params": [
       [
         "6dmNQ5jwLeLk5REvio1JcMshcbvkYMwy26sJ8pbkvStu",
         "BGsqMegLpV6n6Ve146sSX2dTjUMj3M92HnU8BbNRMhF2"
       ],
       {
         "epoch": 800,
         "commitment": "finalized"
       }
     ]
   }
'

// Result

```
{% endcode %}
