---
description: Get the contract class definition associated with the given hash
---

# starknet\_getClass

#### **Parameters:**

**Block ID -** The hash of the requested block, or number (height) of the requested block, or a block tag

**CLASS\_HASH**  -  The hash of the requested contract class

#### **Returns:**

The contract class.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc":"2.0","method":"starknet_getClass","params":["latest","0x7d1bd0a80107d8ffdb7fe5158548ac852ff02e8823fda8704d8cfa5b2f532e4"],"id":1}'

// Result
{
    
}
```
{% endcode %}
