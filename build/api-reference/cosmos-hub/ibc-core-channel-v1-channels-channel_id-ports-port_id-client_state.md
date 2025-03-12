---
description: >-
  ChannelClientState queries for the client state for the channel associated
  with the provided channel identifiers.
---

# /ibc/core/channel/v1/channels/{channel\_id}/ports/{port\_id}/client\_state

#### **Parameters:**

**channel\_id - string**, channel unique identifier

**port\_id - string**, port unique identifier

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/core/channel/v1/channels/channel-370/ports/icahost/client_state

// Result
{
    "identified_client_state": {
        "client_id": "07-tendermint-892",
        "client_state": {
            "@type": "/ibc.lightclients.tendermint.v1.ClientState",
            "chain_id": "stafihub-1",
            "trust_level": {
                "numerator": "1",
                "denominator": "3"
            },
            "trusting_period": "806400s",
            "unbonding_period": "1209600s",
            "max_clock_drift": "60s",
            "frozen_height": {
                "revision_number": "0",
                "revision_height": "0"
            },
            "latest_height": {
                "revision_number": "1",
                "revision_height": "2724066"
            },
            "proof_specs": [
                {
                    "leaf_spec": {
                        "hash": "SHA256",
                        "prehash_key": "NO_HASH",
                        "prehash_value": "SHA256",
                        "length": "VAR_PROTO",
                        "prefix": "AA=="
                    },
                    "inner_spec": {
                        "child_order": [
                            0,
                            1
                        ],
                        "child_size": 33,
                        "min_prefix_length": 4,
                        "max_prefix_length": 12,
                        "empty_child": null,
                        "hash": "SHA256"
                    },
                    "max_depth": 0,
                    "min_depth": 0
                },
                {
                    "leaf_spec": {
                        "hash": "SHA256",
                        "prehash_key": "NO_HASH",
                        "prehash_value": "SHA256",
                        "length": "VAR_PROTO",
                        "prefix": "AA=="
                    },
                    "inner_spec": {
                        "child_order": [
                            0,
                            1
                        ],
                        "child_size": 32,
                        "min_prefix_length": 1,
                        "max_prefix_length": 1,
                        "empty_child": null,
                        "hash": "SHA256"
                    },
                    "max_depth": 0,
                    "min_depth": 0
                }
            ],
            "upgrade_path": [
                "upgrade",
                "upgradedIBCState"
            ],
            "allow_update_after_expiry": true,
            "allow_update_after_misbehaviour": true
        }
    },
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
