---
description: Return the first four bytes of the chain's genesis checkpoint digest.
---

# sui\_getChainIdentifier

#### **Parameters:**

**None**

#### **Returns:**

String< string >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getChainIdentifier",
  "params": []
}'

// Result
{
    "jsonrpc": "2.0",
    "result": "35834a8a",
    "id": 1
}
```
{% endcode %}
