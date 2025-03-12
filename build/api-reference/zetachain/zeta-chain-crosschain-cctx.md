---
description: >-
  Queries a list of send items. This method only returns the latest 100
  pagination.
---

# /zeta-chain/crosschain/cctx

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/cctxPending

// Result
{
    "CrossChainTx": [
        {
            "creator": "",
            "index": "0x0000b92fc2450075794b4bb42371ad8d99c9017bfa9a2207b5780af3009f90c1",
            "zetaBurnt": "216476236984273420",
            "zetaMint": "216476236984273420",
            "zetaFees": "0",
            "relayedMessage": "",
            "cctx_status": {
                "status": "PendingOutbound",
                "statusMessage": "",
                "lastUpdateTimestamp": "1680108229"
            },
            "InBoundTxParams": {
                "sender": "0x71Ec5c05Aa669c4922569c1D33F7a81aaa218138",
                "senderChain": "ZETA",
                "inBoundTxObservedHash": "0x07f05b27963283cc023bfd321bd0ca6bccb5021da5be88e50cb7e12f0294ec7f",
                "inBoundTxObservedExternalHeight": "2091929",
                "inBoundTxFinalizedZetaHeight": "0",
                "inBoundTXBallotIndex": "0x0000b92fc2450075794b4bb42371ad8d99c9017bfa9a2207b5780af3009f90c1",
                "txOrigin": "0x43968994DAa79a3e23fb7f5df40f736Bc7c2625A"
            },
            "OutBoundTxParams": {
                "receiver": "0x00000000000000000000000043968994daa79a3e23fb7f5df40f736bc7c2625a",
                "receiverChain": "BSCTESTNET",
                "broadcaster": "0",
                "outBoundTxHash": "",
                "outBoundTxTSSNonce": "1305312",
                "outBoundTxGasLimit": "90000",
                "outBoundTxGasPrice": "13333333333",
                "outBoundTXBallotIndex": "",
                "outBoundTxFinalizedZetaHeight": "0",
                "outBoundTxObservedExternalHeight": "0"
            }
        },
         ......
    ]
}
```
{% endcode %}
