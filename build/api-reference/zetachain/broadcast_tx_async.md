---
description: >-
  Returns right away, with no response. Does not wait for CheckTx nor DeliverTx
  Response.
---

# /broadcast\_tx\_async

#### **Parameters:**

**tx - string**, The transaction

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/broadcast_tx_async?tx=0x46D04F0B4ED3303B86554799E11659D16E144E6976385D65050FBAB56B862891

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "code": 2,
        "data": "",
        "log": "expected 2 wire type, got 6: tx parse error",
        "codespace": "sdk",
        "hash": "9D3E7287EDD6C1B731B2D233E9ABE7630C6D5F9956AF4ADD9DA22EB416672286"
    }
}                      
```
{% endcode %}
