---
description: AllBalances queries the balance of all coins for a single account.
---

# /cosmos/bank/v1beta1/balances/{address}

#### **Parameters:**

**address-string,** address is the address to query balances for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/bank/v1beta1/balances/cosmos1hkthq04278pj5cqt7tsle4shs2hhlee4s9vc2m

// Result
{
    "balances": [
        {
            "denom": "ibc/B05539B66B72E2739B986B86391E5D08F12B8D5D2C2A7F8F8CF9ADF674DFA231",
            "amount": "37"
        },
        {
            "denom": "uatom",
            "amount": "783604"
        }
    ],
    "pagination": {
        "next_key": null,
        "total": "2"
    }
}
```
{% endcode %}
