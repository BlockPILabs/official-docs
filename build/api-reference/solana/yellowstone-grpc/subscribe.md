---
description: >-
  Subscribe establishes a bidirectional streaming connection with the Geyser
  service to receive real-time updates about Solana blockchain events.
---

# subscribe

#### **Parameters:**

blockhash - bytes - The blockhash you want to validate

#### **Returns:**

result - object - The result representing the return value of a bidirectional stream method call with a Geyser gRPC subscription request and subscription update

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto geyser.proto
-d '{"slots": {}, "accounts": { }, "transactions": {}, "blocks": { "blocks": {"include_transactions": false, "include_accounts": true} }, "blocks_meta": {}, "accounts_data_slice": []}'
-H "x-token: <your-token>" 
solana.blockpi.network
geyser.Geyser/Subscribe
```
{% endcode %}
