# /eth/v1/validator/liveness/{epoch}

Requests the beacon node to indicate if a validator has been observed to be live in a given epoch. The beacon node might detect liveness by observing messages from the validator on the network, in the beacon chain, from its API or from any other source. A beacon node SHOULD support the current and previous epoch, however it MAY support earlier epoch. It is important to note that the values returned by the beacon node are not canonical; they are best-effort and based upon a subjective view of the network. A beacon node that was recently started or suffered a network partition may indicate that a validator is not live when it actually is.

#### Parameters:

**None**

**Request body:**

An array of the validator indices for which to detect liveness.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/liveness/280000

'
[
  "1"
]
'

// Result

```
{% endcode %}
