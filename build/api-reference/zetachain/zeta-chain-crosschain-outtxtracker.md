---
description: Queries a list of OutTxTracker items.
---

# /zeta-chain/crosschain/outTxTracker

#### **Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/outTxTracker

// Result
{
  "outTxTracker": [
    {
      "index": "BSCTESTNET-1205026",
      "chain": "BSCTESTNET",
      "nonce": "1205026",
      "hashList": [
        {
          "txHash": "0xcd97faed6e7e6999407c3694161466193159dbee283406aeb574dcfb5c068c12",
          "signer": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84"
        }
      ]
    },
    {
      "index": "BSCTESTNET-1205027",
      "chain": "BSCTESTNET",
      "nonce": "1205027",
      "hashList": [
        {
          "txHash": "0x124786537afcdd2bb8d6fb9f79976f4d4c6deeb95f20e8b10e3e0f1ff095a61a",
          "signer": "zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84"
        }
      ]
    },
    ......
  ],
  "pagination": {
    "next_key": "R09FUkxJLTk1NDIyMy8=",
    "total": "157"
  }
}    
```
{% endcode %}
