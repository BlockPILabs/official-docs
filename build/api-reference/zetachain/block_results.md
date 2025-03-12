---
description: >-
  Get block_results. When the discard_abci_responses storage flag is enabled,
  this endpoint will return an error.
---

# /block\_results

If the `height` field is set to a non-default value, upon success, the `Cache-Control` header will be set with the default maximum age.

#### **Parameters:**

**height - int**, height to return. If no height is provided, it will fetch information regarding the latest block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/block_by_hash?hash=0x55728BEBE614C989F40720FDCD3A565115407BDCA0D0BBEEE6A51350E8BB412F

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "height": "2115710",
        "txs_results": [
            {
                "code": 0,
                "data": "CjsKOS96ZXRhY2hhaW4uemV0YWNvcmUuY3Jvc3NjaGFpbi5Nc2dWb3RlT25PYnNlcnZlZEluYm91bmRUeA==",
                "log": "[{\"events\":[{\"type\":\"message\",\"attributes\":[{\"key\":\"action\",\"value\":\"SendVoter\"}]}]}]",
                "info": "",
                "gas_wanted": "10000000",
                "gas_used": "105961",
                "events": [
                    {
                        "type": "coin_spent",
                        "attributes": [
                            {
                                "key": "c3BlbmRlcg==",
                                "value": "emV0YTF0NHprbTk4d2Y2MjVrN3k1bnR2ODUwcnF6eTNyZDRhMHN2NnU4NA==",
                                "index": true
                            },
                            {
                                "key": "YW1vdW50",
                                "value": "NDAwMDBhemV0YQ==",
                                "index": true
                            }
                        ]
                    },
                    ......
                 ]
            }
        ],
        "validator_updates": null,
        "consensus_param_updates": {
            "block": {
                "max_bytes": "22020096",
                "max_gas": "500000000"
            },
            "evidence": {
                "max_age_num_blocks": "100000",
                "max_age_duration": "172800000000000",
                "max_bytes": "1048576"
            },
            "validator": {
                "pub_key_types": [
                    "ed25519"
                ]
            }
        }
    }
}
```
{% endcode %}
