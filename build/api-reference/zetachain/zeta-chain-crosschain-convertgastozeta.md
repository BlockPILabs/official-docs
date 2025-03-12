# /zeta-chain/crosschain/convertGasToZeta

#### **Parameters:**

**chain - string**

**gasLimit - string**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/convertGasToZeta?chain=MUMBAI&gasLimit=220000

// Result
{
  "outboundGasInZeta": "2534313729842650",
  "protocolFeeInZeta": "2000000000000000000",
  "ZetaBlockHeight": "2099956"
}
```
{% endcode %}
