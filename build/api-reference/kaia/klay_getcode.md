---
description: Returns code at a given address.
---

# kaia\_getCode

#### **Parameters**

| Type                    | Description                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| 20-byte DATA            | Address                                                                                                    |
| QUANTITY \| TAG \| HASH | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`, or block hash. |

#### **Return Value**

| Type | Description                       |
| ---- | --------------------------------- |
| DATA | The code from the given address.. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_getCode","params":["0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b", "0x2"],"id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id":1,
  "result":   "0x600160008035811a818181146012578301005b601b6001356025565b8060005260206000f25b600060078202905091905056"
}
```
{% endcode %}
