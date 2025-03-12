---
description: Queries a ForeignCoins by index.
---

# /zeta-chain/fungible/foreign\_coins/{index}

#### **Parameters:**

**index - string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/zetacore/fungible/foreign_coins/BNB-BSCTESTNET

// Result
{
  "foreignCoins": {
    "index": "BNB-BSCTESTNET",
    "zrc20ContractAddress": "0x13A0c5930C028511Dc02665E7285134B6d11A5f4",
    "erc20ContractAddress": "",
    "foreignChain": "BSCTESTNET",
    "decimals": 18,
    "name": "BNB-BSCTESTNET",
    "symbol": "tBNB",
    "coinType": "Gas"
  }
}
```
{% endcode %}
