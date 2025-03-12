---
description: >-
  Returns a list with a textual summary of all the transactions currently
  pending for inclusion in the next block(s), as well as the ones that are being
  scheduled for future execution only.
---

# txpool\_inspect

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://viction.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"txpool_inspect","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "pending": {
            "0x0302Dc89Df5d20c18f4d7E86491A6dF29eA06689": {
                "74": "0xA01d0D978E8b2E2a2f1b60C640680598bc4A366C: 20000800000000000 wei + 116771 gas × 300000000 wei"
            },
            ......
            "0xF53a9Dc529c8F3adE8Af664B21627C89e2D9AF8f": {
                "64": "0xA01d0D978E8b2E2a2f1b60C640680598bc4A366C: 20000800000000000 wei + 110460 gas × 300000000 wei"
            }
        },
        "queued": {}
    }
}
```
{% endcode %}
