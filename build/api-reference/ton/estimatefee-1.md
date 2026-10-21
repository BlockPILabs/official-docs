# estimatefee

Estimate the fees required to process the query. The `body`, `init_code`, and `init_data` fields accept serialized, base64-encoded values.

**Parameters**

Request body (`application/json`):

* **`address`** — string. Target contract address whose execution is estimated.
* **`body`** — string. Serialized (base64 boc) message body to be executed.
* **`ignore_chksig`** — boolean. Set to `true` to skip signature verification during estimation.
* **`init_code`** — string. Serialized (base64 boc) contract code, if the account is not deployed yet.
* **`init_data`** — string. Serialized (base64 boc) contract data, if the account is not deployed yet.

**Returns**

* `destination_fees` — array of objects with fields `fwd_fee`, `gas_fee`, `in_fwd_fee`, `storage_fee`
* `source_fees` — object with fields `fwd_fee`, `gas_fee`, `in_fwd_fee`, `storage_fee`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/estimateFee' \
  -H 'Content-Type: application/json' \
  --data '{"address": "0:F785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78", "body": "te6ccgEBAQEAAgAAAA==", "ignore_chksig": true}'

// Result
{
  "source_fees": {
    "in_fwd_fee": 66667,
    "storage_fee": 972,
    "gas_fee": 0,
    "fwd_fee": 0
  },
  "destination_fees": []
}
```
{% endcode %}
