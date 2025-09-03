---
description: Returns a list of prioritization fees from recent blocks.
---

# getRecentPrioritizationFees

#### **Parameters:**

array - optional - An array of Account addresses (up to a maximum of 128 addresses), as base-58 encoded strings

#### **Returns:**

array - An array of prioritization fee objects

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getRecentPrioritizationFees",
     "params": [
       ["CxELquR1gPP8wHe33gZ4QxqGB3sZ9RSwsJ2KshVewkFY"]
     ]
   }
'

// Result

```
{% endcode %}
