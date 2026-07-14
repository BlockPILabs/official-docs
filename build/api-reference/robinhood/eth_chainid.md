# eth\_chainid

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - big integer of the current chain id.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x1237"
}
```
{% endcode %}
