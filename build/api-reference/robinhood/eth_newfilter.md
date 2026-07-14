# eth\_newfilter

#### **Parameters:**

**Object** - The filter options:

* **fromBlock: QUANTITY|TAG** - (optional, default: "latest") Integer block number, or "latest" for the last mined block
* **toBlock: QUANTITY|TAG** - (optional, default: "latest") Integer block number, or "latest" for the last mined block
* **address: DATA|Array, 20 Bytes** - (optional) Contract address or a list of addresses from which logs should originate.
* **topics: Array of DATA** - (optional) Array of 32 Bytes DATA topics.

#### **Returns:**

**QUANTITY** - A filter id.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://robinhood.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_newFilter","params":[{"fromBlock":"0x1","toBlock":"0x2"}],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0xe9ba06d78eacf6f686fbc6747e68c861"
}
```
{% endcode %}
