---
description: Return a structured representation of Move function
---

# sui\_getNormalizedMoveFunction

#### **Parameters:**

**package< ObjectID >**&#x20;

**module< string >**&#x20;

**function< string >**&#x20;

#### **Returns:**

SuiMoveNormalizedFunction< SuiMoveNormalizedFunction >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getNormalizedMoveFunction",
  "params": [
    "0xb2582f82ab308bf9c96dfb22ec7345db1b5f14fdb2b9538efb160d31842e3a17",
    "moduleName",
    "functionName"
  ]
}'

// Result

```
{% endcode %}
