---
description: Queries a lastBlockHeight by index.
---

# /zeta-chain/crosschain/lastBlockHeight/{index}

#### **Parameters:**

**index - string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zeta.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/lastBlockHeight/MUMBAI

// Result
{
  "LastBlockHeight": {
    "creator": "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
    "index": "MUMBAI",
    "chain": "MUMBAI",
    "lastSendHeight": "33744060",
    "lastReceiveHeight": "0"
  }
}
```
{% endcode %}
