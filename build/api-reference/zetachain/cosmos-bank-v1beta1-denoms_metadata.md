---
description: >-
  DenomsMetadata queries the client metadata for all registered coin
  denominations.
---

# /cosmos/bank/v1beta1/denoms\_metadata

#### **Parameters:**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/denoms_metadata

// Result
{
  "metadatas": [],
  "pagination": {
    "next_key": null,
    "total": "0"
  }
}
```
{% endcode %}
