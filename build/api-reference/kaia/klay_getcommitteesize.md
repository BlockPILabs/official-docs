---
description: >-
  Returns the size of the committee at the specified block. If the parameter is
  not set, returns the size of the committee at the latest block.
---

# klay\_getCommitteeSize

#### **Parameters**

| Name            | Type         | Description                                                                               |
| --------------- | ------------ | ----------------------------------------------------------------------------------------- |
| QUANTITY \| TAG | block number | (optional) Integer or hexadecimal block number, or the string `"earliest"` or `"latest"`  |

#### **Return Value**

| Type     | Description             |
| -------- | ----------------------- |
| QUANTITY | The size of the council |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "method":"klay_getCommitteeSize", "params":["0x1b4"],"id":73}' http://klaytn.blockpi.network/v1/rpc/your-api-key
// Result
{
    "jsonrpc":"2.0",
    "id":73,
    "result":4
}
```
{% endcode %}
