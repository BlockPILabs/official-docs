---
description: Retrieves data about the given peer
---

# /eth/v1/node/peers/{peer\_id}



#### Parameters:

**peer\_id-string**,&#x20;



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/node/peers/16Uiu2HAmBuGPDp8sErJk5L8NTmXHY9q2udF5FBdmQJW4sP4JTZcv

// Result
{
    "data": {
        "peer_id": "16Uiu2HAmBuGPDp8sErJk5L8NTmXHY9q2udF5FBdmQJW4sP4JTZcv",
        "enr": null,
        "last_seen_p2p_address": "/ip4/184.160.96.39/tcp/13103",
        "state": "disconnected",
        "direction": "inbound"
    }
}
```
{% endcode %}
