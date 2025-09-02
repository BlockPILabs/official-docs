---
description: >-
  Return the resolved names given address, if multiple names are resolved, the
  first one is the primary name.
---

# suix\_resolveNameServiceNames

#### **Parameters:**

**address< SuiAddress >** - The address to resolve&#x20;

**cursor< ObjectID >**&#x20;

**limit< uint >**&#x20;

#### **Returns:**

Page\<String,ObjectID>< Page\_for\_String\_and\_ObjectID >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_resolveNameServiceNames",
  "params": [
    "0xb01f2f3f227a90090e6777f19aa10fd9e64e29dd4e8da119481d1a7c3c050dc5",
    "0x7d0cd09d3cc1679290f1df2803b32b76ba0395dbb635e3fb7390f04e6567f739",
    3
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "data": [],
        "nextCursor": null,
        "hasNextPage": false
    },
    "id": 1
}
```
{% endcode %}
