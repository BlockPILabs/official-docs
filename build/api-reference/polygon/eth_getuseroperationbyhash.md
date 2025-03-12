---
description: returns a UserOperation by its hash returned from eth_sendUserOperation
---

# eth\_getUserOperationByHash

#### **Parameters:**

**string**- hash of the UserOperation

#### **Returns:**

**Object**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://polygon.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 0,
  "method": "eth_getUserOperationByHash",
  "params": [userOpHash, entrypointAddress]
}'

// Result
full UserOperation objest
```
{% endcode %}
