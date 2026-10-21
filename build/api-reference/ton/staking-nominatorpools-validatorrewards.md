# staking nominatorpools validatorrewards

Return validator rewards from the specified nominator pool.

**Parameters**

* **`validator`** — string, required. Validator address in any form.
* **`pool`** — string, required. Pool address in any form.
* **`start_utime`** — integer, optional. Query rewards with a timestamp at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query rewards with a timestamp at or before the specified timestamp.
* **`limit`** — integer, optional, default `100`. Limit the number of rows to return.

**Returns**

* `address_book` — object
* `end_utime` — integer
* `rewards` — array of objects with fields `balance_before`, `cycle_start`, `query_id`, `reward`, `tx_hash`, `tx_lt`, `utime`
* `start_utime` — integer
* `total_on_page` — string

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/staking/nominatorPools/validatorRewards?validator=-1%3A532A6F5724802A2486E7B099DE15456B0BFA60982DDD9CAB151EEBEE8822A2C6&pool=-1%3A6DC4C16B8506A4797972CEC29C181E9B49D62670786DB7A71DAD430893ACC965&limit=2'

// Result
{
  "total_on_page": "39871877392",
  "rewards": [
    {
      "utime": 1792528780,
      "reward": "19976020920",
      "balance_before": "2014926758944",
      "tx_hash": "bI9vOnWN033b3pdQc5OgcXjKI+gwpxvmoDI/vYHwglc=",
      "tx_lt": "111279647000007",
      "cycle_start": 1792429832,
      "query_id": "1792528780"
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
