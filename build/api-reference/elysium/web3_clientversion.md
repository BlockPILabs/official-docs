# web3\_clientversion

#### **Parameters:**

None

#### **Returns:**

**String** - The current client version.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "nitro/v3.12.2+5f02f3f-20261014T220458Z/linux-amd64/go1.25.12"
}
```
{% endcode %}
