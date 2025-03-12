# /eth/v2/beacon/blinded\_blocks

Instructs the beacon node to use the components of the `SignedBlindedBeaconBlock` to construct and publish a `SignedBeaconBlock` by swapping out the `transactions_root` for the corresponding full list of `transactions`. The beacon node should broadcast a newly constructed `SignedBeaconBlock` to the beacon network, to be included in the beacon chain. The beacon node is not required to validate the signed `BeaconBlock`, and a successful response (20X) only indicates that the broadcast has been successful. The beacon node is expected to integrate the new block into its state, and therefore validate the block internally, however blocks which fail the validation are still broadcast but a different status code is returned (202). Before Bellatrix, this endpoint will accept a `SignedBeaconBlock`. The broadcast behaviour may be adjusted via the `broadcast_validation` query parameter.

#### P**arameters:**

**None**

**Request body**

The `SignedBlindedBeaconBlock` object composed of `BlindedBeaconBlock` object (produced by beacon node) and validator signature.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v2/beacon/blinded_blocks
'{
<Request body>
}'

// Result

```
{% endcode %}
