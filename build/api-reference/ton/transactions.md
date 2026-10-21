# transactions

Query transactions that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND. `start_utime` / `end_utime` are Unix seconds (UTC); `*_lt` values are logical times and should be passed as strings.
{% endhint %}

**Parameters**

* **`workchain`** — integer, optional. Workchain of the block.
* **`shard`** — string, optional. Block shard ID. Provide this parameter with `workchain`. Example: `8000000000000000`.
* **`seqno`** — integer, optional. Sequence number of the block. Provide this parameter with `workchain` and `shard`.
* **`mc_seqno`** — integer, optional. Masterchain block sequence number.
* **`account`** — array of strings, optional. List of account addresses for the transactions. Provide addresses in hex, base64, or base64url form.
* **`exclude_account`** — array of strings, optional. Exclude transactions for the specified account addresses.
* **`hash`** — string, optional. Transaction hash.
* **`lt`** — integer, optional. Transaction `lt`.
* **`start_utime`** — integer, optional. Query transactions with a generation timestamp at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query transactions with a generation timestamp at or before the specified timestamp.
* **`start_lt`** — integer, optional. Query transactions where `lt` is at or above the specified value.
* **`end_lt`** — integer, optional. Query transactions where `lt` is at or below the specified value.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional, default `desc`. Sort transactions by `lt`.

**Returns**

* `address_book` — object
* `transactions` — array of objects with fields `account`, `account_state_after`, `account_state_before`, `block_ref`, `description`, `emulated`, `end_status`, `finality`, `hash`, `in_msg`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/transactions?limit=2'

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
  }
}
```
{% endcode %}
