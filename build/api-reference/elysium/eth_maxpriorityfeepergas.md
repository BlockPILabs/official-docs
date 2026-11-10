# eth\_maxpriorityfeepergas

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - integer of the current `maxPriorityFeePerGas` in wei, as suggested by the node. On Elysium the sequencer accepts a zero priority fee, so this value is commonly `0x0`.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_maxPriorityFeePerGas","params":[],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x0"
}
```
{% endcode %}
