# eth\_newfilter

#### **Parameters:**

**Object** - The filter options:

* **fromBlock: QUANTITY|TAG** - (optional, default: "latest") Integer block number, or "latest" for the last mined block
* **toBlock: QUANTITY|TAG** - (optional, default: "latest") Integer block number, or "latest" for the last mined block
* **address: DATA|Array, 20 Bytes** - (optional) Contract address or a list of addresses from which logs should originate.
* **topics: Array of DATA** - (optional) Array of 32 Bytes DATA topics.

#### **Returns:**

**QUANTITY** - A filter id.

{% hint style="info" %}
The block range of `eth_newFilter` is limited to **1024** blocks. Requests with a wider range will get an error.
{% endhint %}

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_newFilter","params":[{"fromBlock":"0x37ad01","toBlock":"latest"}],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0xd442cd2c1ac870d169589ed7b8d818c6"
}
```
{% endcode %}
