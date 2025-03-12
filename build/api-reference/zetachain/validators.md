---
description: >-
  Get Validators. Validators are sorted by voting power.  If the height field is
  set to a non-default value, upon success, the Cache-Control header will be set
  with the default maximum age.
---

# /validators

#### **Parameters:**

**height - int**, height to return. If no height is provided, it will fetch information regarding the latest block.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/validators?height=14183822

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "block_height": "2115729",
        "validators": [
            {
                "address": "0CE77A66422692185F4EE7DAFC212D2A2294BBAE",
                "pub_key": {
                    "type": "tendermint/PubKeyEd25519",
                    "value": "IYYt/r5YgdxYhwPWivBOgfGGBXMtd2ChQ8qv5RWqhvI="
                },
                "voting_power": "5000001000000",
                "proposer_priority": "-6625237053879"
            },
            {
                "address": "7BA1052999259832EA5D237E56DA46547006CA9D",
                "pub_key": {
                    "type": "tendermint/PubKeyEd25519",
                    "value": "YFidBWI0/eFh7yybDU4GJ+LRbPVNwxMMyGHgH5b5f4Q="
                },
                "voting_power": "5000001000000",
                "proposer_priority": "8374754075618"
            },
            {
                "address": "8D5804BDEFA39EDFA488062C1F67718250C366CD",
                "pub_key": {
                    "type": "tendermint/PubKeyEd25519",
                    "value": "4/CBdLhTDLAkkEkIi05fzLRD4kH+u6XplhIyJu5xhPo="
                },
                "voting_power": "5000001000000",
                "proposer_priority": "3374767030322"
            },
            {
                "address": "D84908FDC1549917028C7727B5E8D7803621F573",
                "pub_key": {
                    "type": "tendermint/PubKeyEd25519",
                    "value": "4ACkC+IwzpWDQg7G3QPv+h5hIQZcVKxyc4WQGyEPROo="
                },
                "voting_power": "5000001000000",
                "proposer_priority": "8374769138717"
            },
            {
                "address": "4DC45FE111D08B478EA6CEC45DE48F9B89B3BF62",
                "pub_key": {
                    "type": "tendermint/PubKeyEd25519",
                    "value": "pYQNipc5czjiOtf2EYB5JO5lHlXYK/RmH+npxXx15Z0="
                },
                "voting_power": "1100002",
                "proposer_priority": "5250941750119"
            },
            {
                "address": "2D274FF48703433A46AD6FAD636E0347B7ADC3F8",
                "pub_key": {
                    "type": "tendermint/PubKeyEd25519",
                    "value": "U9b5SFkZ2XzhcsR5RHSTbJg6+RzaA90g0j/lWyt8STw="
                },
                "voting_power": "3",
                "proposer_priority": "-18749994940894"
            }
        ],
        "count": "6",
        "total": "6"
    }
}
```
{% endcode %}
