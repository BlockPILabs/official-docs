---
description: Retrieves block header for given block id.
---

# /eth/v1/beacon/headers/{block\_id}

#### P**arameters:**

**block\_id-string**, Block identifier. Can be one of: "head" (canonical head in node's view), "genesis", "finalized", , \<hex encoded blockRoot with 0x prefix>.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/headers/head


// Result
{
    "execution_optimistic": false,
    "finalized": false,
    "data": {
        "root": "0x62466b2370cb6ff5c379e52ca3abbc2d14230ef3a9bd38558923884eebf1d424",
        "canonical": true,
        "header": {
            "message": {
                "slot": "9085022",
                "proposer_index": "102734",
                "parent_root": "0x222077bf3b706b5bd7684191d832b68a345f7b673dc34e963c64e0e9c5f46de7",
                "state_root": "0x3b0ddb96a21c0e528db7793cc8fdf3d37e3dadd37900d133710efa7dd3491308",
                "body_root": "0x3a0f5fb9f743c2692ca54198891afb48f34740e81bf84eceb7f80a1eb9b1d0fe"
            },
            "signature": "0xb15b3f226e0a707a065aad78e795018ea806f6af9a54666d1b5a45781fb910a1666c3b42d27975b4481c9d3798ed522d0467247e1065a4134529c3294a4f620fa4183c15e84b07bc08eaeae679c21133fe92f4ba27bf68fa85db53c8915206f3"
        }
    }
}
```
{% endcode %}
