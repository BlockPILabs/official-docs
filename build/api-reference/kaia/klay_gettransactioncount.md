---
description: Returns the number of transactions sent from an address.
---

# klay\_getTransactionCount

#### **Parameters**

| Type                    | Description                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| 20-byte DATA            | Address                                                                                                    |
| QUANTITY \| TAG \| HASH | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`, or block hash. |

#### **Return Value**

<table><thead><tr><th width="259">Type</th><th>Description</th></tr></thead><tbody><tr><td>QUANTITY</td><td>Integer of the number of transactions send from this address.</td></tr></tbody></table>

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_getTransactionCount","params":["0xc94770007dda54cF92009BFF0dE90c06F603a09f","latest"],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
 "jsonrpc": "2.0",
 "id":1,
 "result": "0x1" // 1
}
```
{% endcode %}
