---
description: Returns Keccak-256 (not the standardized SHA3-256) of the given data.
---

# web3\_sha3

#### **Parameters:**

**DATA** - the data to convert into a SHA3 hash

#### **Returns:**

**DATA** - The SHA3 result of the given string.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://gnosis.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"web3_sha3","params":["0x68656c6c6f20776f726c64"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "result": "0x47173285a8d7341e5e972fc677286384f802f8ef42a5ec5f03bbfa254cb01fad",
    "id": 1
}
```
{% endcode %}
