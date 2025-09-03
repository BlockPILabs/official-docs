---
description: Retrieves the current slot number of the Solana blockchain.
---

# getSlot

#### **Parameters:**

**None**

#### **Returns:**

slots - tring - The current slot number on the Solana blockchain

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto geyser.proto
-H "x-token: <your-token>" 
-d '{}' 
solana.blockpi.network
geyser.Geyser/GetBlockHeight/GetSlot
```
{% endcode %}
