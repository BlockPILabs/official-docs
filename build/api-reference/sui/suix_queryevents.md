---
description: Return list of events for a specified query criteria.
---

# suix\_queryEvents

#### **Parameters:**

**query< EventFilter >** - The event query criteria. See [Event filter](https://docs.sui.io/build/event_api#event-filters) documentation for examples.

**cursor< EventID >** - Optional paging cursor

**limit< uint >** - Maximum number of items per page, default to \[QUERY\_MAX\_RESULT\_LIMIT] if not specified.

**descending\_order< Boolean >** - Query result ordering, default to false (ascending order), oldest record first.

#### **Returns:**

EventPage< Page\_for\_Event\_and\_EventID >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_queryEvents",
  "params": [
    {
      "MoveModule": {
        "package": "0x30651d6e8f93e0fb79b4bc65a512beb5b9f3378423de90ed03b694cecf443c72",
        "module": "test"
      }
    },
    {
      "txDigest": "Nb5kW8n655ApSBA19d2K8UVFGtMnJHa1mJQRH1h5N9L",
      "eventSeq": "1"
    },
    100,
    false
  ]
}'

// Result

```
{% endcode %}
