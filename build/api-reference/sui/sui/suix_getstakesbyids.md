---
description: >-
  Return one or more [DelegatedStake]. If a Stake was withdrawn its status will
  be Unstaked.
---

# suix\_getStakesByIds

#### **Parameters:**

**staked\_sui\_ids<\[ ObjectID ]>**

#### **Returns:**

Vec<\[ DelegatedStake ]>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getStakesByIds",
  "params": [
    [
      "0xb2a5bea2e681ea5af4e59bd1abb0bb4fcb2747866ff92885a3c21a7703f56472",
      "0x1c198308aa0c71b771ada6b96c16fc9c0fa754b3c61936f77fcfdaa213c2f7b4"
    ]
  ]
}'

// Result

```
{% endcode %}
