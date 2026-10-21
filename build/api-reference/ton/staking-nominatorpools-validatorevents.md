# staking nominatorpools validatorevents

Return validator accounting events from nominator pools, optionally filtered by validator, pool, event type, and time range.

**Parameters**

* **`validator`** — string, optional. Validator address in any form.
* **`pool`** — string, optional. Pool address in any form.
* **`type`** — string, optional. Filter by event type: `reward`, `penalty`, `deposit`, or `withdrawal`.
* **`start_utime`** — integer, optional. Query events with a timestamp at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query events with a timestamp at or before the specified timestamp.
* **`limit`** — integer, optional, default `100`. Limit the number of rows to return.

**Returns**

* `address_book` — object
* `end_utime` — integer
* `events` — array of objects with fields `amount`, `balance_after`, `balance_before`, `balance_delta`, `cycle_start`, `pool_address`, `query_id`, `tx_hash`, `tx_lt`, `type`
* `start_utime` — integer

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/staking/nominatorPools/validatorEvents?pool=-1%3A6DC4C16B8506A4797972CEC29C181E9B49D62670786DB7A71DAD430893ACC965&limit=2'

// Result
{
  "events": [
    {
      "tx_hash": "bI9vOnWN033b3pdQc5OgcXjKI+gwpxvmoDI/vYHwglc=",
      "tx_lt": "111279647000007",
      "utime": 1792528780,
      "pool_address": "-1:6DC4C16B8506A4797972CEC29C181E9B49D62670786DB7A71DAD430893ACC965",
      "validator_address": "-1:532A6F5724802A2486E7B099DE15456B0BFA60982DDD9CAB151EEBEE8822A2C6",
      "type": "reward",
      "amount": "19976020920",
      "balance_delta": "19976020920",
      "balance_before": "2014926758944",
      "balance_after": "2034902779864",
      "query_id": "1792528780",
      "cycle_start": 1792429832,
      "validator_reward_share": 100
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
    }
  }
}
```
{% endcode %}
