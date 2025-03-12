---
description: Queries a list of ForeignCoins items.
---

# /zeta-chain/fungible/foreign\_coins

#### **Parameters:**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/zetacore/fungible/foreign_coins

// Result
{
  "foreignCoins": [
    {
      "index": "BNB-BSCTESTNET",
      "zrc20ContractAddress": "0x13A0c5930C028511Dc02665E7285134B6d11A5f4",
      "erc20ContractAddress": "",
      "foreignChain": "BSCTESTNET",
      "decimals": 18,
      "name": "BNB-BSCTESTNET",
      "symbol": "tBNB",
      "coinType": "Gas"
    },
    {
      "index": "BTC-BTCTESTNET",
      "zrc20ContractAddress": "0x48f80608B672DC30DC7e3dbBd0343c5F02C738Eb",
      "erc20ContractAddress": "",
      "foreignChain": "BTCTESTNET",
      "decimals": 8,
      "name": "BTC-BTCTESTNET",
      "symbol": "tBTC",
      "coinType": "Gas"
    },
    {
      "index": "ETH-GOERLI",
      "zrc20ContractAddress": "0x91d18e54DAf4F677cB28167158d6dd21F6aB3921",
      "erc20ContractAddress": "",
      "foreignChain": "GOERLI",
      "decimals": 18,
      "name": "ETH-GOERLI",
      "symbol": "gETH",
      "coinType": "Gas"
    },
    {
      "index": "KLAY",
      "zrc20ContractAddress": "0x65a45c57636f9BcCeD4fe193A602008578BcA90b",
      "erc20ContractAddress": "",
      "foreignChain": "BAOBAB",
      "decimals": 18,
      "name": "KLAY",
      "symbol": "tKLAY",
      "coinType": "Gas"
    },
    {
      "index": "MATIC-MUMBAI",
      "zrc20ContractAddress": "0xd97B1de3619ed2c6BEb3860147E30cA8A7dC9891",
      "erc20ContractAddress": "",
      "foreignChain": "MUMBAI",
      "decimals": 18,
      "name": "MATIC-MUMBAI",
      "symbol": "tMATIC",
      "coinType": "Gas"
    }
  ],
  "pagination": {
    "next_key": null,
    "total": "5"
  }
}
```
{% endcode %}
