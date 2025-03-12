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
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "erigon/2.29.0/linux-amd64/go1.19.2"
}
```
{% endcode %}
