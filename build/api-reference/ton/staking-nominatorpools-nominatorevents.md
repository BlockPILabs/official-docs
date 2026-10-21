# staking nominatorpools nominatorevents

Return events for the specified nominator pool, optionally filtered by nominator and time range.

**Parameters**

* **`pool`** — string, required. Pool address in any form.
* **`nominator`** — string, optional. Nominator address in any form.
* **`start_utime`** — integer, optional. Query events with a timestamp at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query events with a timestamp at or before the specified timestamp.
* **`limit`** — integer, optional, default `100`. Limit the number of rows to return.

**Returns**

* `address_book` — object
* `end_utime` — integer
* `events` — array of objects with fields `amount`, `balance_after`, `balance_before`, `balance_delta`, `nominator_address`, `pending_balance_after`, `pending_balance_before`, `pending_balance_delta`, `pool_address`, `tx_hash`
* `start_utime` — integer

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/staking/nominatorPools/nominatorEvents?pool=-1%3A6DC4C16B8506A4797972CEC29C181E9B49D62670786DB7A71DAD430893ACC965&limit=2'

// Result
{
  "events": [
    {
      "tx_hash": "bI9vOnWN033b3pdQc5OgcXjKI+gwpxvmoDI/vYHwglc=",
      "tx_lt": "111279647000007",
      "utime": 1792528780,
      "pool_address": "-1:6DC4C16B8506A4797972CEC29C181E9B49D62670786DB7A71DAD430893ACC965",
      "nominator_address": "0:8FD2EE11B74B35EBCE381D401592B5275B016434135CF3FDA1DED417EA13F470",
      "type": "reward",
      "amount": "1977626071138",
      "balance_delta": "1977626071138",
      "pending_balance_delta": "0",
      "balance_before": "3067370749138858",
      "balance_after": "3069348375209996",
      "pending_balance_before": "0",
      "pending_balance_after": "0",
      "withdraw_request_before": false,
      "withdraw_request_after": false
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
