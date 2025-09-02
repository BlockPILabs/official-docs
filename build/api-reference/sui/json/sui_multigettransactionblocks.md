---
description: >-
  Returns an ordered list of transaction responses The method will throw an
  error if the input contains any duplicate or the input size exceeds
  QUERY_MAX_RESULT_LIMIT
---

# sui\_multiGetTransactionBlocks

#### **Parameters:**

**object\_ids<\[ ObjectID ]>** - The IDs of the queried objects&#x20;

**options< TransactionBlockResponseOptions >** - Config options to control which fields to fetch

#### **Returns:**

Vec<\[ TransactionBlockResponse ]>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_multiGetTransactionBlocks",
  "params": [
    [
      "61GhydW9kTXNU6LXktceLKM5svzLcDwW1eRU2UdQ9wov",
      "4TU9wToRuiYvPZZAtMzq3gfQEBuv91Nt5pkgWbVL8mR9",
      "HiWguwCqK3mWzhv5Qefb6pfhKdocWZo7gbToHED5Pzp7"
    ],
    {
      "showInput": true,
      "showRawInput": false,
      "showEffects": true,
      "showEvents": true,
      "showObjectChanges": false,
      "showBalanceChanges": false,
      "showRawEffects": false
    }
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": [
        {
            "digest": "61GhydW9kTXNU6LXktceLKM5svzLcDwW1eRU2UdQ9wov",
            "events": []
        },
        {
            "digest": "4TU9wToRuiYvPZZAtMzq3gfQEBuv91Nt5pkgWbVL8mR9",
            "events": []
        },
        {
            "digest": "HiWguwCqK3mWzhv5Qefb6pfhKdocWZo7gbToHED5Pzp7",
            "events": []
        }
    ],
    "id": 1
}
```
{% endcode %}
