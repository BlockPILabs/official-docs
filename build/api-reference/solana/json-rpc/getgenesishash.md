---
description: Returns the genesis hash
---

# getGenesisHash

#### **Parameters:**

None

#### **Returns:**

string - A Hash as base-58 encoded string

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getGenesisHash"
   }
'

// Result

```
{% endcode %}
