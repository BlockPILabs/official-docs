---
description: Returns with the responses from CheckTx and DeliverTx.
---

# /broadcast\_tx\_commit

#### **Parameters:**

**tx - string**, The transaction

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/broadcast_tx_commit?tx=0x46D04F0B4ED3303B86554799E11659D16E144E6976385D65050FBAB56B862891

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "check_tx": {
            "code": 2,
            "data": null,
            "log": "expected 2 wire type, got 6: tx parse error",
            "info": "",
            "gas_wanted": "0",
            "gas_used": "106992",
            "events": [],
            "codespace": "sdk",
            "sender": "",
            "priority": "0",
            "mempoolError": ""
        },
        "deliver_tx": {
            "code": 0,
            "data": null,
            "log": "",
            "info": "",
            "gas_wanted": "0",
            "gas_used": "0",
            "events": [],
            "codespace": ""
        },
        "hash": "9D3E7287EDD6C1B731B2D233E9ABE7630C6D5F9956AF4ADD9DA22EB416672286",
        "height": "0"
    }
}                     
```
{% endcode %}
