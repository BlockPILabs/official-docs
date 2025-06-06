---
description: Proposal queries proposal details based on ProposalID.
---

# /cosmos/gov/v1beta1/proposals/{proposal\_id}

#### **Parameters:**

**proposal\_id - string**, proposal\_id defines the unique id of the proposal.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1beta1/proposals/1

// Result
{
    "proposal": {
        "proposal_id": "1",
        "content": {
            "@type": "/cosmos.gov.v1beta1.TextProposal",
            "title": "Adjustment of blocks_per_year to come aligned with actual block time",
            "description": "This governance proposal is for adjustment of blocks_per_year parameter to normalize the inflation rate and reward rate.\\n ipfs link: https://ipfs.io/ipfs/QmXqEBr56xeUzFpgjsmDKMSit3iqnKaDEL4tabxPXoz9xc"
        },
        "status": "PROPOSAL_STATUS_PASSED",
        "final_tally_result": {
            "yes": "97118903526799",
            "abstain": "402380577234",
            "no": "320545400000",
            "no_with_veto": "0"
        },
        "submit_time": "2019-03-20T06:41:27.040075748Z",
        "deposit_end_time": "2019-04-03T06:41:27.040075748Z",
        "total_deposit": [
            {
                "denom": "uatom",
                "amount": "512100000"
            }
        ],
        "voting_start_time": "2019-03-20T20:43:59.630492307Z",
        "voting_end_time": "2019-04-03T20:43:59.630492307Z"
    }
}
```
{% endcode %}
