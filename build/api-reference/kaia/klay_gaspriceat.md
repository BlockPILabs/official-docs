---
description: Returns the unit price of the given block in peb.
---

# klay\_gasPriceAt

#### **Parameters**

| Type   | Description                                                   |
| ------ | ------------------------------------------------------------- |
| NUMBER | Block number. If omitted, latest unit price will be returned. |

#### **Return Value**

| Type     | Description                              |
| -------- | ---------------------------------------- |
| QUANTITY | Integer of the current gas price in peb. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_gasPriceAt","params":["0x64"],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id":1,
  "result": "0xAE9F7BCC00" // 750,000,000,000 peb = 750 ston
}
```
{% endcode %}
