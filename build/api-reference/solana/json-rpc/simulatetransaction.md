---
description: Simulate sending a transaction
---

# simulateTransaction

#### **Parameters:**

string - required - Transaction, as an encoded string.

object - optional - Configuration object

#### **Returns:**

object - The result

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://solana.blockpi.network/v1/rpc/your-rpc-key
  POST -H "Content-Type: application/json" -d ' 
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "simulateTransaction",
     "params": [
       "AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAEEjNmKiZGiOtSZ+g0//wH5kEQo3+UzictY+KlLV8hjXcs44M/Xnr+1SlZsqS6cFMQc46yj9PIsxqkycxJmXT+veJjIvefX4nhY9rY+B5qreeqTHu4mG6Xtxr5udn4MN8PnBt324e51j94YQl285GzN2rYa/E2DuQ0n/r35KNihi/zamQ6EeyeeVDvPVgUO2W3Lgt9hT+CfyqHvIa11egFPCgEDAwIBAAkDZAAAAAAAAAA=",
       {
         "commitment": "confirmed",
         "encoding": "base64",
         "replaceRecentBlockhash": true
       }
     ]
   }
'

// Result

```
{% endcode %}
