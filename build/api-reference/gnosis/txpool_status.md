---
description: >-
  Returns the number of transactions currently pending for inclusion in the next
  block(s), as well as the ones that are being scheduled for future execution
  only.
---

# txpool\_status

#### **Parameters:**

None

#### Returns:

**object** - with following fields:

* **pending** - Total number of pending transactions in the txpool.
* **queued** - Total number of queued transactions in the txpool.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://gnosis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"txpool_status","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "pending": 743,
        "queued": 0
    }
}
```
{% endcode %}
