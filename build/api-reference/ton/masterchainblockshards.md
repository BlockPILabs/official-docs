# masterchainblockshards

Return all workchain blocks that appeared after the previous masterchain block.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`seqno`** — integer, required. Masterchain block sequence number.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.

**Returns**

* `address_book` — object
* `transactions` — array of objects with fields `account`, `account_state_after`, `account_state_before`, `block_ref`, `description`, `emulated`, `end_status`, `finality`, `hash`, `in_msg`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/masterchainBlockShards?seqno=100356802&limit=2'

// Result
{
  "blocks": [
    {
      "workchain": -1,
      "shard": "8000000000000000",
      "seqno": 100356802,
      "root_hash": "G868vp3GkD4v951ei6LTyp+VkVOPqeakRgJeC5EfdDU=",
      "file_hash": "ZPTvLjGjVs16Ts+tumdtJXDoibwf5zTFp9iBxcULVQU=",
      "global_id": -239,
      "version": 0,
      "after_merge": false,
      "before_split": false,
      "after_split": false,
      "want_merge": true,
      "want_split": false,
      "key_block": false,
      "vert_seqno_incr": false,
      "flags": 1,
      "gen_utime": "1792550022",
      "start_lt": "111332781000000",
      "end_lt": "111332781000004",
      "validator_list_hash_short": -1706221931,
      "gen_catchain_seqno": 873733,
      "min_ref_mc_seqno": 100356800,
      "prev_key_block_seqno": 100223813,
      "vert_seqno": 1,
      "master_ref_seqno": 0,
      "rand_seed": "v7uEVvhqmVvouspcNj1sgU+7X5OJ9kvIEHUHyMjG/kw=",
      "created_by": "E+9Aa3I0LxaIT4hxAYRuMjKWAJHPs21s0atIWww4Bkg=",
      "tx_count": 3,
      "masterchain_block_ref": {
        "workchain": -1,
        "shard": "8000000000000000",
        "seqno": 100356802
      },
      "prev_blocks": [
        {
          "workchain": -1,
          "shard": "8000000000000000",
          "seqno": 100356801
        }
      ]
    }
  ]
}
```
{% endcode %}
