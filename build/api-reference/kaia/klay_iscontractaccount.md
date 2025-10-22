---
description: >-
  Returns true if an input account has a non-empty codeHash at the time of a
  specific block number. It returns false if the account is an EOA or a smart
  contract account which doesn't have codeHash.
---

# kaia\_isContractAccount

#### **Parameters**

| Name                 | Type                    | Description                                                                                                |
| -------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| address              | 20-byte DATA            | Address                                                                                                    |
| block number or hash | QUANTITY \| TAG \| HASH | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`, or block hash. |

#### **Return Value**

| Type    | Description                                                             |
| ------- | ----------------------------------------------------------------------- |
| Boolean | `true` means the input parameter is an existing smart contract address. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_isContractAccount","params":["0x2f07d5b3fa1051460099dc9ea0c2975b6ea67776", "latest"],"id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
```
{% endcode %}
