# /eth/v1/beacon/blocks

Instructs the beacon node to broadcast a newly signed beacon block to the beacon network, to be included in the beacon chain. A success response (20x) indicates that the block passed gossip validation and was successfully broadcast onto the network. The beacon node is also expected to integrate the block into state, but may broadcast it before doing so, so as to aid timely delivery of the block. Should the block fail full validation, a separate success response code (202) is used to indicate that the block was successfully broadcast but failed integration. After Deneb, this additionally instructs the beacon node to broadcast all given blobs.

#### P**arameters:**

**None**

**Request body**

The `SignedBlindedBeaconBlock` object composed of `BlindedBeaconBlock` object (produced by beacon node) and validator signature.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/blocks
'{
<Request body>
}'

// Result

```
{% endcode %}
