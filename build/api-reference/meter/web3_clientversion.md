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
curl https://meter.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": "Meter-Gear/1.2.47/linux/python3.9.13",
    "id": 1
}
```
{% endcode %}
