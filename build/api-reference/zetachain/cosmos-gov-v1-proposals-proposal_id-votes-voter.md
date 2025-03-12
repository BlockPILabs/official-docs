---
description: Vote queries voted information based on proposalID, voterAddr.
---

# /cosmos/gov/v1/proposals/{proposal\_id}/votes/{voter}

#### **Parameters:**

**proposal\_id - string**, proposal\_id defines the unique id of the proposal.

**voter - string**, voter defines the oter address for the proposals.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1/proposals/98/votes/{voter}

// Result
{   } 
```
{% endcode %}
