---
description: >-
  Creates a new message call transaction or a contract creation for signed
  transactions.
---

# klay\_sendRawTransaction

#### **Parameters**

| Type | Description                  |
| ---- | ---------------------------- |
| DATA | The signed transaction data. |

#### **Return Value**

| Type         | Description                                                                    |
| ------------ | ------------------------------------------------------------------------------ |
| 32-byte DATA | The transaction hash or the zero hash if the transaction is not yet available. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_sendRawTransaction","params":[{see above}],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id":1,
  "result": "0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331"
}
```
{% endcode %}
