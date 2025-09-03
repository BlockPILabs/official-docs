---
description: Returns the current Solana version running on the node
---

# getVersion

#### **Parameters:**

None

#### **Returns:**

object - A JSON object&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getVersion"
   }
'

// Result

```
{% endcode %}

