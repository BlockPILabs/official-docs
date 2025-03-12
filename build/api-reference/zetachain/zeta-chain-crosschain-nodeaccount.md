---
description: Queries a list of nodeAccount items.
---

# /zeta-chain/crosschain/nodeAccount

#### **Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/nodeAccount

// Result
{
  "NodeAccount": [
    {
      "creator": "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
      "index": "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
      "nodeAddress": "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
      "pubkeySet": {
        "secp256k1": "zetapub1addwnpepq0y4zjwqd7aljxme8d5w3wpuelyj55jxhmn6h0u7y695esll6ragyvyanvl",
        "ed25519": ""
      },
      "nodeStatus": "Unknown"
    },
    {
      "creator": "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
      "index": "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
      "nodeAddress": "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
      "pubkeySet": {
        "secp256k1": "zetapub1addwnpepqw7ls4yhg2u8ev0l74ukqcat4m53k4zj4mqsgwfc252u0m5tejshvvyscqy",
        "ed25519": ""
      },
      "nodeStatus": "Unknown"
    },
    {
      "creator": "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
      "index": "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
      "nodeAddress": "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
      "pubkeySet": {
        "secp256k1": "zetapub1addwnpepqvs7ctdynw88zynt4275lf2a2r43yjgskqeeqdlefq7w6s6h25w4xmmtgx3",
        "ed25519": ""
      },
      "nodeStatus": "Unknown"
    },
    {
      "creator": "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j",
      "index": "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j",
      "nodeAddress": "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j",
      "pubkeySet": {
        "secp256k1": "zetapub1addwnpepqd87xkh9je2zthjthjqeq5uq64h2n25389786kwvulfuxfdtywjjq9nj9km",
        "ed25519": ""
      },
      "nodeStatus": "Unknown"
    },
    {
      "creator": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
      "index": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
      "nodeAddress": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
      "pubkeySet": {
        "secp256k1": "zetapub1addwnpepqgftrzjj735glqcghqhn5zjeut4tytqrqza4ayvkjg5fr5wl5q4nyft465a",
        "ed25519": ""
      },
      "nodeStatus": "Unknown"
    }
  ],
  "pagination": {
    "next_key": null,
    "total": "5"
  }
}
```
{% endcode %}
