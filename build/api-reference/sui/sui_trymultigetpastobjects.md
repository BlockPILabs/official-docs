# sui\_tryMultiGetPastObjects

Note there is no software-level guarantee/SLA that objects with past versions can be retrieved by this API, even if the object and version exists/existed. The result may vary across nodes depending on their pruning policies. Return the object information for a specified version

#### **Parameters:**

**past\_objects<\[ GetPastObjectRequest ]>** - A vector of object and versions to be queried

**options< ObjectDataOptions >** - Options for specifying the content to be returned

#### **Returns:**

Vec<\[ ObjectRead ]>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_tryMultiGetPastObjects",
  "params": [
    [
      {
        "objectId": "0x5056aa3325512c8af40b9f5fd7065c83ded900657eac70a7979c2541646fa449",
        "version": "4"
      },
      {
        "objectId": "0xe81109dc075f537067726d63dd5287100e177404a969989215da2abfbfc098cf",
        "version": "12"
      }
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
            "status": "ObjectNotExists",
            "details": "0x5056aa3325512c8af40b9f5fd7065c83ded900657eac70a7979c2541646fa449"
        },
        {
            "status": "ObjectNotExists",
            "details": "0xe81109dc075f537067726d63dd5287100e177404a969989215da2abfbfc098cf"
        }
    ],
    "id": 1
}
```
{% endcode %}
