---
description: Queries a list of send items.
---

# /zeta-chain/crosschain/cctx

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/cctx

// Result
{
  "CrossChainTx": [
    {
      "creator": "zeta1hk05v9len8u0c2xrwxgfknvcskpd4vncm7ehch",
      "index": "0x00039af9e4df747316866064d6907e936520cd0d1d4264237bc906400571fa20",
      "zeta_fees": "0",
      "relayed_message": "",
      "cctx_status": {
        "status": "OutboundMined",
        "status_message": "First half of EVM transfer Completed",
        "lastUpdate_timestamp": "1688068482"
      },
      "inbound_tx_params": {
        "sender": "0x271dd8063C2ee25D4124DD254D25610A84065006",
        "sender_chain_id": "5",
        "tx_origin": "0x271dd8063C2ee25D4124DD254D25610A84065006",
        "coin_type": "Zeta",
        "asset": "",
        "amount": "1",
        "inbound_tx_observed_hash": "0xab40fcbcf93a88fbffb30d2170eb3e41fa43e7d84f430b1cdc39a20bc46b282e",
        "inbound_tx_observed_external_height": "9262317",
        "inbound_tx_ballot_index": "0x00039af9e4df747316866064d6907e936520cd0d1d4264237bc906400571fa20",
        "inbound_tx_finalized_zeta_height": "0"
      },
         ......
    ]
}
```
{% endcode %}
