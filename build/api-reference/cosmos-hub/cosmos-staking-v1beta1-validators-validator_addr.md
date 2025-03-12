---
description: Validator queries validator info for given validator address.
---

# /cosmos/staking/v1beta1/validators/{validator\_addr}

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/validators/cosmosvaloper1qphf0ferqcch0jca9hlqfm3x0eds3dpkcvpafp

// Result
{
    "validator": {
        "operator_address": "cosmosvaloper1qphf0ferqcch0jca9hlqfm3x0eds3dpkcvpafp",
        "consensus_pubkey": {
            "@type": "/cosmos.crypto.ed25519.PubKey",
            "key": "voVoXB0ArzZ57NgZgyAhrwa0mVabPijeqT0ebQJYPPc="
        },
        "jailed": false,
        "status": "BOND_STATUS_UNBONDED",
        "tokens": "1000000",
        "delegator_shares": "1000000.000000000000000000",
        "description": {
            "moniker": "test kim",
            "identity": "",
            "website": "",
            "security_contact": "",
            "details": ""
        },
        "unbonding_height": "0",
        "unbonding_time": "1970-01-01T00:00:00Z",
        "commission": {
            "commission_rates": {
                "rate": "0.100000000000000000",
                "max_rate": "0.200000000000000000",
                "max_change_rate": "0.010000000000000000"
            },
            "update_time": "2022-12-20T07:59:27.494716670Z"
        },
        "min_self_delegation": "1000000"
    }
}
```
{% endcode %}
