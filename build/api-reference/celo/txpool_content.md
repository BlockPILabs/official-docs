---
description: >-
  list the exact details of all the transactions currently pending for inclusion
  in the next block(s), as well as the ones that are being scheduled for future
  execution only.
---

# txpool\_content

#### **Parameters:**

None

#### Returns:

| Type        | Description                          |
| ----------- | ------------------------------------ |
| JSON string | The content of the transaction pool. |

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://celo.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"txpool_content","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        ......
    }
}
```
{% endcode %}
