# blocks

Return blocks that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND. `start_utime` / `end_utime` are Unix seconds (UTC); `*_lt` values are logical times and should be passed as strings.
{% endhint %}

**Parameters**

* **`workchain`** — integer, optional. Workchain of the block.
* **`shard`** — string, optional. Shard ID of the block. Provide this parameter with `workchain`. Example: `8000000000000000`.
* **`seqno`** — integer, optional. Sequence number of the block. Provide this parameter with `workchain` and `shard`.
* **`root_hash`** — string, optional. Root hash of the block.
* **`file_hash`** — string, optional. File hash of the block.
* **`mc_seqno`** — integer, optional. Masterchain block sequence number.
* **`start_utime`** — integer, optional. Query blocks with a generation timestamp at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query blocks with a generation timestamp at or before the specified timestamp.
* **`start_lt`** — integer, optional. Query blocks where `lt` is at or above the specified value.
* **`end_lt`** — integer, optional. Query blocks where `lt` is at or below the specified value.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional, default `desc`. Sort blocks by generation timestamp.

**Returns**

* `blocks` — array of objects with fields `after_merge`, `after_split`, `before_split`, `created_by`, `end_lt`, `file_hash`, `flags`, `gen_catchain_seqno`, `gen_utime`, `global_id`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/blocks?limit=2'

// Result
{
  "blocks": [
    {
      "workchain": -1,
      "shard": "8000000000000000",
      "seqno": 100356914,
      "root_hash": "8laRWSP/dCwLyrROiFa0P3Muq0S4A2Io8vX5j7BCU/0=",
      "file_hash": "57s5XuccVwGJ/mQVpF6aOZuv1jmmaiqM4/ZM3T8tuSE=",
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
      "gen_utime": "1792550067",
      "start_lt": "111332894000000",
      "end_lt": "111332894000004",
      "validator_list_hash_short": -1706221931,
      "gen_catchain_seqno": 873733,
      "min_ref_mc_seqno": 100356911,
      "prev_key_block_seqno": 100223813,
      "vert_seqno": 1,
      "master_ref_seqno": 0,
      "rand_seed": "yrdT4C2mY27iSzz8cndVe5M4bTtiiLlCWr42Pb4C6e8=",
      "created_by": "SpChueUpPrNwazgTvFW2J+HvHhRLR7QZit498c+YYyw=",
      "tx_count": 3,
      "masterchain_block_ref": {
        "workchain": -1,
        "shard": "8000000000000000",
        "seqno": 100356914
      },
      "prev_blocks": [
        {
          "workchain": -1,
          "shard": "8000000000000000",
          "seqno": 100356913
        }
      ]
    }
  ]
}
```
{% endcode %}
