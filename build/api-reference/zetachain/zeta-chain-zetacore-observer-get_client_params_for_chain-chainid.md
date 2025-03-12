---
description: Queries a list of GetClientParamsForChain items.
---

# /zeta-chain/zetacore/observer/get\_client\_params\_for\_chain/{chainID}

#### **Parameters:**

**chainID-string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/zetacore/observer/get_client_params_for_chain/5
// Result
{
  "core_params": {
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
  }
}
```
{% endcode %}
