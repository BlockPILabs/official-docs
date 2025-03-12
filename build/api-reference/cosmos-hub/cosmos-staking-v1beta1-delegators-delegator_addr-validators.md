---
description: DelegatorValidators queries all validators info for given delegator address.
---

# /cosmos/staking/v1beta1/delegators/{delegator\_addr}/validators

#### **Parameters:**

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/delegators/cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9/validators

// Result
{
    "validators": [
        {
            "operator_address": "cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf",
            "consensus_pubkey": {
                "@type": "/cosmos.crypto.ed25519.PubKey",
                "key": "T2/RQlkfKOBz6eCt/drq8pCIQUPmk2e8QFJ39IsA96M="
            },
            "jailed": false,
            "status": "BOND_STATUS_BONDED",
            "tokens": "1327187181968",
            "delegator_shares": "1327319911492.666342752078967754",
            "description": {
                "moniker": "strangelove-ventures",
                "identity": "D0D8B80F1C5C70B5",
                "website": "https://strangelove.ventures",
                "security_contact": "",
                "details": "'You must construct additional pylons' -StarCraft"
            },
            "unbonding_height": "8270293",
            "unbonding_time": "2021-11-28T03:09:15.865885008Z",
            "commission": {
                "commission_rates": {
                    "rate": "0.050000000000000000",
                    "max_rate": "0.150000000000000000",
                    "max_change_rate": "0.100000000000000000"
                },
                "update_time": "2021-03-19T18:29:44.287558408Z"
            },
            "min_self_delegation": "1"
        },
        ......
    ],
    "pagination": {
        "next_key": null,
        "total": "3"
    }
}
```
{% endcode %}
