---
description: >-
  Retrieve attestation reward info for validators specified by array of public
  keys or validator index. If no array is provided, return reward info for every
  validator.
---

# /eth/v1/beacon/rewards/attestations/{epoch}

#### Parameters:

**epoch-string**, The epoch to get rewards info from

**Request body:**

An array of either hex encoded public key (any bytes48 with 0x prefix) or validator index

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/rewards/attestations/280000

'
[
  "722032"
]
'

// Result

```
{% endcode %}
