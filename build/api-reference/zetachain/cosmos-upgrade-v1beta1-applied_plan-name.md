---
description: AppliedPlan queries a previously applied upgrade plan by its name.
---

# /cosmos/upgrade/v1beta1/applied\_plan/{name}

#### **Parameters:**

**name-string**, name is the name of the applied plan to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/upgrade/v1beta1/applied_plan/{name}

// Result
{
  "height": "0"
}
```
{% endcode %}
