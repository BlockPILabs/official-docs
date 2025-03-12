---
description: Deposit queries single deposit information based proposalID, depositAddr.
---

# /cosmos/gov/v1/proposals/{proposal\_id}/deposits/{depositor}

#### **Parameters:**

**proposal\_id - string**, proposal\_id defines the unique id of the proposal.

**depositor - string**, depositor defines the deposit addresses from the proposals.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1/proposals/99/deposits/{depositor}

// Result
{}
```
{% endcode %}
