---
description: Return transaction events.
---

# sui\_getEvents

#### **Parameters:**

**transaction\_digest< TransactionDigest >** - The event query criteria.

#### **Returns:**

Vec<\[ Event ]>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getEvents",
  "params": [
    "11a72GCQ5hGNpWGh2QhQkkusTEGS6EDqifJqxr7nSYX"
  ]
}'

// Result

```
{% endcode %}
