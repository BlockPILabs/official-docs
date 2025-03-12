---
description: Submits sync committee signature objects to the node.
---

# /eth/v1/beacon/pool/sync\_committees

Sync committee signatures are not present in phase0, but are required for Altair networks.

If a sync committee signature is validated successfully the node MUST publish that sync committee signature on all applicable subnets.

If one or more sync committee signatures fail validation the node MUST return a 400 error with details of which sync committee signatures have failed, and why.

#### Parameters:

None

**Request body:**

The sync committee signature objects

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/pool/sync_committees
‘
<signature object>
’

// Result

```
{% endcode %}
