---
description: >-
  DenomsMetadata queries the client metadata for all registered coin
  denominations.
---

# /cosmos/bank/v1beta1/denoms\_metadata

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/denoms_metadata

// Result
{
    "metadatas": [
        {
            "description": "The native staking token of the Cosmos Hub.",
            "denom_units": [
                {
                    "denom": "uatom",
                    "exponent": 0,
                    "aliases": [
                        "microatom"
                    ]
                },
                {
                    "denom": "matom",
                    "exponent": 3,
                    "aliases": [
                        "milliatom"
                    ]
                },
                {
                    "denom": "atom",
                    "exponent": 6,
                    "aliases": []
                }
            ],
            "base": "uatom",
            "display": "atom",
            "name": "",
            "symbol": ""
        }
    ],
    "pagination": {
        "next_key": null,
        "total": "1"
    }
}
```
{% endcode %}
