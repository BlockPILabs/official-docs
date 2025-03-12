---
description: Retrieves hashTreeRoot of BeaconBlock/BeaconBlockHeader
---

# /eth/v1/beacon/blocks/{block\_id}/root

#### P**arameters:**

**block\_id-string**, Block identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", , \<hex encoded blockRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/blocks/head/root


// Result
{
    "execution_optimistic": false,
    "finalized": false,
    "data": {
        "root": "0xc60c1a57d32e78ebbc1a813fd84cabcbc7c3287a1ab7482438d6987953b83174"
    }
}
```
{% endcode %}
