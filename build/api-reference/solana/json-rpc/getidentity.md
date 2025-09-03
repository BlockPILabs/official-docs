---
description: Returns the identity pubkey for the current node
---

# getIdentity

#### **Parameters:**

None

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
     "method": "getIdentity"
   }
'

// Result

```
{% endcode %}
