---
description: Returns the lowest slot that the node has information about in its ledger.
---

# minimumLedgerSlot

#### **Parameters:**

None

#### **Returns:**

u64 - The minimum ledger slot number

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "minimumLedgerSlot"
   }
'

// Result

```
{% endcode %}
