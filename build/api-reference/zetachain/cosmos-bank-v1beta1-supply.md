---
description: TotalSupply queries the total supply of all coins.
---

# /cosmos/bank/v1beta1/supply

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/supply

// Result
{
  "supply": [
    {
      "denom": "azeta",
      "amount": "702527705286411307728318696264917662"
    }
  ],
  "pagination": {
    "next_key": null,
    "total": "1"
  }
}
```
{% endcode %}
