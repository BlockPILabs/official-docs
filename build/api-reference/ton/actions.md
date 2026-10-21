# actions

Query actions that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND. `start_utime` / `end_utime` are Unix seconds (UTC); `*_lt` values are logical times and should be passed as strings.
{% endhint %}

**Parameters**

* **`account`** — string, optional. List of account addresses to query. Provide addresses in hex, base64, or base64url form.
* **`tx_hash`** — array of strings, optional. Find actions by transaction hash.
* **`msg_hash`** — array of strings, optional. Find actions by message hash.
* **`action_id`** — array of strings, optional. Find actions by `action_id`.
* **`trace_id`** — array of strings, optional. Find actions by `trace_id`.
* **`mc_seqno`** — integer, optional. Query actions for traces completed in the masterchain block with the specified sequence number.
* **`start_utime`** — integer, optional. Query actions for traces with `trace_end_utime u003e= start_utime`.
* **`end_utime`** — integer, optional. Query actions for traces with `trace_end_utime u003c= end_utime`.
* **`start_lt`** — integer, optional. Query actions for traces with `trace_end_lt u003e= start_lt`.
* **`end_lt`** — integer, optional. Query actions for traces with `trace_end_lt u003c= end_lt`.
* **`action_type`** — array of strings, optional. Filter actions by type.
* **`exclude_action_type`** — array of strings, optional. Exclude the specified action types.
* **`supported_action_types`** — array of strings, optional. List supported action types.
* **`include_accounts`** — boolean, optional, default `False`. Include the `accounts` array for each action in the response.
* **`include_transactions`** — boolean, optional, default `False`. Include the `transactions_full` array with detailed transaction data for each action in the response.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional, default `desc`. Sort actions by `lt`.

**Returns**

* `actions` — array of objects with fields `accounts`, `action_id`, `details`, `end_lt`, `end_utime`, `finality`, `start_lt`, `start_utime`, `success`, `trace_end_lt`
* `address_book` — object
* `metadata` — object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/actions?limit=2&sort=desc'

// Result
{
  "actions": [
    {
      "trace_id": "ErD49hgaiCCdamXBImMHdrlpCigbe5ONIlku2RMEK9E=",
      "action_id": "1u/1YtWcyysDlNV23gXen9IkrgLewkSMamE2N6XYy38=",
      "start_lt": "111332874000000",
      "end_lt": "111332874000002",
      "start_utime": 1792550059,
      "end_utime": 1792550059,
      "trace_end_lt": "111332874000002",
      "trace_end_utime": 1792550059,
      "trace_mc_seqno_end": 100356894,
      "transactions": [
        "ErD49hgaiCCdamXBImMHdrlpCigbe5ONIlku2RMEK9E="
      ],
      "success": true,
      "type": "ton_transfer",
      "details": {
        "source": "-1:0000000000000000000000000000000000000000000000000000000000000000",
        "destination": "-1:3333333333333333333333333333333333333333333333333333333333333333",
        "value": "2700000000",
        "value_extra_currencies": {},
        "comment": null,
        "encrypted": false
      },
      "trace_external_hash": "ziUEPFLhq+qWc9Va5f51sxFu/Rdr5xoqW7QeFzzdqNg=",
      "finality": "finalized"
    }
  ],
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
    }
  },
  "metadata": {},
  "next_cursor": "lsLD0wAAZUG0WNRCxCDrpdzSF9OVrhHFB_jzxQB82DcumlTkklqw6qZBK5BDM9MAAGVBtFjUQsQgMuNiG0GS5GpcuhkZB7TddtM0TXUurOtoCKufF1q6rqw"
}
```
{% endcode %}
