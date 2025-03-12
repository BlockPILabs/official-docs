---
description: Returns all events matching the given filter
---

# starknet\_getEvents

#### **Parameters:**

**filter** - The conditions used to filter the returned events

#### **Returns:**

All the event objects matching the filter.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "starknet_getEvents",
  "params": [
    {
      "from_block": "latest",
      "to_block": "latest",
      "address": "0x044e5b3f0471a26bc749ffa1d8dd8e43640e05f1b33cf05cef6adee6f5b1b4cf",
      "chunk_size": 10
    }
  ]
}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "events": []
    }
}
```
{% endcode %}
