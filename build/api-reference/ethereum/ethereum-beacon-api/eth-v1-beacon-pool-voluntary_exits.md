---
description: >-
  Retrieves voluntary exits known by the node but not necessarily incorporated
  into any block
---

# /eth/v1/beacon/pool/voluntary\_exits

#### Parameters:

None



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/pool/voluntary_exits

// Result
{
    "data": [
        {
            "message": {
                "epoch": "273119",
                "validator_index": "1198198"
            },
            "signature": "0x8e9f440703d0d9a4ef22a665a59759f5b4b33e3d068aaac297e124af8854fd5b1593cdd022734910c748dbe3791ae882135daec5ec761809ec4d6a31796e0b5dbf55824ee2d0b36ef02bdc81baf64614d4f536832ee5a307e145616d673620eb"
        },
        ......
```
{% endcode %}
