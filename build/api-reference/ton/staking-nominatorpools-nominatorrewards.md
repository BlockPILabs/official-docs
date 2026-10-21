# staking nominatorpools nominatorrewards

Return rewards for the specified nominator in the specified nominator pool.

**Parameters**

* **`nominator`** — string, required. Nominator address in any form.
* **`pool`** — string, required. Pool address in any form.
* **`start_utime`** — integer, optional. Query rewards with a timestamp at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query rewards with a timestamp at or before the specified timestamp.
* **`limit`** — integer, optional, default `100`. Limit the number of rows to return.

**Returns**

* `address_book` — object
* `end_utime` — integer
* `rewards` — array of objects with fields `reward`, `stake_before`, `tx_hash`, `tx_lt`, `utime`
* `start_utime` — integer
* `total_on_page` — string

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/staking/nominatorPools/nominatorRewards?nominator=0%3A8FD2EE11B74B35EBCE381D401592B5275B016434135CF3FDA1DED417EA13F470&pool=-1%3A6DC4C16B8506A4797972CEC29C181E9B49D62670786DB7A71DAD430893ACC965&limit=2'

// Result
{
  "total_on_page": "3947315861912",
  "rewards": [
    {
      "utime": 1792528780,
      "reward": "1977626071138",
      "stake_before": "3067370749138858",
      "tx_hash": "bI9vOnWN033b3pdQc5OgcXjKI+gwpxvmoDI/vYHwglc=",
      "tx_lt": "111279647000007"
    }
  ],
  "address_book": {
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
