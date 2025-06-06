---
description: Returns traces matching given filter.
---

# trace\_filter

#### **Parameters:**

**Object** - The filter object

* **fromBlock: Quantity | Tag** - (optional) From this block.
* **toBlock: Quantity | Tag** - (optional) To this block.
* **fromAddress: Array** - (optional) Sent from these addresses.
* **toAddress: Address** - (optional) Sent to these addresses.
* **after: Quantity** - (optional) The offset trace number
* **count: Quantity** - (optional) Integer number of traces to display in a batch.

#### **Returns:**

**Array**- Trace object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://fantom.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"trace_filter","params":[{"fromBlock":"0xf2f8c7","toBlock":"0xf2f8c8"}],"id":1,"jsonrpc":"2.0"}'
      
// Result
{
      "jsonrpc":"2.0",
      "id":1,
      "result":{as described above}
}
```
{% endcode %}
