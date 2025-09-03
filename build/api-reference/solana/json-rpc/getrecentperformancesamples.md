---
description: >-
  Returns a list of recent performance samples, in reverse slot order.
  Performance samples are taken every 60 seconds and include the number of
  transactions and slots that occur in a given time window.
---

# getRecentPerformanceSamples

#### **Parameters:**

usize - optional - Number of samples to return (maximum 720)

#### **Returns:**

array - An array of performance sample objects

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getRecentPerformanceSamples",
     "params": [
       2
     ]
   }
'

// Result

```
{% endcode %}
