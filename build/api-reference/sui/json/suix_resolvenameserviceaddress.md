---
description: Return the resolved address given resolver and name
---

# suix\_resolveNameServiceAddress

#### **Parameters:**

**name< string >** - The name to resolve

#### **Returns:**

SuiAddress< SuiAddress >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_resolveNameServiceAddress",
  "params": [
    "example.sui"
  ]
}'

// Result

```
{% endcode %}
