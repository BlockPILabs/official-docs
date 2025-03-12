# /zeta-chain/observer/all\_observer\_mappers

#### **Parameters:**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/observer/all_observer_mappers

// Result
{
  "ObserverMappers": [
    {
      "index": "BTCTestnet-InBoundTx",
      "ObserverChain": "BTCTestnet",
      "ObservationType": "InBoundTx",
      "observerList": [
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j"
      ]
    },
    {
      "index": "BTCTestnet-OutBoundTx",
      "ObserverChain": "BTCTestnet",
      "ObservationType": "OutBoundTx",
      "observerList": [
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j"
      ]
    },
    {
      "index": "Baobab-InBoundTx",
      "ObserverChain": "Baobab",
      "ObservationType": "InBoundTx",
      "observerList": [
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j"
      ]
    },
    {
      "index": "Baobab-OutBoundTx",
      "ObserverChain": "Baobab",
      "ObservationType": "OutBoundTx",
      "observerList": [
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j"
      ]
    },
    {
      "index": "BscTestnet-InBoundTx",
      "ObserverChain": "BscTestnet",
      "ObservationType": "InBoundTx",
      "observerList": [
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j"
      ]
    },
    {
      "index": "BscTestnet-OutBoundTx",
      "ObserverChain": "BscTestnet",
      "ObservationType": "OutBoundTx",
      "observerList": [
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j"
      ]
    },
    {
      "index": "Goerli-InBoundTx",
      "ObserverChain": "Goerli",
      "ObservationType": "InBoundTx",
      "observerList": [
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j"
      ]
    },
    {
      "index": "Goerli-OutBoundTx",
      "ObserverChain": "Goerli",
      "ObservationType": "OutBoundTx",
      "observerList": [
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j"
      ]
    },
    {
      "index": "Mumbai-InBoundTx",
      "ObserverChain": "Mumbai",
      "ObservationType": "InBoundTx",
      "observerList": [
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j"
      ]
    },
    {
      "index": "Mumbai-OutBoundTx",
      "ObserverChain": "Mumbai",
      "ObservationType": "OutBoundTx",
      "observerList": [
        "zeta16c0wtwez2736xshha67ff9g87c8nh58w92meek",
        "zeta15q5rqp40q2kf7nmevhstx6lux4e22nuzpulnr9",
        "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84",
        "zeta1kk9jqwufhceveakcajv30whj68g228dccs2xe5",
        "zeta1lewf3hrqs04vl624cz2csqe4egdt06ylsrfn3j"
      ]
    }
  ]
}
```
{% endcode %}
