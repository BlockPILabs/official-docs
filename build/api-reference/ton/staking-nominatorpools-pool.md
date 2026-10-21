# staking nominatorpools pool

Return details about the specified nominator pool.

**Parameters**

* **`pool`** — string, required. Pool address in any form.

**Returns**

* `active_nominators` — array of objects with fields `address`, `balance`, `pending_balance`
* `address_book` — object
* `max_nominators_count` — integer
* `min_nominator_stake` — string
* `min_validator_stake` — string
* `nominators_count` — integer
* `stake_amount_sent` — string
* `state` — integer
* `validator_address` — string
* `validator_amount` — string
* `validator_reward_share` — integer

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/staking/nominatorPools/pool?pool=-1%3A6DC4C16B8506A4797972CEC29C181E9B49D62670786DB7A71DAD430893ACC965'

// Result
{
  "stake_amount_sent": "3071415178698577",
  "validator_amount": "2034902779864",
  "validator_address": "-1:532A6F5724802A2486E7B099DE15456B0BFA60982DDD9CAB151EEBEE8822A2C6",
  "validator_reward_share": 100,
  "state": 2,
  "nominators_count": 1,
  "max_nominators_count": 1,
  "min_validator_stake": "1000000000000",
  "min_nominator_stake": "300000000000000",
  "active_nominators": [
    {
      "address": "0:8FD2EE11B74B35EBCE381D401592B5275B016434135CF3FDA1DED417EA13F470",
      "balance": "3069348375209996",
      "pending_balance": "0"
    }
  ],
  "address_book": {
    "-1:532A6F5724802A2486E7B099DE15456B0BFA60982DDD9CAB151EEBEE8822A2C6": {
      "user_friendly": "Uf9TKm9XJIAqJIbnsJneFUVrC_pgmC3dnKsVHuvuiCKixiXU",
      "domain": null,
      "interfaces": [
        "wallet_v1r3"
      ]
    },
    "-1:6DC4C16B8506A4797972CEC29C181E9B49D62670786DB7A71DAD430893ACC965": {
      "user_friendly": "Ef9txMFrhQakeXlyzsKcGB6bSdYmcHhtt6cdrUMIk6zJZUUs",
      "domain": null,
      "interfaces": [
        "daolama_vault"
      ]
    },
    "0:8FD2EE11B74B35EBCE381D401592B5275B016434135CF3FDA1DED417EA13F470": {
      "user_friendly": "UQCP0u4Rt0s16844HUAVkrUnWwFkNBNc8_2h3tQX6hP0cCXU",
      "domain": null,
      "interfaces": [
        "wallet_v4r2"
      ]
    }
  }
}
```
{% endcode %}
