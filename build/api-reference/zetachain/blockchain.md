---
description: >-
  Get block headers for minHeight <= height <= maxHeight.  At most 20 items will
  be returned.  Upon success, the Cache-Control header will be set with the
  default maximum age.
---

# /blockchain

#### **Parameters:**

**minHeight - int**, Minimum block height to return

**maxHeight- int**, Maximumblock height to return

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/blockchain

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "last_height": "2115614",
        "block_metas": [
            {
                "block_id": {
                    "hash": "77C737AE8A55AF5603E17028CB8CE4864852CCC707FA272001AF01A9F5DC92E3",
                    "parts": {
                        "total": 1,
                        "hash": "C5296D389BB5314A47246BFBA5AA5EA44BB0721447210E4E663A0BDF8460B7CD"
                    }
                },
                "block_size": "18016",
                "header": {
                    "version": {
                        "block": "11"
                    },
                    "chain_id": "athens_7001-1",
                    "height": "2115614",
                    "time": "2023-03-31T06:38:57.046975021Z",
                    "last_block_id": {
                        "hash": "AD3DB3E722CDC9229CD00A2B8947E1CE2C9F5143CBC29489723B6969226721E0",
                        "parts": {
                            "total": 1,
                            "hash": "41233BAECAE59F5F7F903A013AE288117682E5EC814E08ECBEFD7E3472B15C99"
                        }
                    },
                    "last_commit_hash": "DD7800C7FBF8F1BE740C53A2BFC543DDF55F7B648537589E19B747935AFAEEE4",
                    "data_hash": "E29E855601601FABD1574529C230236CCFD8BEFA2FB6DB4D9E295BEC3206F261",
                    "validators_hash": "D6732A30D4EDA7A71B7591F45946ACACACE1E35B64C3A03034F14AB5B1961529",
                    "next_validators_hash": "D6732A30D4EDA7A71B7591F45946ACACACE1E35B64C3A03034F14AB5B1961529",
                    "consensus_hash": "D976051F1620D15880ADD4C6E2D55BE2CCE6FA96426F6BD98D2F4BE80D807DAA",
                    "app_hash": "4DD7AC938C5EB6C65506FEB41FC7ED65D4AF4FCC52FBB4CD2341FA45EBC3D91A",
                    "last_results_hash": "E8EC4AB5C8B52ED5CFE73E3BA8F4B649492BC853D6E452B5C5C346DFD19A7469",
                    "evidence_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
                    "proposer_address": "D84908FDC1549917028C7727B5E8D7803621F573"
                },
                "num_txs": "30"
            },
            ......
        ]
    }
}
```
{% endcode %}
