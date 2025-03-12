---
description: >-
  Creates a filter object, based on filter options. To get all matching logs for
  specific filter, call eth_getFilterLogs. To check if the state has changed,
  call eth_getFilterChanges.
---

# eth\_newFilter

#### **Parameters:**

**Object** - The filter options:

* **fromBlock: QUANTITY|TAG** - (optional, default: "latest") Integer block number, or "latest" for the last mined block
* **toBlock: QUANTITY|TAG** - (optional, default: "latest") Integer block number, or "latest" for the last mined block
* **address: DATA|Array, 20 Bytes** - (optional) Contract address or a list of addresses from which logs should originate.
* **topics: Array of DATA** - (optional) Array of 32 Bytes DATA topics. Topics are order-dependent. Each topic can also be an array of DATA with “or” options.

#### **Returns:**

**QUANTITY** - A filter id.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://fantom.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_newFilter","params":[{"topics":["0x1234123412341234123412341111111111111111111111111111111111111111"]}],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0xa91fd9570ac139bf7e58f4562c82885c"
}
```
{% endcode %}
