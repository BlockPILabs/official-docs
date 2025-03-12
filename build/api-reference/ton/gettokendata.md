# /getTokenData

Get NFT or Jetton information.



**Parameters:**

**address - string,** Address of NFT collection/item or Jetton master/wallet smart contract

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getTokenData?address=EQCgH4od_xrY2pviA7MI30zdKG6z-7d2mh79Ki4GRVwRfHXM' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "init": true,
    "index": 0,
    "owner_address": "EQACaKYuhOZZSN5cHitEmp6qSOhlPS7yAavTtZTUYF3BcAek",
    "content": {
      "type": "offchain",
      "data": "https://nft.ton.diamonds/inner-landscapes/creativity/creativity.json"
    },
    "contract_type": "nft_item"
  }
}
```
{% endcode %}
