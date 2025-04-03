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
curl https://t3rn.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 0,
    "result": "nitro/v3.5.4-217e414/linux-amd64/go1.23.1"
}
```
{% endcode %}
