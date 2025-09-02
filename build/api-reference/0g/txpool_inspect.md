---
description: >-
  Returns a list with a textual summary of all the transactions currently
  pending for inclusion in the next block(s), as well as the ones that are being
  scheduled for future execution only.
---

# txpool\_inspect

#### **Parameters:**

None

### Returns:

**array** - list of pending and queued transations, with each having the following fields:&#x20;

* **pending** - Array of transaction objects, with textual data.
* **queued** - Array of transaction objects, with textual data.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://0g-galileo.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"txpool_inspect","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {as described above}
}
```
{% endcode %}
