---
description: >-
  can be queried for the number of transactions currently pending for inclusion
  in the next block(s), as well as the ones that are being scheduled for future
  execution only.
---

# txpool\_status

#### **Parameters**

**None**

#### **Return Value**

| Type | Description                         |
| ---- | ----------------------------------- |
| int  | The number of pending transactions. |
| int  | The number of queued transactions.  |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"txpool_status","id":1}' https://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "pending": "0x7",
        "queued": "0x0"
    }
}
```
{% endcode %}
