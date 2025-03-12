---
description: Proposal queries proposal details based on ProposalID.
---

# /cosmos/gov/v1/proposals/{proposal\_id}

#### **Parameters:**

**proposal\_id - string**, proposal\_id defines the unique id of the proposal.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1/proposals/1

// Result
{
  "proposal": {
    "proposal_id": "1",
    "content": {
      "@type": "/cosmos.upgrade.v1beta1.SoftwareUpgradeProposal",
      "title": "v2.0.0",
      "description": "Zeta Release v2.0.0",
      "plan": {
        "name": "v2.0.0",
        "time": "0001-01-01T00:00:00Z",
        "height": "392589",
        "info": "{\"binaries\": {\"zetacored-linux/amd64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetacored-ubuntu-22-amd64?checksum=sha256:fecaece4530c7358a3f331bb3461c7903614189250964b34bdb60eba113d8a77\",\"zetacored-linux/arm64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetacored-ubuntu-22-arm64?checksum=sha256:324988e195e4d0b5233bed43568fbf9ef7ccc1bdef3a7a73174075be366a8b3a\",\"zetaclientd-linux/amd64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetaclientd-ubuntu-22-arm64?checksum=sha256:94c8cc0171da3b6300ae7a43337496742e29628c249e84a6ef4041e7e4b520f2\",\"zetaclientd-linux/arm64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetaclientd-ubuntu-22-amd64?checksum=sha256:f36f070e7636ce36e66f230996491fab370d4f4084b5bcadc22cbd5cd547b701\"}}",
        "upgraded_client_state": null
      }
    },
    "status": "PROPOSAL_STATUS_FAILED",
    "final_tally_result": {
      "yes": "11890200000000000000000",
      "abstain": "0",
      "no": "0",
      "no_with_veto": "0"
    },
    "submit_time": "2023-06-19T16:45:07.743798724Z",
    "deposit_end_time": "2023-06-21T16:45:07.743798724Z",
    "total_deposit": [
      {
        "denom": "azeta",
        "amount": "10000000"
      }
    ],
    "voting_start_time": "2023-06-19T16:45:07.743798724Z",
    "voting_end_time": "2023-06-19T18:45:07.743798724Z"
  }
}
```
{% endcode %}
