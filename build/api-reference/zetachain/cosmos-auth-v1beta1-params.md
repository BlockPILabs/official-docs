---
description: Params queries all parameters.
---

# /cosmos/auth/v1beta1/params

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/auth/v1beta1/params

// Result
{
  "params": {
    "max_memo_characters": "256",
    "tx_sig_limit": "7",
    "tx_size_cost_per_byte": "10",
    "sig_verify_cost_ed25519": "590",
    "sig_verify_cost_secp256k1": "1000"
  }
}
```
{% endcode %}
