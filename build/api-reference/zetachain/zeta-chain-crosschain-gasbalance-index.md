---
description: Queries a list of gasBalance items.
---

# /zeta-chain/crosschain/gasBalance/{index}

#### **Parameters:**

**index - string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/gasBalance/{index}

// Result
{
  "GasBalance": {
    "creator": "string",
    "index": "string",
    "chain": "string",
    "signers": [
      "string"
    ],
    "blockNums": [
      "string"
    ],
    "balances": [
      "string"
    ],
    "medianIndex": "string"
  }
}
```
{% endcode %}
