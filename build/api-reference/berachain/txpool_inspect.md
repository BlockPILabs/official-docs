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
curl https://berachain-bartio.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"txpool_inspect","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "pending": {
            "0x06CB8CFBD729888168CE2552dA91B97C76c983C5": {
                "27103": "0x9fAa90d6797Bd01dB2035F820Fa662e38CcBaaab: 14000000000000000000 wei + 720000 gas × 10787794844 wei"
            },
            ......
```
{% endcode %}
