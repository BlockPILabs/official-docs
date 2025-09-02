---
description: Return structured representations of all modules in the given package
---

# sui\_getNormalizedMoveModulesByPackage

#### **Parameters:**

**package< ObjectID >**&#x20;

#### **Returns:**

BTreeMap\<String,SuiMoveNormalizedModule>< SuiMoveNormalizedModule >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getNormalizedMoveModulesByPackage",
  "params": [
    "0xece356d10d89e75f565b0934851ba8d5bc59462a46078b90f1f508a1e4fd4eed"
  ]
}'

// Result

```
{% endcode %}
