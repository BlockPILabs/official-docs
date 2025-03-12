---
description: Submit an unbonding delegation
---

# /staking/delegators/{delegator\_addr}/unbonding\_delegations

#### **Parameters:**

**delegatorAddr - string**, Bech32 AccAddress of Delegator

**delegation- object**, Unbond an amount of bonded shares from a validator

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/staking/delegators/cosmos1j52fnrad494smwjp3l7tg4ng96s2kmzd9kgue9/unbonding_delegations
{
  "base_req": {
    "from": "cosmos1g9ahr6xhht5rmqven628nklxluzyv8z9jqjcmc",
    "memo": "Sent via Cosmos Voyager ð",
    "chain_id": "Cosmos-Hub",
    "account_number": "0",
    "sequence": "1",
    "gas": "200000",
    "gas_adjustment": "1.2",
    "fees": [
      {
        "denom": "stake",
        "amount": "50"
      }
    ],
    "simulate": false
  },
  "delegator_address": "cosmos1depk54cuajgkzea6zpgkq36tnjwdzv4afc3d27",
  "validator_address": "cosmosvaloper16xyempempp92x9hyzz9wrgf94r6j9h5f2w4n2l",
  "amount": {
    "denom": "stake",
    "amount": "50"
  }
}

// Result
{
  "msg": [
    "string"
  ],
  "fee": {
    "gas": "string",
    "amount": [
      {
        "denom": "stake",
        "amount": "50"
      }
    ]
  },
  "memo": "string",
  "signature": {
    "signature": "MEUCIQD02fsDPra8MtbRsyB1w7bqTM55Wu138zQbFcWx4+CFyAIge5WNPfKIuvzBZ69MyqHsqD8S1IwiEp+iUb6VSdtlpgY=",
    "pub_key": {
      "type": "tendermint/PubKeySecp256k1",
      "value": "Avz04VhtKJh8ACCVzlI8aTosGy0ikFXKIVHQ3jKMrosH"
    },
    "account_number": "0",
    "sequence": "0"
  }
}
```
{% endcode %}
