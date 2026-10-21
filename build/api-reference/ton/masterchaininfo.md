# masterchaininfo

Return the first and last indexed blocks.

**Parameters**

None.

**Returns**

* `first` — object with fields `after_merge`, `after_split`, `before_split`, `created_by`, `end_lt`, `file_hash`, `flags`, `gen_catchain_seqno`, `gen_utime`, `global_id`
* `last` — object with fields `after_merge`, `after_split`, `before_split`, `created_by`, `end_lt`, `file_hash`, `flags`, `gen_catchain_seqno`, `gen_utime`, `global_id`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/masterchainInfo'

// Result
{
  "last": {
    "workchain": -1,
    "shard": "8000000000000000",
    "seqno": 100356923,
    "root_hash": "esgEOOIysloxBKNMrVLgA1HGCJq90KF/pUvnzi8RpIE=",
    "file_hash": "L5F/Y3y/+lgsQGKbqv/b8+UWQXP7q8f6RqkY0Qf+UnA=",
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
    "gen_utime": "1792550071",
    "start_lt": "111332904000000",
    "end_lt": "111332904000004",
    "validator_list_hash_short": -1706221931,
    "gen_catchain_seqno": 873733,
    "min_ref_mc_seqno": 100356920,
    "prev_key_block_seqno": 100223813,
    "vert_seqno": 1,
    "master_ref_seqno": 0,
    "rand_seed": "0VK5gdizavrWzuGfbiAC2FagtQuQExkpYB+hU1oltCw=",
    "created_by": "l2d3sjHXM9TPBDa6NPb/iJGLrC9SBVDZ3zaYdpwNZb8=",
    "tx_count": 3,
    "masterchain_block_ref": {
      "workchain": -1,
      "shard": "8000000000000000",
      "seqno": 100356923
    },
    "prev_blocks": [
      {
        "workchain": -1,
        "shard": "8000000000000000",
        "seqno": 100356922
      }
    ]
  },
  "first": {
    "workchain": -1,
    "shard": "8000000000000000",
    "seqno": 1,
    "root_hash": "8GYhhrigd8CwZGrRT59iulLDcgiTYuvOAzFJxugc0Ts=",
    "file_hash": "V+XzykEwun4yePZhAEPZk77RbMfMOgS/S4GiJkSKY6s=",
    "global_id": -239,
    "version": 0,
    "after_merge": false,
    "before_split": false,
    "after_split": false,
    "want_merge": false,
    "want_split": false,
    "key_block": false,
    "vert_seqno_incr": false,
    "flags": 0,
    "gen_utime": "1573822385",
    "start_lt": "1000000",
    "end_lt": "1000012",
    "validator_list_hash_short": -1447544682,
    "gen_catchain_seqno": 0,
    "min_ref_mc_seqno": 1,
    "prev_key_block_seqno": 0,
    "vert_seqno": 0,
    "master_ref_seqno": 0,
    "rand_seed": "e1ZHQiC/ZPGzzR9IHm3u7FZ2ZwzzdUXMYRJf7DCQdQg=",
    "created_by": "6MC3PyuC80JUx8L+cNE4TnXEZ1i3TeCKxYFV5ZP9eKw=",
    "tx_count": 9,
    "masterchain_block_ref": {
      "workchain": -1,
      "shard": "8000000000000000",
      "seqno": 1
    },
    "prev_blocks": [
      {
        "workchain": -1,
        "shard": "8000000000000000",
        "seqno": 0
      }
    ]
  }
}
```
{% endcode %}
