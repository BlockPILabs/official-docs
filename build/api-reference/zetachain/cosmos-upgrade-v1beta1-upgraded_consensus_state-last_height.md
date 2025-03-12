---
description: >-
  UpgradedConsensusState queries the consensus state that will serve as a
  trusted kernel for the next version of this chain. It will only be stored at
  the last height of this chain.
---

# /cosmos/upgrade/v1beta1/upgraded\_consensus\_state/{last\_height}

#### **Parameters:**

**last\_height - string**, last height of the current chain must be sent in request as this is the height under which next consensus state is stored

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/upgrade/v1beta1/upgraded_consensus_state/14064517

// Result
{
    "upgraded_consensus_state": null
}
```
{% endcode %}
