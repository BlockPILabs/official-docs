---
description: Return list of transactions for a specified query criteria.
---

# suix\_queryTransactionBlocks

#### **Parameters:**

**query< TransactionBlockResponseQuery >** - The transaction query criteria.&#x20;

**cursor< TransactionDigest >** -  An optional paging cursor. If provided, the query will start from the next item after the specified cursor. Default to start from the first item if not specified.&#x20;

**limit< uint >** - Maximum item returned per page, default to QUERY\_MAX\_RESULT\_LIMIT if not specified.&#x20;

**descending\_order< Boolean >** -  Query result ordering, default to false (ascending order), oldest record first.

#### **Returns:**

TransactionBlocksPage< Page\_for\_TransactionBlockResponse\_and\_TransactionDigest >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_queryTransactionBlocks",
  "params": [
    {
      "filter": {
        "InputObject": "0x93633829fcba6d6e0ccb13d3dbfe7614b81ea76b255e5d435032cd8595f37eb8"
      },
      "options": null
    },
    "HxidAfFfyr4kXSiWeVq1J6Tk526YUVDoSUY5PSnS4tEJ",
    100,
    false
  ]
}'

// Result

```
{% endcode %}
