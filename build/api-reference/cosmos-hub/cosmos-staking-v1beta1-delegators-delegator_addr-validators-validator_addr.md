---
description: DelegatorValidator queries validator info for given delegator validator pair.
---

# /cosmos/staking/v1beta1/delegators/{delegator\_addr}/validators/{validator\_addr}

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

**validator\_address - string**, validator\_address defines the validator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/delegators/cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9/validators/cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq

// Result
{
    "validator": {
        "operator_address": "cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq",
        "consensus_pubkey": {
            "@type": "/cosmos.crypto.ed25519.PubKey",
            "key": "t9l8HjwxL8WVwanxbZTOv7YNeUIp5EnMwg2xaVgi8I0="
        },
        "jailed": false,
        "status": "BOND_STATUS_BONDED",
        "tokens": "1065431041035",
        "delegator_shares": "1065431041035.000000000000000000",
        "description": {
            "moniker": "Stakecito",
            "identity": "D16E26E5C8154E17",
            "website": "",
            "security_contact": "",
            "details": "Securing & Decentralizing PoS Networks."
        },
        "unbonding_height": "0",
        "unbonding_time": "1970-01-01T00:00:00Z",
        "commission": {
            "commission_rates": {
                "rate": "0.050000000000000000",
                "max_rate": "0.200000000000000000",
                "max_change_rate": "0.010000000000000000"
            },
            "update_time": "2021-04-30T17:56:30.783593817Z"
        },
        "min_self_delegation": "1"
    }
}
```
{% endcode %}
