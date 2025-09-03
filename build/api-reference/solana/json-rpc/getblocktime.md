---
description: Returns the estimated production time of a block.
---

# getBlockTime

#### **Parameters:**

u64 - required - Block number, identified by Slot

#### **Returns:**

i64 - Estimated production time, as Unix timestamp (seconds since the Unix epoch)

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getBlockTime",
     "params": [
       5
     ]
   }
'

// Result

```
{% endcode %}
