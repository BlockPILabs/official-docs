---
description: AllEvidence queries all evidence.
---

# /cosmos/evidence/v1beta1/evidence

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/evidence/v1beta1/evidence

// Result
{
    "evidence": [
        {
            "@type": "/cosmos.evidence.v1beta1.Equivocation",
            "height": "12842605",
            "time": "2022-11-14T12:26:53.319800141Z",
            "power": "225822",
            "consensus_address": "cosmosvalcons18eg64zpqxmt6wru5705xg94hvqdh3hvv94e3cm"
        }
    ],
    "pagination": {
        "next_key": null,
        "total": "1"
    }
}
```
{% endcode %}
