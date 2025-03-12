---
description: Return the object information for a specified object
---

# sui\_getObject

#### **Parameters:**

**object\_id< ObjectID >** - The ID of the queried object&#x20;

**options< ObjectDataOptions >** - Options for specifying the content to be returned

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
  "method": "sui_getObject",
  "params": [
    "0x75eb1006f1e73fea9c467ddce8bf6aa7efa350bc59ea9197e2ec47e599d94dd2",
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
        "data": {
            "objectId": "0x75eb1006f1e73fea9c467ddce8bf6aa7efa350bc59ea9197e2ec47e599d94dd2",
            "version": "229910049",
            "digest": "9jnsLZhRFmtPsmu34JL8K4SjqCmfPiSAPGnWKfJgx2k6",
            "type": "0x2::coin::Coin<0xa8816d3a6e3136e86bc2873b1f94a15cadc8af2703c075f2d546c2ae367f4df9::ocean::OCEAN>",
            "owner": {
                "AddressOwner": "0xe648f4e05742e27e99eb8d8778862c1ffb97038a143b73d200647276a37cf2ad"
            },
            "previousTransaction": "FngHthKGR852Y6tUU57UPLDzqFyKLyJ5EfwinSzVYEYn",
            "storageRebate": "1337600",
            "content": {
                "dataType": "moveObject",
                "type": "0x2::coin::Coin<0xa8816d3a6e3136e86bc2873b1f94a15cadc8af2703c075f2d546c2ae367f4df9::ocean::OCEAN>",
                "hasPublicTransfer": true,
                "fields": {
                    "balance": "62500000",
                    "id": {
                        "id": "0x75eb1006f1e73fea9c467ddce8bf6aa7efa350bc59ea9197e2ec47e599d94dd2"
                    }
                }
            }
        }
    },
    "id": 1
}
```
{% endcode %}
