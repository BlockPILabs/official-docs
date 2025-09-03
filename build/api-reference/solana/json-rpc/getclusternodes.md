---
description: Returns information about all the nodes participating in the cluster
---

# getClusterNodes

#### **Parameters:**

None

#### **Returns:**

array - The result field will be an array of JSON objects

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getClusterNodes"
   }
'

// Result

```
{% endcode %}
