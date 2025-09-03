---
description: Get the max slot seen from retransmit stage.
---

# getMaxRetransmitSlot

#### **Parameters:**

None

#### **Returns:**

u64 - Slot number

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getMaxRetransmitSlot"
   }
'

// Result

```
{% endcode %}
