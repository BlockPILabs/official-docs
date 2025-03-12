---
description: Queries a gasPrice by index.
---

# /zeta-chain/crosschain/gasPrice/{index}

#### **Parameters:**

**index - string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/gasPrice/MUMBAI

// Result
{
  "GasPrice": {
    "creator": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
    "index": "MUMBAI",
    "chain": "MUMBAI",
    "signers": [
      "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
      "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
      "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j",
      "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
      "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5"
    ],
    "blockNums": [
      "33745177",
      "33745184",
      "33745185",
      "33745179",
      "33745174"
    ],
    "prices": [
      "2500000016",
      "2500000016",
      "2187212094",
      "2500000016",
      "2500000016"
    ],
    "medianIndex": "1"
  }
}
```
{% endcode %}
