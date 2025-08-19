---
description: Return the list of dynamic field objects owned by an object.
---

# suix\_getDynamicFields

#### **Parameters:**

**parent\_object\_id< ObjectID >** - The ID of the parent object&#x20;

**cursor< ObjectID >** - An optional paging cursor. If provided, the query will start from the next item after the specified cursor. Default to start from the first item if not specified.&#x20;

**limit< uint >** - Maximum item returned per page, default to \[QUERY\_MAX\_RESULT\_LIMIT] if not specified.

#### **Returns:**

DynamicFieldPage< Page\_for\_DynamicFieldInfo\_and\_ObjectID >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getDynamicFields",
  "params": [
    "0xe15bb8de6dadd21835dfe44f4973139c15f93ddea0f8c3da994d9ead562ce76e",
    "0xa9334aeacc435c70ab9635e47a277d8f8dd9d87765d1aadec2db8cc24c312542",
    3
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "data": [],
        "nextCursor": "0xa9334aeacc435c70ab9635e47a277d8f8dd9d87765d1aadec2db8cc24c312542",
        "hasNextPage": false
    },
    "id": 1
}
```
{% endcode %}
