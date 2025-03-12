---
description: Queries a tSS by index.
---

# /zeta-chain/crosschain/TSS/{index}

#### **Parameters:**

**index - string**,&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/TSS/{BAOBAB}

// Result
{
  "TSS": {
    "creator": "",
    "index": "BAOBAB",
    "chain": "BAOBAB",
    "address": "0x7c125C1d515b8945841b3d5144a060115C58725F",
    "pubkey": "zetapub1addwnpepq2e8wxr4z64z9jpr05cq2xwkc032kdyp3vn3lqal4angczkcdzft74m07ym",
    "signer": [
      "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
      "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j",
      "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
      "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
      "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84"
    ],
    "finalizedZetaHeight": "507315"
  }
}
```
{% endcode %}
