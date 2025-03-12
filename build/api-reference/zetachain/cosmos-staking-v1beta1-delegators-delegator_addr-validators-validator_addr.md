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
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/delegators/zeta1tzflr0lc0s9fxpx2h6770uj0z7jlk0q3smulpv/validators/zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r

// Result
{
  "validator": {
    "operator_address": "zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r",
    "consensus_pubkey": {
      "@type": "/cosmos.crypto.ed25519.PubKey",
      "key": "pYQNipc5czjiOtf2EYB5JO5lHlXYK/RmH+npxXx15Z0="
    },
    "jailed": false,
    "status": "BOND_STATUS_BONDED",
    "tokens": "1100002000000000000002674",
    "delegator_shares": "1100002000000000000002674.000000000000000000",
    "description": {
      "moniker": "validator2",
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
      "update_time": "2022-11-17T16:26:37.029969767Z"
    },
    "min_self_delegation": "1"
  }
}
```
{% endcode %}
