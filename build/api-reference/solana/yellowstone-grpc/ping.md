---
description: >-
  Sends a number of ping requests to the network to check the connection's
  responsiveness and status.
---

# ping

#### **Parameters:**

blockhash - bytes - The blockhash you want to validate

#### **Returns:**

status - integer - A message or indicator that confirms whether the ping was successful

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto geyser.proto
-H "x-token: <your-token>" 
-d '{"blockhash": "5Kd3N2Q3u6oQp9n2rE8cG7p8VY2w9a7YXrW1mM7r3X6Y"}' 
solana.blockpi.network
geyser.Geyser/GetBlockHeight/Ping
```
{% endcode %}
