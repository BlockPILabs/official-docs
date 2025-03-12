---
description: >-
  Retrieves block headers matching given query. By default it will fetch current
  head slot blocks.
---

# /eth/v1/beacon/headers

#### P**arameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/headers


// Result
{
    "execution_optimistic": false,
    "finalized": false,
    "data": [
        {
            "root": "0x221197ac0e8df04f7257e0fb5d19d3308c35bcd0b983e0282555573bcb9e1cc1",
            "canonical": true,
            "header": {
                "message": {
                    "slot": "9085002",
                    "proposer_index": "1163441",
                    "parent_root": "0xecc9d85acaf7f3cdb4f2b3e6d972143be3f4997dbbfe4904a7ba95cd7189cc5d",
                    "state_root": "0x7b32b1b8310d3ff01ad662886c7d94f533bc955b7f913de5cd0ea25b7cbf4f8a",
                    "body_root": "0x0f2fed039b9389bc0c8139c1dbf0c9ba3bb66965502b9b94eb30148a30f9f808"
                },
                "signature": "0xb4ee1295c7bb99b0ef76e5f8b19458819626cb5fee8e561184b95f9a8c7c3cf901b873b23d649cf0b28aca183d6f39e518097c0b562b3925df45072ab459209abba7ccab080aec8d30c7ecdc2655979a83894ff99b71ce032ccb690b558a438d"
            }
        }
    ]
}
```
{% endcode %}
