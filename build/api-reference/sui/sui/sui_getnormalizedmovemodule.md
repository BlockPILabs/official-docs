---
description: Return a structured representation of Move module
---

# sui\_getNormalizedMoveModule

#### **Parameters:**

**package< ObjectID >**&#x20;

**module\_name< string >**&#x20;

#### **Returns:**

SuiMoveNormalizedModule< SuiMoveNormalizedModule >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getNormalizedMoveModule",
  "params": [
    "0x16dc6797cf787c839a07edc03e633842109123618df6438d21a48040e6bb568c",
    "module"
  ]
}'

// Result

```
{% endcode %}
