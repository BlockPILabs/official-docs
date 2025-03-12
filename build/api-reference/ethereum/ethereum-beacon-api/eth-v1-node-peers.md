---
description: >-
  Retrieves data about the node's network peers. By default this returns all
  peers. Multiple query params are combined using AND conditions
---

# /eth/v1/node/peers



#### Parameters:

**None**



#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/node/peers

// Result
{
    "data": [
        {
            "peer_id": "16Uiu2HAmBuGPDp8sErJk5L8NTmXHY9q2udF5FBdmQJW4sP4JTZcv",
            "enr": null,
            "last_seen_p2p_address": "/ip4/184.160.96.39/tcp/13103",
            "state": "disconnected",
            "direction": "inbound"
        },
        {
            "peer_id": "16Uiu2HAmCJWsQ9znN6wAfpS5hR3rc9cApHo4aHeJr9oDw5G6ndgF",
            "enr": "enr:-Ma4QMCILD_4E1-2t6t_3Jgnz41_hBOtnseUSAlZl9Kd4D9VKOjnUPmo_xL_CYfdAskg4Rbae8qCIKJBxnE5O2x-SseCAVSHYXR0bmV0c4gAAAAAAAAAA4RldGgykGqVoakEAAAA__________-CaWSCdjSCaXCELN8Ex4RxdWljgiMpiXNlY3AyNTZrMaEC-sFPpQg1JBQY1GbIzPP0h4qwp3hlr3h653BadekO4KyIc3luY25ldHMAg3RjcIIjKIN1ZHCCIyg",
            "last_seen_p2p_address": "/ip4/44.223.4.199/tcp/9000/p2p/16Uiu2HAmCJWsQ9znN6wAfpS5hR3rc9cApHo4aHeJr9oDw5G6ndgF",
            "state": "disconnected",
            "direction": "outbound"
        },
        ......
```
{% endcode %}
