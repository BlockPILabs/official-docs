---
description: Checks the transaction without executing it.
---

# /check\_tx

#### **Parameters:**

**tx - string**, The transaction

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/check_tx?tx=0x46D04F0B4ED3303B86554799E11659D16E144E6976385D65050FBAB56B862891

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "code": 2,
        "data": null,
        "log": "expected 2 wire type, got 6: tx parse error",
        "info": "",
        "gas_wanted": "0",
        "gas_used": "1136790",
        "events": [],
        "codespace": "sdk",
        "sender": "",
        "priority": "0",
        "mempoolError": ""
    }
}           
```
{% endcode %}
