---
description: >-
  Uninstalls a filter with given id. Should always be called when watch is no
  longer needed.
---

# kaia\_uninstallFilter

The execution of this API can be limited by two node configurations to manage resources of Klaytn node safely.

#### **Parameters**

| Name   | Type     | Description  |
| ------ | -------- | ------------ |
| filter | QUANTITY | A filter id. |

#### **Return Value**

| Type    | Description                                                           |
| ------- | --------------------------------------------------------------------- |
| Boolean | `true` if the filter was successfully uninstalled, otherwise `false`. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_uninstallFilter","params":["0xb"],"id":73}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id":1,
  "result": true
}
```
{% endcode %}
