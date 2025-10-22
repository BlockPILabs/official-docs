---
description: Returns a list of addresses owned by client.
---

# kaia\_accounts

#### **Parameters**

None

#### **Return Value**

| Type                  | Description                    |
| --------------------- | ------------------------------ |
| Array of 20-byte DATA | Addresses owned by the client. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_accounts","params":[],"id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc":"2.0",
  "id":1,
  "result": ["0xc94770007dda54cF92009BFF0dE90c06F603a09f"]
}
```
{% endcode %}
