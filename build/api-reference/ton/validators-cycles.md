# validators cycles

`min_stake` and `max_stake` are the true stake bounds for selected validators. `min_stake_limit` and `max_stake_limit` are the config17 election limits. When the response includes validators, `max_factor` is the participant's raw declared factor (65536 = 1.0). The effective factor used to derive `stake` is the smaller of `max_factor` and `max_stake_factor`.

**Parameters**

* **`cycle_start`** — integer, optional. Validator cycle start time.
* **`election_id`** — integer, optional. Elector election ID that produced the cycle.
* **`stake_holder_address`** — string, optional. Stakeholder address in any form.
* **`adnl_address`** — string, optional. ADNL address in hex, base64, or base64url form.
* **`validator_pubkey`** — string, optional. Validator public key in hex, base64, or base64url form.
* **`return_validators`** — boolean, optional, default `False`. Return validators in the set. If `stake_holder_address`, `adnl_address`, or `validator_pubkey` is specified, return only matching validators.
* **`start_utime`** — integer, optional. Query cycles with `cycle_start` at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query cycles with `cycle_start` at or before the specified timestamp.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. At most 100 when `return_validators` is `true`.

**Returns**

* `address_book` — object
* `cycles` — array of objects with fields `cycle_end`, `cycle_start`, `election_id`, `elections_end_before`, `elections_start_before`, `main`, `max_main_validators`, `max_stake`, `max_stake_factor`, `max_stake_limit`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/validators/cycles?limit=2'

// Result
{
  "cycles": [
    {
      "election_id": 1792495368,
      "cycle_start": 1792495368,
      "cycle_end": 1792560904,
      "total": 382,
      "main": 100,
      "total_weight": "1152921504606846792",
      "total_stake": "677999312078967055",
      "validators_elected_for": 65536,
      "elections_start_before": 32768,
      "elections_end_before": 8192,
      "stake_held_for": 32768,
      "max_validators": 400,
      "max_main_validators": 100,
      "min_validators": 75,
      "min_stake": "819550198470000",
      "max_stake": "3263315198470000",
      "min_stake_limit": "300000000000000",
      "max_stake_limit": "10000000000000000",
      "min_total_stake": "75000000000000000",
      "max_stake_factor": 294912
    }
  ],
  "address_book": {}
}
```
{% endcode %}
