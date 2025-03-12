---
description: >-
  Get Commit.  If the height field is set to a non-default value, upon success,
  the Cache-Control header will be set with the default maximum age.
---

# /commit

#### **Parameters:**

**height - int**, height to return. If no height is provided, it will fetch information regarding the latest block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/commit?height=14183822

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "signed_header": {
            "header": {
                "version": {
                    "block": "11"
                },
                "chain_id": "athens_7001-1",
                "height": "2115722",
                "time": "2023-03-31T06:48:30.288710799Z",
                "last_block_id": {
                    "hash": "D8BB61FA533AE7BAC4150C436D8F23D89A57272307FD2B60C8EA9EEAF3E2DF63",
                    "parts": {
                        "total": 1,
                        "hash": "35F5A0EFE7D17E930B52B7A5FE6648E9F7B339D8277E96D006BC6B2AC3F1499D"
                    }
                },
                "last_commit_hash": "88DD0FF15F56A68884E02DED436DC53B5DD5AE2910045D985F2331E5220E9AB2",
                "data_hash": "3286FE8F32E1D702FAF31730AC3298551061E117E976FDEE12A59AC8C274FAF1",
                "validators_hash": "D6732A30D4EDA7A71B7591F45946ACACACE1E35B64C3A03034F14AB5B1961529",
                "next_validators_hash": "D6732A30D4EDA7A71B7591F45946ACACACE1E35B64C3A03034F14AB5B1961529",
                "consensus_hash": "D976051F1620D15880ADD4C6E2D55BE2CCE6FA96426F6BD98D2F4BE80D807DAA",
                "app_hash": "1847D3AA886F378A0BED60EFE4B7D5949B41AC24E1DD78C4B363790C987AEE8C",
                "last_results_hash": "08B4240FDB7BC3CBD1F59CE9CF0D68EAE6656634B0CD1543198891CF8262AA6A",
                "evidence_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
                "proposer_address": "D84908FDC1549917028C7727B5E8D7803621F573"
            },
            "commit": {
                "height": "2115722",
                "round": 0,
                "block_id": {
                    "hash": "D753E9AA5523E87747F3421F02688EEB8FD00CE1DF1E5ECEDB6C86349B9CADE3",
                    "parts": {
                        "total": 2,
                        "hash": "D253072C0725295A3ABA2F6BA73A608A1CAF4E6046F672CF8EF649F589361949"
                    }
                },
                "signatures": [
                    {
                        "block_id_flag": 2,
                        "validator_address": "0CE77A66422692185F4EE7DAFC212D2A2294BBAE",
                        "timestamp": "2023-03-31T06:48:35.61105791Z",
                        "signature": "aUA0BY8HvrO6r/mKfgFK2dI3AVB1cmtjnBQb+Zt7Ndn39HgweklLp5rVCh+SxcJdtMpHjRwSruzmoMcKdlR5Aw=="
                    },
                    {
                        "block_id_flag": 1,
                        "validator_address": "",
                        "timestamp": "0001-01-01T00:00:00Z",
                        "signature": null
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "8D5804BDEFA39EDFA488062C1F67718250C366CD",
                        "timestamp": "2023-03-31T06:48:35.609674254Z",
                        "signature": "UMEYb9hFJTNmIL9Cb3IhTDxG1p9oha7wnN3DErAB5esSFSqJJb/5Mtmi9lJ2e4Y9vYoWIXd4czW4thjuOxPnBw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "D84908FDC1549917028C7727B5E8D7803621F573",
                        "timestamp": "2023-03-31T06:48:35.656293334Z",
                        "signature": "Z1cM67w218E63SeOR38RcTXXRYzmCc6qH+Xc6SJNvoaOHiJPafsLEh+D/lHFB7nVAeCEjgEkWYevluUk52wgCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "4DC45FE111D08B478EA6CEC45DE48F9B89B3BF62",
                        "timestamp": "2023-03-31T06:48:35.622177458Z",
                        "signature": "TJQMWOcdYhG+dmQfOB/RYPpIVlZOpPLgMLBnaMkeCe+p0+5701Pf1n9f+bh/lgISOv23ferYrQTpXwL9WBtsDQ=="
                    },
                    {
                        "block_id_flag": 1,
                        "validator_address": "",
                        "timestamp": "0001-01-01T00:00:00Z",
                        "signature": null
                    }
                ]
            }
        },
        "canonical": false
    }
}           
```
{% endcode %}
