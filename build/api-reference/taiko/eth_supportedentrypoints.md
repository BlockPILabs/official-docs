---
description: returns an array of the entryPoint addresses supported by the bundler
---

# eth\_supportedEntryPoints

#### **Parameters:**

**None**

#### **Returns:**

**string -** the current entrypoint address

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://taiko.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 0,
  "method": "eth_supportedEntryPoints",
  "params": []
}'

// Result
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": ["0x00...", "0x01..."],
}
```
{% endcode %}
