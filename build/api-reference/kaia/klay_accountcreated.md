---
description: >-
  Returns true if the account associated with the address is created. It returns
  false otherwise.
---

# klay\_accountCreated

#### **Parameters**

| Name                 | Type                    | Description                                                                                                |
| -------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| account              | 20-byte DATA            | Address                                                                                                    |
| block number or hash | QUANTITY \| TAG \| HASH | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`, or block hash. |

#### **Return Value**

| Type    | Description                       |
| ------- | --------------------------------- |
| Boolean | The existence of an input address |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_accountCreated","params":["0xa4f42d4d2a3a13874406435500950c9bf2d783db","latest"],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc":"2.0",
  "id":1,
  "result":true
}
```
{% endcode %}
