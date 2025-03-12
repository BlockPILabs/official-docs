---
description: /cosmos/staking/v1beta1/validators/{validator_addr}/unbonding_delegations
---

# /cosmos/staking/v1beta1/validators/{validator\_addr}/unbonding\_delegations

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/validators/cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p/unbonding_delegations

// Result
{
    "unbonding_responses": [
        {
            "delegator_address": "cosmos1rwacecm06qaleed52sszajandyenjkdf0c6n6c",
            "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
            "entries": [
                {
                    "creation_height": "13811912",
                    "completion_time": "2023-02-15T11:03:01.397405310Z",
                    "initial_balance": "35000000",
                    "balance": "35000000"
                }
            ]
        },
        {
            "delegator_address": "cosmos1ywkxynljd0hzk2ftsu9rze85pflh2crz99gwcp",
            "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
            "entries": [
                {
                    "creation_height": "14069168",
                    "completion_time": "2023-03-06T18:32:18.274049045Z",
                    "initial_balance": "204235475",
                    "balance": "204235475"
                }
            ]
        },
        {
            "delegator_address": "cosmos1ymvwpvzqr8nt80pjrzqhlqc4fv4p8cr5xasph9",
            "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
            "entries": [
                {
                    "creation_height": "13974844",
                    "completion_time": "2023-02-27T20:31:54.796613924Z",
                    "initial_balance": "20000000",
                    "balance": "20000000"
                }
            ]
        },
        {
            "delegator_address": "cosmos1xnh88r2ut5nuksv3lkt6w5047f63slrmm7r3g5",
            "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
            "entries": [
                {
                    "creation_height": "14001625",
                    "completion_time": "2023-03-01T19:37:32.426914596Z",
                    "initial_balance": "23007656",
                    "balance": "23007656"
                }
            ]
        },
        {
            "delegator_address": "cosmos15vfv0agnst36xljczdtylt8sd7hat2v6xz8n7m",
            "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
            "entries": [
                {
                    "creation_height": "13985880",
                    "completion_time": "2023-02-28T15:56:23.086083113Z",
                    "initial_balance": "9836553",
                    "balance": "9836553"
                }
            ]
        },
        {
            "delegator_address": "cosmos14h9t4gaf2gsy765g929mz9ac2762zn8j2zkysg",
            "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
            "entries": [
                {
                    "creation_height": "13904647",
                    "completion_time": "2023-02-22T12:33:37.306955163Z",
                    "initial_balance": "2500000",
                    "balance": "2500000"
                }
            ]
        },
        {
            "delegator_address": "cosmos16aqhazk96f8hq0r2mw9krlsnyf07nxdt7mlevs",
            "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
            "entries": [
                {
                    "creation_height": "13823762",
                    "completion_time": "2023-02-16T08:14:28.577748800Z",
                    "initial_balance": "16000000",
                    "balance": "16000000"
                }
            ]
        },
        {
            "delegator_address": "cosmos1m8kuukjn97uk78hv3c548z46y3qz95ehh52s5q",
            "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
            "entries": [
                {
                    "creation_height": "13895024",
                    "completion_time": "2023-02-21T18:37:26.432062176Z",
                    "initial_balance": "50000",
                    "balance": "50000"
                }
            ]
        },
        {
            "delegator_address": "cosmos1lu7fl37yrxvqc2qw8x8lwgkttcln4k8yac2876",
            "validator_address": "cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p",
            "entries": [
                {
                    "creation_height": "13896544",
                    "completion_time": "2023-02-21T21:27:17.854989013Z",
                    "initial_balance": "10010000",
                    "balance": "10010000"
                }
            ]
        }
    ],
    "pagination": {
        "next_key": null,
        "total": "9"
    }
}
```
{% endcode %}
