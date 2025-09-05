---
description: ClientState queries an IBC light client.
---

# /ibc/core/client/v1/client\_states/{client\_id}

#### **Parameters:**

**client\_id - string**, client state unique identifier

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/ibc/core/client/v1/client_states/07-tendermint-0

// Result
{
    "client_state": {
        "@type": "/ibc.lightclients.tendermint.v1.ClientState",
        "chain_id": "okwme",
        "trust_level": {
            "numerator": "1",
            "denominator": "3"
        },
        "trusting_period": "1209600s",
        "unbonding_period": "1814400s",
        "max_clock_drift": "600s",
        "frozen_height": {
            "revision_number": "0",
            "revision_height": "0"
        },
        "latest_height": {
            "revision_number": "0",
            "revision_height": "20"
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
        "allow_update_after_expiry": false,
        "allow_update_after_misbehaviour": false
    },
    "proof": null,
    "proof_height": {
        "revision_number": "4",
        "revision_height": "14099411"
    }
}
```
{% endcode %}
