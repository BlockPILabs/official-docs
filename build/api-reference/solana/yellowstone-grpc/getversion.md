---
description: >-
  Retrieves the version information for both the Geyser gRPC service and the
  connected Solana node.
---

# getVersion

#### **Parameters:**

**None**

#### **Returns:**

version - object - The version object&#x20;

extra - object - The extra object&#x20;

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto geyser.proto
-H "x-token: <your-token>" 
-d '{}' 
solana.blockpi.network
geyser.Geyser/GetBlockHeight/Version
```
{% endcode %}
