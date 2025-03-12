---
description: >-
  Get Block.  If the height field is set to a non-default value, upon success,
  the Cache-Control header will be set with the default maximum age.
---

# /block

#### **Parameters:**

**height - int**, height to return. If no height is provided, it will fetch the latest block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/block?height=14183822

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "block_id": {
            "hash": "9DFF465BE04752B7685A6AF50C9BD5681985AC6AE8763AA0F4D377633248DD46",
            "parts": {
                "total": 1,
                "hash": "E22C1128320D5D2A683C401B29AFA50E801450CA052F259C3C528F231579A110"
            }
        },
        "block": {
            "header": {
                "version": {
                    "block": "11"
                },
                "chain_id": "athens_7001-1",
                "height": "2115661",
                "time": "2023-03-31T06:43:06.499294837Z",
                "last_block_id": {
                    "hash": "B1F6385A8C620DFF531E787FBA41202689BBB21A75B99880BA6E86B424D9F21A",
                    "parts": {
                        "total": 1,
                        "hash": "E375BFD748CDB510E8F323C00B9BE75165C3C539CBB26C6B2C8941666013045C"
                    }
                },
                "last_commit_hash": "90887BB82682EE65915544005ED4D682C6E77B7B62E733AA6BC7D9AD620C6F00",
                "data_hash": "63993DA41FC3D12EDD6AB7B8F66F82966918A5A969A54D915FC9CD09FCEFB3C3",
                "validators_hash": "D6732A30D4EDA7A71B7591F45946ACACACE1E35B64C3A03034F14AB5B1961529",
                "next_validators_hash": "D6732A30D4EDA7A71B7591F45946ACACACE1E35B64C3A03034F14AB5B1961529",
                "consensus_hash": "D976051F1620D15880ADD4C6E2D55BE2CCE6FA96426F6BD98D2F4BE80D807DAA",
                "app_hash": "01286FE51FB1A63F44647F54C17174B9E31CE7B779980BEA98E17250B5A7AF3E",
                "last_results_hash": "A248B8575955F796CDAC2CE2DFC062FD65FD0751ED1D020F4CB526E91749D199",
                "evidence_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
                "proposer_address": "0CE77A66422692185F4EE7DAFC212D2A2294BBAE"
            },
            "data": {
                "txs": [
                ......
                ]
            },
            "evidence": {
                "evidence": []
            },
            "last_commit": {
                "height": "2115660",
                "round": 0,
                "block_id": {
                    "hash": "B1F6385A8C620DFF531E787FBA41202689BBB21A75B99880BA6E86B424D9F21A",
                    "parts": {
                        "total": 1,
                        "hash": "E375BFD748CDB510E8F323C00B9BE75165C3C539CBB26C6B2C8941666013045C"
                    }
                },
                "signatures": [
                    {
                        "block_id_flag": 2,
                        "validator_address": "0CE77A66422692185F4EE7DAFC212D2A2294BBAE",
                        "timestamp": "2023-03-31T06:43:06.494991946Z",
                        "signature": "WTxcPcGWd0RxtCVcuy+/UctQxhDprVhanX2D18fs562bbHoPQ9eexH+Dq+anbSf3mEaC7CNwn/44XmNGPYkACA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "7BA1052999259832EA5D237E56DA46547006CA9D",
                        "timestamp": "2023-03-31T06:43:06.499393059Z",
                        "signature": "9rcOQ04BxbFOnsh96hTOhCXKjKxMihBgR/e9p/imEs8nNWTfdybVU5rNiUx8lY+bDRixvUS6wvBNqw0vVWLoBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "8D5804BDEFA39EDFA488062C1F67718250C366CD",
                        "timestamp": "2023-03-31T06:43:06.499294837Z",
                        "signature": "xa6uMZ8uz1Hok5TMpD3F9QYQos8awQd/lt1GHRaYQ9VkoKQzJ+OUT57eMJqeFiWj/Aq/g9Ps3OKw+HgvN/t9CQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "D84908FDC1549917028C7727B5E8D7803621F573",
                        "timestamp": "2023-03-31T06:43:06.49521508Z",
                        "signature": "BcpC33W4SarW6DnnmYq0D+dqI6HVUcZGWBz/mskbkLjYL6TFEjt0IwVmBlFPVy5NVRr+dRTviyKdOEcG+uKlBg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "4DC45FE111D08B478EA6CEC45DE48F9B89B3BF62",
                        "timestamp": "2023-03-31T06:43:06.50468782Z",
                        "signature": "oyHQYd4VDP3ICcnLGoNg8KHuGTznYRS5zWKMrL2pY9SBk6wVskZLho+1pXZSppGMR33lG1kwYcbGfggpPy2oDA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "2D274FF48703433A46AD6FAD636E0347B7ADC3F8",
                        "timestamp": "2023-03-31T06:43:06.507888052Z",
                        "signature": "Ix7utrwgtQeRojX675nCfhO7eWQegIa/jyY3fkajjaROtKmk7SXEhlheNxwFpTafv8v3q9uPtOrr1wDLBIbsAg=="
                    }
                ]
            }
        }
    }
}            
```
{% endcode %}
