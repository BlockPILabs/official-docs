# /getBlockHeader

Get metadata of a given block.



**Parameters:**

**workchain - integer,** Workchain id to look up block in

**shard - integer,** Shard id to look up block in

**seqno - integer,** Masterchain seqno to fetch shards of.

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getBlockHeader?workchain=-1&shard=8000000000000000&seqno=39984096&count=40' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "@type": "blocks.header",
    "id": {
      "@type": "ton.blockIdExt",
      "workchain": -1,
      "shard": "-9223372036854775808",
      "seqno": 39984096,
      "root_hash": "b26/Pw8BYz6VY7RyYB/w2Nf8pKBebsg+H4rT1pH5ZEM=",
      "file_hash": "lLylrj7eZn0TSNxpg4yovJJ4x/ILgeeJ3byS6MFVTJw="
    },
    "global_id": -239,
    "version": 0,
    "flags": 1,
    "after_merge": false,
    "after_split": false,
    "before_split": false,
    "want_merge": true,
    "want_split": false,
    "validator_list_hash_short": -2039098909,
    "catchain_seqno": 600633,
    "min_ref_mc_seqno": 39984087,
    "is_key_block": false,
    "prev_key_block_seqno": 39983536,
    "start_lt": "48756940000000",
    "end_lt": "48756940000004",
    "gen_utime": 1724744427,
    "vert_seqno": 1,
    "prev_blocks": [
      {
        "@type": "ton.blockIdExt",
        "workchain": -1,
        "shard": "-9223372036854775808",
        "seqno": 39984095,
        "root_hash": "JfhMFGykjcugr9PP+brOsJ9YMVipPqNU/lh3t/Pmado=",
        "file_hash": "OEDW1/cSI+ItOTk4zctEkAPwmwvhZQZG2sKkkiJLTGQ="
      }
    ],
    "@extra": "1724745625.9983342:11:0.4466366330488255"
  }
}
```
{% endcode %}
