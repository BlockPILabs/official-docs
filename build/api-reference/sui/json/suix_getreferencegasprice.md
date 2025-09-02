---
description: Return the reference gas price for the network
---

# suix\_getReferenceGasPrice

#### **Parameters:**

None

#### **Returns:**

SuiSystemStateSummary< SuiSystemStateSummary >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getReferenceGasPrice",
  "params": []
}'

// Result
{
    "jsonrpc": "2.0",
    "result": "750",
    "id": 1
}
```
{% endcode %}
