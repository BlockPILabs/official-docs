---
description: Checks whether a given blockhash is still valid on the Solana blockchain.
---

# isBlockhashValid

#### **Parameters:**

blockhash - bytes - The blockhash you want to validate

#### **Returns:**

valid - boolean - A boolean value (true or false) indicating whether the blockhash is still valid

slot - string - The slot number associated with the blockhash

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto geyser.proto
-H "x-token: <your-token>" 
-d '{"blockhash": "5Kd3N2Q3u6oQp9n2rE8cG7p8VY2w9a7YXrW1mM7r3X6Y"}' 
solana.blockpi.network
geyser.Geyser/GetBlockHeight/Version
```
{% endcode %}
