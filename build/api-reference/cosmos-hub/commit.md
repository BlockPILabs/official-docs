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
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/commit?height=14183822

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
                "chain_id": "cosmoshub-4",
                "height": "14183822",
                "time": "2023-02-22T07:02:28.186373674Z",
                "last_block_id": {
                    "hash": "AA83830192C2F4C606FB351888A6110844B9DE9F9DB0D139D5F43BD5420FB657",
                    "parts": {
                        "total": 1,
                        "hash": "7B427742BC05C487C456C9AFE27101F31CAC9FD8EFD4CDA3CE907BDFD9FFA240"
                    }
                },
                "last_commit_hash": "6CECBD40AF8E9ED2766BBDE0209CC07AE4DDDCE0FE5737E4091F27C7E1B88E70",
                "data_hash": "23E47B2D0F4A115082B9AF566DB3618BB7E143CB26C42C194725EDD78A4A69A5",
                "validators_hash": "72C90481C1525AAC72E7F330A7AEE985458995725BF2C84B2EE0599490D845DE",
                "next_validators_hash": "72C90481C1525AAC72E7F330A7AEE985458995725BF2C84B2EE0599490D845DE",
                "consensus_hash": "80364965B7C2CC9DE961C0998B47A7F93F1970077EB882E0ED1C3822408888C7",
                "app_hash": "323B71A2A9B4995916A2832E507F2F30CD7FF18371FCE23D291A892DC56048E1",
                "last_results_hash": "062A583EC0608F483E15CEFCCBB981323993E3D0EDCCC77C7D07D08623ED3219",
                "evidence_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
                "proposer_address": "83F47D7747B0F633A6BA0DF49B7DCF61F90AA1B0"
            },
            "commit": {
                "height": "14183822",
                "round": 0,
                "block_id": {
                    "hash": "55728BEBE614C989F40720FDCD3A565115407BDCA0D0BBEEE6A51350E8BB412F",
                    "parts": {
                        "total": 1,
                        "hash": "E88010DC45941059FA174E1979F013C91157E1CBA1A1832036493B12B18E2FC8"
                    }
                },
                "signatures": [
                    {
                        "block_id_flag": 2,
                        "validator_address": "AC2D56057CD84765E6FBE318979093E8E44AA18F",
                        "timestamp": "2023-02-22T07:02:34.725046703Z",
                        "signature": "K0Fw5CR7x44UvLe5sJliRfMk8GtqwzwS5I+YAY+86i65/fL1Tmrkr58pbqi3mVee+vY3rg0bKTdC8IgnKS6FBg=="
                    },
                    ......
                ]
            }
        },
        "canonical": true
    }
}                    
```
{% endcode %}
