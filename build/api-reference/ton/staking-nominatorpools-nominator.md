# staking nominatorpools nominator

Return the nominator's positions in all nominator pools.

**Parameters**

* **`nominator`** — string, required. Nominator address in any form.

**Returns**

* `address_book` — object
* `nominator_pools` — array of objects with fields `balance`, `pending_balance`, `pool_address`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/staking/nominatorPools/nominator?nominator=0%3A8FD2EE11B74B35EBCE381D401592B5275B016434135CF3FDA1DED417EA13F470'

// Result
{
  "nominator_pools": [
    {
      "pool_address": "-1:6DC4C16B8506A4797972CEC29C181E9B49D62670786DB7A71DAD430893ACC965",
      "balance": "3069348375209996",
      "pending_balance": "0"
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
