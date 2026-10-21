# validators elections

Return validator elections, optionally including matching participants.

**Parameters**

* **`election_id`** — integer, optional. Election ID.
* **`stake_holder_address`** — string, optional. Stakeholder address in any form.
* **`adnl_address`** — string, optional. ADNL address in hex, base64, or base64url form.
* **`validator_pubkey`** — string, optional. Validator public key in hex, base64, or base64url form.
* **`return_participants`** — boolean, optional, default `False`. Return election participants. If `stake_holder_address`, `adnl_address`, or `validator_pubkey` is specified, return only matching participants.
* **`finished`** — boolean, optional. Filter by the `finished` flag.
* **`start_utime`** — integer, optional. Query elections with `election_id` at or after the specified value. This parameter filters `election_id`, not `elect_close`.
* **`end_utime`** — integer, optional. Query elections with `election_id` at or before the specified value. This parameter filters `election_id`, not `elect_close`.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. At most 100 when `return_participants` is `true`.

**Returns**

* `address_book` — object
* `elections` — array of objects with fields `election_id`, `elect_close`, `failed`, `finished`, `min_stake`, `participants`, `total_participants`, `total_stake`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/validators/elections?limit=2'

// Result
{
  "elections": [
    {
      "election_id": 1792560904,
      "elect_close": 1792552712,
      "min_stake": "300000000000000",
      "total_stake": "655441248086399229",
      "total_participants": 376,
      "failed": false,
      "finished": false
    }
  ],
  "address_book": {}
}
```
{% endcode %}
