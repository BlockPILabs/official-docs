# /eth/v1/validator/sync\_committee\_contribution

Requests that the beacon node produce a sync committee contribution.

A 503 error must be returned if the block identified by the response `beacon_block_root` is optimistic (i.e. the sync committee contribution refers to a block that has not been fully verified by an execution engine).

#### Parameters:

**slot-string**, The slot for which the block should be proposed.

**committee\_index-strin**g, The validator's randao reveal value.

**beacon\_block\_root-strin**g, the block root for which to produce the contribution.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/sync_committee_contribution?slot=1&subcommittee_index=1&beacon_block_root=0xcf8e0d4e9587369b2301d0790347320302cc0943d5a1884560367e8208d920f2

// Result

```
{% endcode %}
