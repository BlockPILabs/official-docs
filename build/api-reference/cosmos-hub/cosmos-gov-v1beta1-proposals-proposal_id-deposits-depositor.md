---
description: Deposit queries single deposit information based proposalID, depositAddr.
---

# /cosmos/gov/v1beta1/proposals/{proposal\_id}/deposits/{depositor}

#### **Parameters:**

**proposal\_id - string**, proposal\_id defines the unique id of the proposal.

**depositor - string**, depositor defines the deposit addresses from the proposals.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1beta1/proposals/99/deposits/cosmos1ykhysgmsnju92p7lny34km2uywqwpjcgzuxnut

// Result
{
    "deposit": {
        "proposal_id": "99",
        "depositor": "cosmos1ykhysgmsnju92p7lny34km2uywqwpjcgzuxnut",
        "amount": [
            {
                "denom": "uatom",
                "amount": "50000000"
            }
        ]
    }
}
```
{% endcode %}
