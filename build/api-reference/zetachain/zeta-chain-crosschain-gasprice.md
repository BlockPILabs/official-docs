---
description: Queries a list of gasPrice items.
---

# /zeta-chain/crosschain/gasPrice

#### **Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/gasPrice

// Result
{
  "GasPrice": [
    {
      "creator": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
      "index": "BAOBAB",
      "chain": "BAOBAB",
      "signers": [
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j",
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek"
      ],
      "blockNums": [
        "118586116",
        "118586110",
        "118586070",
        "118586074",
        "118586060"
      ],
      "prices": [
        "50000000000",
        "50000000000",
        "50000000000",
        "50000000000",
        "50000000000"
      ],
      "medianIndex": "2"
    },
    {
      "creator": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
      "index": "BSCTESTNET",
      "chain": "BSCTESTNET",
      "signers": [
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j",
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5"
      ],
      "blockNums": [
        "28490730",
        "28490715",
        "28490716",
        "28490712",
        "28490728"
      ],
      "prices": [
        "10000000000",
        "10000000000",
        "10000000000",
        "10000000000",
        "10000000000"
      ],
      "medianIndex": "2"
    },
    {
      "creator": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
      "index": "GOERLI",
      "chain": "GOERLI",
      "signers": [
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j",
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5"
      ],
      "blockNums": [
        "8742944",
        "8742942",
        "8742942",
        "8742941",
        "8742944"
      ],
      "prices": [
        "162081986059",
        "178680626904",
        "178680626904",
        "173906098486",
        "162081986059"
      ],
      "medianIndex": "3"
    },
    {
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
        "33745149",
        "33745127",
        "33745129",
        "33745122",
        "33745146"
      ],
      "prices": [
        "1879048192",
        "1879048192",
        "1879048192",
        "1822676747",
        "1879048192"
      ],
      "medianIndex": "1"
    }
  ],
  "pagination": {
    "next_key": null,
    "total": "4"
  }
}
```
{% endcode %}
