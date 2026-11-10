# eth\_getcode

#### **Parameters:**

**DATA, 20 Bytes** - address.

**QUANTITY|TAG** - integer block number, or the string "latest", "earliest" or "pending".

#### **Returns:**

**DATA** - the code from the given address.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getCode","params":["0x063f7cc5339f92a5fd7baf3d22233044fda1f327","latest"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x363d3d373d3d3d363d7310b0292fb853966d3039d80bbef98b1a9507f55f5af43d82803e903d91602b57fd5bf3"
}
```
{% endcode %}
