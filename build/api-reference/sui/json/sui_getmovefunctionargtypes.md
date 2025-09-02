---
description: Return the argument types of a Move function, based on normalized Type.
---

# sui\_getMoveFunctionArgTypes

#### **Parameters:**

**package< ObjectID >**&#x20;

**module< string >**&#x20;

**function< string >**&#x20;

#### **Returns:**

Vec<\[ MoveFunctionArgType ]>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getMoveFunctionArgTypes",
  "params": [
    "0x007efb0f94f1e64d2e8090c619a39299d87ee8070b5f56bb10bafa0e2261d819",
    "suifrens",
    "mint"
  ]
}'

// Result

```
{% endcode %}
