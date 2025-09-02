---
description: Return a structured representation of Move struct
---

# sui\_getNormalizedMoveStruct

#### **Parameters:**

**package< ObjectID >**&#x20;

**module\_name< string >**&#x20;

**struct\_name< string >**&#x20;

#### **Returns:**

SuiMoveNormalizedStruct< SuiMoveNormalizedStruct >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getNormalizedMoveStruct",
  "params": [
    "0x46c25c211cb35c05d801c769b78770474957b37379c527753c5c8ab783f697e7",
    "module",
    "StructName"
  ]
}'

// Result

```
{% endcode %}
