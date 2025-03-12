---
description: Get data about unconfirmed transactions
---

# /num\_unconfirmed\_txs

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/num_unconfirmed_txs

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "n_txs": "6",
        "total": "6",
        "total_bytes": "1766",
        "txs": null
    }
}
```
{% endcode %}
