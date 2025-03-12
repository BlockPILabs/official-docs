---
description: Retrieve block reward info for a single block
---

# /eth/v1/beacon/rewards/blocks/{block\_id}

#### Parameters:

**block\_id-string**, Block identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", , \<hex encoded blockRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/rewards/blocks/head



// Result
{
    "execution_optimistic": false,
    "finalized": false,
    "data": {
        "proposer_index": "197627",
        "total": "44337971",
        "attestations": "42791096",
        "sync_aggregate": "1546875",
        "proposer_slashings": "0",
        "attester_slashings": "0"
    }
}
```
{% endcode %}
