---
description: Queries a list of GetCoreParams items.
---

# /zeta-chain/zetacore/observer/get\_core\_params

#### **Parameters:**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/observer/params

// Result
{
  "core_params": {
    "core_params": [
      {
        "confirmation_count": "6",
        "gas_price_ticker": "30",
        "in_tx_ticker": "8",
        "out_tx_ticker": "8",
        "watch_utxo_ticker": "0",
        "zeta_token_contract_address": "0x0000c304d2934c00db1d51995b9f6996affd17c0",
        "connector_contract_address": "0x00005e3125aba53c5652f9f0ce1a4cf91d8b15ea",
        "erc20_custody_contract_address": "0x000047f11c6e42293f433c82473532e869ce4ec5",
        "chain_id": "5",
        "outbound_tx_schedule_interval": "30",
        "outbound_tx_schedule_lookahead": "60"
      },
      {
        "confirmation_count": "6",
        "gas_price_ticker": "30",
        "in_tx_ticker": "5",
        "out_tx_ticker": "8",
        "watch_utxo_ticker": "0",
        "zeta_token_contract_address": "0x0000c9ec4042283e8139c74f4c64bcd1e0b9b54f",
        "connector_contract_address": "0x0000ecb8cdd25a18f12daa23f6422e07fbf8b9e1",
        "erc20_custody_contract_address": "0x0000a7db254145767262c6a81a7ee1650684258e",
        "chain_id": "97",
        "outbound_tx_schedule_interval": "30",
        "outbound_tx_schedule_lookahead": "60"
      },
      {
        "confirmation_count": "12",
        "gas_price_ticker": "30",
        "in_tx_ticker": "2",
        "out_tx_ticker": "8",
        "watch_utxo_ticker": "0",
        "zeta_token_contract_address": "0x0000c9ec4042283e8139c74f4c64bcd1e0b9b54f",
        "connector_contract_address": "0x0000ecb8cdd25a18f12daa23f6422e07fbf8b9e1",
        "erc20_custody_contract_address": "0x0000a7db254145767262c6a81a7ee1650684258e",
        "chain_id": "80001",
        "outbound_tx_schedule_interval": "30",
        "outbound_tx_schedule_lookahead": "60"
      },
      {
        "confirmation_count": "3",
        "gas_price_ticker": "5",
        "in_tx_ticker": "2",
        "out_tx_ticker": "3",
        "watch_utxo_ticker": "0",
        "zeta_token_contract_address": "",
        "connector_contract_address": "",
        "erc20_custody_contract_address": "",
        "chain_id": "7001",
        "outbound_tx_schedule_interval": "0",
        "outbound_tx_schedule_lookahead": "0"
      },
      {
        "confirmation_count": "2",
        "gas_price_ticker": "30",
        "in_tx_ticker": "120",
        "out_tx_ticker": "60",
        "watch_utxo_ticker": "30",
        "zeta_token_contract_address": "",
        "connector_contract_address": "",
        "erc20_custody_contract_address": "",
        "chain_id": "18332",
        "outbound_tx_schedule_interval": "30",
        "outbound_tx_schedule_lookahead": "60"
      }
    ]
  }
}
```
{% endcode %}
