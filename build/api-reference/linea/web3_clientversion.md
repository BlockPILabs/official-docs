---
description: Returns the current client version.
---

# web3\_clientVersion

#### **Parameters:**

None

#### **Returns:**

**String** - The current client version

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://linea.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "Geth/v1.11.6-stable-ea9e62ca/linux-amd64/go1.20.3"
}
```
{% endcode %}
