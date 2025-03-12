---
description: Queries a list of ObserversByChainAndType items.
---

# /zeta-chain/observer/observers\_by\_chain/{observation\_chain}

#### **Parameters:**

**observation\_chain- string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/observer/observers_by_chain/goerli_testnet

// Result
{
  "observers": [
    "zeta1ggqzjf5726uu7xc6pfwg00lny79w6t3a3utpw5",
    "zeta1hk05v9len8u0c2xrwxgfknvcskpd4vncm7ehch",
    "zeta1g323lusfa9qqvjvupajre2dphuem999fahc086",
    "zeta1mte0r3jzkf2rkd7ex4p3xsd3fxqg7q29q0wxl5",
    "zeta18pksjzclks34qkqyaahf2rakss80mnusju77cm",
    "zeta18f7wch6kpfdmk6dk9qqhkszpjwrymev4fpte8p",
    "zeta1w8qa37h22h884vxedmprvwtd3z2nwakxu9k935",
    "zeta1j8g8ch4uqgl3gtet3nntvczaeppmlxajqwh5u6",
    "zeta1dxyzsket66vt886ap0gnzlnu5pv0y99v086wnz",
    "zeta1w5czgpk5kc9etxw2anzhr0uyrr4fqks32qmk6k",
    "zeta1ymnrwg9e3xr9xkw42ygzjx34dyvwvtc23cnnxz",
    "zeta15ruj2tc76pnj9xtw64utktee7cc7w6vzaes73z"
  ]
}
```
{% endcode %}
