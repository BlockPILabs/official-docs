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
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/evidence/v1beta1/evidence

// Result
{
  "evidence": [],
  "pagination": {
    "next_key": null,
    "total": "0"
  }
}
```
{% endcode %}
