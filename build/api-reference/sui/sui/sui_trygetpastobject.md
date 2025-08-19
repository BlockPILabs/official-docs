# sui\_tryGetPastObject

Note there is no software-level guarantee/SLA that objects with past versions can be retrieved by this API, even if the object and version exists/existed. The result may vary across nodes depending on their pruning policies. Return the object information for a specified version

#### **Parameters:**

**object\_ids<\[ ObjectID ]>** - The IDs of the queried objects&#x20;

**version< SequenceNumber >** - The version of the queried object. If None, default to the latest known version&#x20;

**options< ObjectDataOptions >** - Options for specifying the content to be returned

#### **Returns:**

SuiPastObjectResponse< ObjectRead >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_tryGetPastObject",
  "params": [
    "0x11af4b844ff94b3fbef6e36b518da3ad4c5856fa686464524a876b463d129760",
    4,
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
    "result": {
        "status": "ObjectNotExists",
        "details": "0x11af4b844ff94b3fbef6e36b518da3ad4c5856fa686464524a876b463d129760"
    },
    "id": 1
}
```
{% endcode %}
