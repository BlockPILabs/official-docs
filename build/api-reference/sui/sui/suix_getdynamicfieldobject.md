---
description: Return the dynamic field object information for a specified object
---

# suix\_getDynamicFieldObject

#### **Parameters:**

**parent\_object\_id< ObjectID >** -The ID of the queried parent object

**name< DynamicFieldName >** -The Name of the dynamic field

#### **Returns:**

SuiObjectResponse< SuiObjectResponse >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getDynamicFieldObject",
  "params": [
    "0xc8359b6b5e3bfeab524e5edaad3a204b4053745b2d45d1f00cd8d24e5b697607",
    {
      "type": "0x0000000000000000000000000000000000000000000000000000000000000009::test::TestField",
      "value": "some_value"
    }
  ]
}'

// Result

```
{% endcode %}
