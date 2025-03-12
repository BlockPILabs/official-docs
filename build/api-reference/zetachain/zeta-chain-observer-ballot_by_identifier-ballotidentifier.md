---
description: Queries a list of VoterByIdentifier items.
---

# /zeta-chain/observer/ballot\_by\_identifier/{ballotIdentifier}

#### **Parameters:**

**ballotIdentifier - string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/observer/ballot_by_identifier/{ballotIdentifier}

// Result
{
  "ballot": {
    "index": "string",
    "BallotIdentifier": "string",
    "VoterList": [
      "string"
    ],
    "Votes": [
      "SuccessObservation"
    ],
    "ObservationType": "EmptyObserverType",
    "BallotThreshold": "string",
    "BallotStatus": "BallotFinalized_SuccessObservation"
  }
}
```
{% endcode %}
