---
description: Queries a list of lastBlockHeight items.
---

# /zeta-chain/crosschain/lastBlockHeight

#### **Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zeta.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/lastBlockHeight

// Result
{
  "LastBlockHeight": [
    {
      "creator": "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
      "index": "BAOBAB",
      "chain": "BAOBAB",
      "lastSendHeight": "112729004",
      "lastReceiveHeight": "0"
    },
    {
      "creator": "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j",
      "index": "BSCTESTNET",
      "chain": "BSCTESTNET",
      "lastSendHeight": "28489163",
      "lastReceiveHeight": "0"
    },
    {
      "creator": "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
      "index": "GOERLI",
      "chain": "GOERLI",
      "lastSendHeight": "8742763",
      "lastReceiveHeight": "0"
    },
    {
      "creator": "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
      "index": "MUMBAI",
      "chain": "MUMBAI",
      "lastSendHeight": "33744060",
      "lastReceiveHeight": "0"
    }
  ],
  "pagination": {
    "next_key": null,
    "total": "4"
  }
}
```
{% endcode %}
