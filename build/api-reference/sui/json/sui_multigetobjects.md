---
description: Return the object data for a list of objects
---

# sui\_multiGetObjects

#### **Parameters:**

**object\_ids<\[ ObjectID ]>** - The IDs of the queried objects&#x20;

**options< ObjectDataOptions >** - Options for specifying the content to be returned

#### **Returns:**

Vec\<SuiObjectResponse><\[ SuiObjectResponse ]>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_multiGetObjects",
  "params": [
    [
      "0xb61439368cd75ebe63d633af32ffb4a022d18b95b4eaa9fd3b22b43f6b2c8e92",
      "0x6ea7bed8f6c3d80f2a595c2305e12dd6d07c3fbbd3ebef7dbcc7b02346cdf056",
      "0x75da5e934f672d3da3e003d989075efaecc79b5cd5df0df2a168259b7115a41c",
      "0x38554a9ff7b4f6b59f9426c321c8013afed093481dd4ef1267c67a8e9a0d074f",
      "0xe74d1b250d5df2cb5170782a8a438fbf681eded4d1e0a2cd7dfb27e784493fb1"
    ],
    {
      "showType": true,
      "showOwner": true,
      "showPreviousTransaction": true,
      "showDisplay": false,
      "showContent": true,
      "showBcs": false,
      "showStorageRebate": true
    }
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": [
        {
            "error": {
                "code": "notExists",
                "object_id": "0xb61439368cd75ebe63d633af32ffb4a022d18b95b4eaa9fd3b22b43f6b2c8e92"
            }
        },
        {
            "error": {
                "code": "notExists",
                "object_id": "0x6ea7bed8f6c3d80f2a595c2305e12dd6d07c3fbbd3ebef7dbcc7b02346cdf056"
            }
        },
        ......
```
{% endcode %}
