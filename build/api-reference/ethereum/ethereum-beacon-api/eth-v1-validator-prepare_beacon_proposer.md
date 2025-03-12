# /eth/v1/validator/prepare\_beacon\_proposer

Prepares the beacon node for potential proposers by supplying information required when proposing blocks for the given validators. The information supplied for each validator index will persist through the epoch in which the call is submitted and for a further two epochs after that, or until the beacon node restarts. It is expected that validator clients will send this information periodically, for example each epoch, to ensure beacon nodes have correct and timely fee recipient information.

Note that there is no guarantee that the beacon node will use the supplied fee recipient when creating a block proposal, so on receipt of a proposed block the validator should confirm that it finds the fee recipient within the block acceptable before signing it.

Also note that requests containing currently inactive or unknown validator indices will be accepted, as they may become active at a later epoch.

#### Parameters:

**None**

**Request body:**

array\<object>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/prepare_beacon_proposer

'
[
  {
    "validator_index": "1",
    "fee_recipient": "0xAbcF8e0d4e9587369b2301D0790347320302cc09"
  }
]
'

// Result

```
{% endcode %}
