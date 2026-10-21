# traces

Query traces that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND. `start_utime` / `end_utime` are Unix seconds (UTC); `*_lt` values are logical times and should be passed as strings.
{% endhint %}

**Parameters**

* **`account`** — string, optional. List of account addresses to query. Provide addresses in hex, base64, or base64url form.
* **`trace_id`** — array of strings, optional. Find traces by trace ID.
* **`tx_hash`** — array of strings, optional. Find traces by transaction hash.
* **`msg_hash`** — array of strings, optional. Find traces by message hash.
* **`mc_seqno`** — integer, optional. Query traces completed in the masterchain block with the specified sequence number.
* **`start_utime`** — integer, optional. Query traces finished at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query traces finished at or before the specified timestamp.
* **`start_lt`** — integer, optional. Query traces where `end_lt` is at or above the specified value.
* **`end_lt`** — integer, optional. Query traces where `end_lt` is at or below the specified value.
* **`include_actions`** — boolean, optional, default `False`. Include trace actions.
* **`supported_action_types`** — array of strings, optional. List supported action types.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional, default `desc`. Sort traces by `lt`.

**Returns**

* `address_book` — object
* `metadata` — object
* `traces` — array of objects with fields `actions`, `end_lt`, `end_utime`, `external_hash`, `is_incomplete`, `mc_seqno_end`, `mc_seqno_start`, `start_lt`, `start_utime`, `trace`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/traces?limit=2&sort=desc'

// Result
{
  "address_book": {
    "-1:0000000000000000000000000000000000000000000000000000000000000000": {
      "user_friendly": "Ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAU",
      "domain": null,
      "interfaces": []
    },
    "-1:3333333333333333333333333333333333333333333333333333333333333333": {
      "user_friendly": "Ef8zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzM0vF",
      "domain": null,
      "interfaces": null
    },
    "-1:5555555555555555555555555555555555555555555555555555555555555555": {
      "user_friendly": "Ef9VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVbxn",
      "domain": null,
      "interfaces": [
        "wallet_v1r2"
      ]
    }
  },
  "metadata": {}
}
```
{% endcode %}
