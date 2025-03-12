---
description: Parameters queries the parameters of the module.
---

# /zeta-chain/observer/params

#### **Parameters:**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/observer/params

// Result
{
  "params": {
    "BallotThresholds": [
      {
        "Chain": "BscTestnet",
        "Observation": "InBoundTx",
        "Threshold": "0.660000000000000000"
      },
      {
        "Chain": "BscTestnet",
        "Observation": "OutBoundTx",
        "Threshold": "0.660000000000000000"
      },
      {
        "Chain": "Goerli",
        "Observation": "InBoundTx",
        "Threshold": "0.660000000000000000"
      },
      {
        "Chain": "Goerli",
        "Observation": "OutBoundTx",
        "Threshold": "0.660000000000000000"
      },
      {
        "Chain": "Mumbai",
        "Observation": "InBoundTx",
        "Threshold": "0.660000000000000000"
      },
      {
        "Chain": "Mumbai",
        "Observation": "OutBoundTx",
        "Threshold": "0.660000000000000000"
      },
      {
        "Chain": "BTCTestnet",
        "Observation": "InBoundTx",
        "Threshold": "0.660000000000000000"
      },
      {
        "Chain": "BTCTestnet",
        "Observation": "OutBoundTx",
        "Threshold": "0.660000000000000000"
      },
      {
        "Chain": "Baobab",
        "Observation": "InBoundTx",
        "Threshold": "0.650000000000000000"
      },
      {
        "Chain": "Baobab",
        "Observation": "OutBoundTx",
        "Threshold": "0.650000000000000000"
      }
    ]
  }
}
```
{% endcode %}
