---
description: HistoricalInfo queries the historical info for given height.
---

# /cosmos/staking/v1beta1/historical\_info/{height}

#### **Parameters:**

**height-string,** height defines at which height to query the historical info.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/historical_info/14077307

// Result
{
    "hist": {
        "header": {
            "version": {
                "block": "11",
                "app": "0"
            },
            "chain_id": "cosmoshub-4",
            "height": "14077307",
            "time": "2023-02-14T08:54:59.091941079Z",
            "last_block_id": {
                "hash": "Um1RccH/5VgdJaLPBJ8ZnkxaLxjckucVBXm9WCTJYHs=",
                "part_set_header": {
                    "total": 1,
                    "hash": "j/r8aF+Ljsim1DZd9CEtcFuMhbMOj1f7xysSjrCDbzA="
                }
            },
            "last_commit_hash": "O3Zax2R4kY7wkAME7wdzADhCDjuZVucG2UESoxmjoKI=",
            "data_hash": "j9+apJJX6+87yfXn+XbN8OhAhu9EUS1fkjEWp8ysj4E=",
            "validators_hash": "9H3TlYoW3+1sL8VpHOH76iTRC9imhLLlrQCDdbiVxck=",
            "next_validators_hash": "9H3TlYoW3+1sL8VpHOH76iTRC9imhLLlrQCDdbiVxck=",
            "consensus_hash": "gDZJZbfCzJ3pYcCZi0en+T8ZcAd+uILg7Rw4IkCIiMc=",
            "app_hash": "0+W3QjNuXQt4vEHVcW44UCiTpBwYpQl5r1au3bNcuFI=",
            "last_results_hash": "YwDe07O0dlCq4Zinj970PxkIimihdIxDKvtkDAF+I4E=",
            "evidence_hash": "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
            "proposer_address": "sRZ9BDfbnfDVM+4qzeSBBxOb3S4="
        },
        "valset": [
            {
                "operator_address": "cosmosvaloper1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u2lcnj0",
                "consensus_pubkey": {
                    "@type": "/cosmos.crypto.ed25519.PubKey",
                    "key": "0kNlxBMpm+5WtfHIG1xsWatOXTKPLtmSqn3EiEIDZeI="
                },
                "jailed": false,
                "status": "BOND_STATUS_BONDED",
                "tokens": "12503774599723",
                "delegator_shares": "12503774599723.000000000000000000",
                "description": {
                    "moniker": "🐠stake.fish",
                    "identity": "90B597A673FC950E",
                    "website": "stake.fish",
                    "security_contact": "",
                    "details": "We are the leading staking service provider for blockchain projects. Join our community to help secure networks and earn rewards. We know staking."
                },
                "unbonding_height": "0",
                "unbonding_time": "1970-01-01T00:00:00Z",
                "commission": {
                    "commission_rates": {
                        "rate": "0.040000000000000000",
                        "max_rate": "1.000000000000000000",
                        "max_change_rate": "0.010000000000000000"
                    },
                    "update_time": "2019-03-13T23:00:00Z"
                },
                "min_self_delegation": "1"
            },
            ......
        ]
    }
}
```
{% endcode %}
