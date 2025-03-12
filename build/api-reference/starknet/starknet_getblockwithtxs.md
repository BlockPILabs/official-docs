---
description: Get block information with full transactions given the block id
---

# starknet\_getBlockWithTxs

#### **Parameters:**

**BLOCK\_PARAM** -  Expected one of `block_number`, `block_hash`, `latest`, `pending`.

#### **Returns:**

The resulting block information with full transactions.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_getBlockWithTxs","params":["latest"],"id":0}'

// Result
{
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "block_hash": "0x6d8a120adc2ba5603bed38ef563cd11aea61ad8f3177b70a8d7088d1467154f",
        "block_number": 472388,
        "l1_gas_price": {
            "price_in_wei": "0xa5ae43c81"
        },
        "new_root": "0x57ee2a837cb700a5657f3d82876f1da80061df6bcb7ef3d708bc1d20b76aaa0",
        "parent_hash": "0xa1023fcb278f5b413052ede0dd6ffafab3bbb60c5a0f61b819d80e75b66766",
        "sequencer_address": "0x1176a1bd84444c89232ec27754698e5d2e7e1a7f1539f12027f28b23ec9f3d8",
        "starknet_version": "0.12.2",
        "status": "ACCEPTED_ON_L2",
        "timestamp": 1702868316,
        "transactions": [
            {
                "calldata": [
                    "0x2",
                    "0x53c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8",
                    "0x219209e083275171774dab1df80982e9df2096516f06319c5c6d71ae0a8480c",
                    "0x3",
                    "0x7a6f98c03379b9513ca84cca1373ff452a7462a3b61598f0af5bb27ad7f76d1",
                    "0xffffffffffffffffffffffffffffffff",
                    "0xffffffffffffffffffffffffffffffff",
                    "0x7a6f98c03379b9513ca84cca1373ff452a7462a3b61598f0af5bb27ad7f76d1",
                    "0x2c0f7bf2d6cf5304c29171bf493feb222fef84bdaf17805a6574b0c2e8bcc87",
                    "0x9",
                    "0xf701e",
                    "0x0",
                    "0x1a135eda354ae",
                    "0x0",
                    "0x2",
                    "0x53c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8",
                    "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
                    "0x1729b9cca1f0924550437b7562792d3b4fcb91596902e204843dcd302e8ec01",
                    "0x18c7aee7177"
                ],
                "max_fee": "0x33659a0d76980",
                "nonce": "0x2f",
                "sender_address": "0x1729b9cca1f0924550437b7562792d3b4fcb91596902e204843dcd302e8ec01",
                "signature": [
                    "0x38ba3a46dcb427d6c213d66326808aacfc116079221a7a04fffd4741b909d44",
                    "0xf385111efe84d22c6af6e18913aee422ff77a28ce18c94cf46946eff161528"
                ],
                "transaction_hash": "0x799b60b1861153bd28f543df5fa46347e793b8fffc3be718642f36439030735",
                "type": "INVOKE",
                "version": "0x1"
            },
            .....
}
```
{% endcode %}
