---
description: Returns the leader schedule for an epoch
---

# getLeaderSchedule

#### **Parameters:**

u64 - optional - Fetch the leader schedule for the epoch that corresponds to the provided slot. If unspecified, the leader schedule for the current epoch is fetched.

#### **Returns:**

object - Returns `null` if requested epoch is not found

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getLeaderSchedule",
     "params": [
       null,
       {
         "commitment": "processed",
         "identity": "dv2eQHeP4RFrJZ6UeiZWoc3XTtmtZCUKxxCApCDcRNV"
       }
     ]
   }
'

// Result

```
{% endcode %}
