---
description: >-
  Retrieve EIP-4881 Deposit Tree Snapshot. Depending on Accept header it can be
  returned either as json or as bytes serialzed by SSZ
---

# /eth/v1/beacon/deposit\_snapshot

#### P**arameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/beacon/deposit_snapshot

// Result
{
    "data": {
        "finalized": [
            "0x8ba2e667c5fbe7666ff631bbe8fef23f10a9591d0ecbdf6ffe14c02c510b0b16",
            "0xfe2c2aa67c40931f82e959734980eacd7d2148cb7c881da196bb62ceb58789eb",
            "0x6a3fb9f400aded7a312b0718f1845e70da9ff2b35975fc3cb5401810e6aa3a76",
            "0xcb91f3f9893bd0d9d8168477702188bfe66fdcfc5edf4d45755d720a639f43bf",
            "0xf97dcc156aeedc3b52e5ec1de6f826ec67210068d8f25696b9893f5cbbe1e2d0",
            "0x734f36bcac5e9ee9d37740d30aee7de5971063d70ebd02e4622af63350b364b7",
            "0x546ab1b4f1fc5f2c612fcec2a7c02a7a7c79ba789fd46bdd9c2380fbef70118e",
            "0x7cbcae635d70629c7b69f04aff93bdc9b48da7184cece332a9a7f99f9d3df584",
            "0xa6fd97a6473a9fdeecc29d347d2f20d03b1201e1e1f1f038887f52eba753c2a7",
            "0x8234ef03f3cc399c06bdb139d0eb8e7dcbe1e4bb4ae903e5bd41b5cced74c3e4",
            "0x424383bede35037fd89fae772b137b6abdf829302548f31bb5b47dff14034cdb",
            "0xba71a0d23add8553527892c928a0478b4a68c39827dc0d7e2706dc842cd61200",
            "0x342f12f0f4206e46543d5d088f7274f708ca5d85d5af882fe465dac8ec1c4701",
            "0x3c0500daacb9ff19f8fd7eff6b6d30572701ff259eb3485daec25bed06f9e574"
        ],
        "deposit_root": "0xb29d072dbe25dffff8dd69e960d4815a26bd835a5a9aa77b5a632bb623d90578",
        "deposit_count": "1474453",
        "execution_block_hash": "0x02dd73c60cbf84f433e6ac98ebaf63996380e211407d912f5f38abbe15f28b19",
        "execution_block_height": "19876525"
    }
}
```
{% endcode %}
