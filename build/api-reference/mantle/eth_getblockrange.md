---
description: >-
  Returns the block info in the form of an array of block objects for multiple
  blocks within a specified range. (See eth_getBlockByHash for the structure of
  a block object)
---

# eth\_getBlockRange

#### **Parameters:**

**QUANTITY|TAG** - Integer | String, Starting block no. of the range, or one of `"earliest"`, `"latest"`, or `"pending"`, as in the [default block parameter](https://ethereum.org/en/developers/docs/apis/json-rpc/#default-block)

**QUANTITY|TAG** - Integer | String, Ending block no. of the range, or one of `"earliest"`, `"latest"`, or `"pending"`, as in the [default block parameter](https://ethereum.org/en/developers/docs/apis/json-rpc/#default-block)

**BOOLEAN** - If `true`, returns full transaction objects If `false`, returns transaction hashes only

#### **Returns:**

Block Object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://mantle.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
'{
    "jsonrpc": "2.0",
    "method": "eth_getBlockRange",
    "params": [
        "0x3e57a50",
        "0x3e57d96",
        true
    ],
    "id": 1
}'

// Result
{
    
}
```
{% endcode %}
