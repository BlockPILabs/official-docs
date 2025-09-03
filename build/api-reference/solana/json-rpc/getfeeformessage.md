---
description: Get the fee the network will charge for a particular Message
---

# getFeeForMessage

#### **Parameters:**

string - required - Base-64 encoded Message

object - optional - Configuration object.

#### **Returns:**

u64 - Fee corresponding to the message at the specified blockhash

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "getFeeForMessage",
     "params": [
       "AQABAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEBAQAA",
       {
         "commitment": "processed"
       }
     ]
   }
'

// Result

```
{% endcode %}
