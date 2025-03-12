---
description: Queries a InTxHashToCctx by hash.
---

# /zeta-chain/crosschain/inTxHashToCctx/{inTxHash}

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/inTxHashToCctx/0x002d123594e4b920d322bc820bbb3524aa3b7dd81b1aecd7597157b4045dc334

// Result
{
  "inTxHashToCctx": {
    "in_tx_hash": "0x002d123594e4b920d322bc820bbb3524aa3b7dd81b1aecd7597157b4045dc334",
    "cctx_index": "0x0dfc45904a266ae808fb0b16bc443c86a59f6a351808134e6d78ccf000c749fb"
  }
}
```
{% endcode %}
