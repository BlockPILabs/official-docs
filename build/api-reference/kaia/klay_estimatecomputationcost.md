---
description: >-
  Generates and returns an estimate of how much computation cost will be spent
  to execute the transaction.
---

# klay\_estimateComputationCost

#### **Parameters**

See [klay\_call](broken-reference) parameters, except that all properties are optional. If no gas limit is specified, the Klaytn node uses the default gas limit (uint64 / 2) as an upper bound.

#### **Return Value**

| Type     | Description                          |
| -------- | ------------------------------------ |
| QUANTITY | The amount of computation cost used. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_estimateComputationCost","params":[{"from":"0x73718c4980728857f3aa5148e9d1b471efa3a7dd", "to":"0x069942a3ca0dabf495dba872533134205764bc9c", "value":"0x0", "data":"0x2a31efc7000000000000000000000000000000000000000000000000000000000000271000000000000000000000000000000000000000000000000000000000000000420000000000000000000000000000000000000000000000000000000000003039"}, "latest"],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0","id":1,
  "result": "0x1e8b0ad"
}
```
{% endcode %}
