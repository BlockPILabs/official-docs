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
curl https://gnosis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": "Nethermind/v1.14.7+4fe81c6b/linux-x64/dotnet6.0.11",
    "id": 1
}
```
{% endcode %}
