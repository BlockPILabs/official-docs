# metadata

Query metadata for the specified addresses.

**Parameters**

* **`address`** — array of strings, required. List of addresses in any form to include in the metadata response. Maximum: 1024 addresses.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/metadata?address=EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs'

// Result
{
  "0:B113A994B5024A16719F69139328EB759596C38A25F59028B146FECDC3621DFE": {
    "is_indexed": true,
    "token_info": [
      {
        "valid": true,
        "type": "jetton_masters",
        "name": "Tether USD",
        "symbol": "USD₮",
        "description": "Tether Token for Tether USD",
        "image": "https://tether.to/images/logoCircle.png",
        "is_nsfw": false,
        "is_scam": false,
        "extra": {
          "_image_big": "https://proxy.toncenter.com/yz-3m7auC_anGW1Ym_SF2mjKl-o8Dnss1dQVxz4304k/pr:big/bG9jYWw6Ly8vMTEvZjIvMTFmMjE1ZTc0YWQxMGZkY…",
          "_image_medium": "https://proxy.toncenter.com/HIgyb4_W9CJmt5bxYup_WyBY0o6hKyjl0sFwJWH2L5w/pr:medium/bG9jYWw6Ly8vMTEvZjIvMTFmMjE1ZTc0YWQxMG…",
          "_image_small": "https://proxy.toncenter.com/zw1kB_VnqUT_mcakALKtiJ4aCJ9XKhu_WqB7XMGxdD4/pr:small/bG9jYWw6Ly8vMTEvZjIvMTFmMjE1ZTc0YWQxMGZ…",
          "decimals": "6",
          "uri": "https://tether.to/usdt-ton.json"
        }
      }
    ]
  }
}
```
{% endcode %}
