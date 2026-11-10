# eth\_newblockfilter

#### **Parameters:**

None

#### **Returns:**

**QUANTITY** - A filter id.

Creates a filter in the node, to notify when a new block arrives. To check if the state has changed, call [eth\_getFilterChanges](/broken/pages/0cd789adef23557181afd9c8706b230d990441a3).

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_newBlockFilter","params":[],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x24533652a38792560e855bbe493293a"
}
```
{% endcode %}
