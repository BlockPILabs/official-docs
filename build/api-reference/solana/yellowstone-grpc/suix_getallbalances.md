---
description: Retrieves the current block height of the Solana blockchain.
---

# getBlockHeight

#### **Parameters:**

**None**

#### **Returns:**

Blockheight - string - The latest block height

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto geyser.proto
-H "x-token: <your-token>" 
-d '{}' 
solana.blockpi.network
geyser.Geyser/GetBlockHeight
```
{% endcode %}
