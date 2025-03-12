---
description: >-
  Submits Attestation objects to the node. Each attestation in the request body
  is processed individually.
---

# /eth/v1/beacon/pool/attestations

If an attestation is validated successfully the node MUST publish that attestation on the appropriate subnet.

If one or more attestations fail validation the node MUST return a 400 error with details of which attestations have failed, and why.



**Request body:**

The attestations object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/pool/attestations
'
<attestations object>
'

// Result

```
{% endcode %}
