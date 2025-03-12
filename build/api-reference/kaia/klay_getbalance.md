---
description: Returns the balance of the account of given address.
---

# klay\_getBalance

#### **Parameters**

| Name                 | Type                    | Description                                                                                                |
| -------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| address              | 20-byte DATA            | Address to check for balance.                                                                              |
| block number or hash | QUANTITY \| TAG \| HASH | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`, or block hash. |

#### **Return Value**

| Type     | Description                            |
| -------- | -------------------------------------- |
| QUANTITY | Integer of the current balance in peb. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_getBalance","params":["0xc94770007dda54cF92009BFF0dE90c06F603a09f", "latest"],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0","id":1,
  "result": "0x0234c8a3397aab58" // 158972490234375000
}
```
{% endcode %}
