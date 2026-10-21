# nft sales

Query GetGems NFT sales and auctions by sale or auction contract address.

{% hint style="info" %}
Only GetGems sale and auction contracts are indexed, so pass contract addresses — not NFT item addresses. An address that is not a GetGems sale contract returns an empty `nft_sales` array.
{% endhint %}

**Parameters**

* **`address`** — array of strings, required. Sale or auction contract address in any form. Maximum: 1000 addresses.

**Returns**

* `address_book` — object
* `metadata` — object
* `nft_sales` — array of objects with fields `address`, `code_hash`, `created_at`, `data_hash`, `details`, `last_transaction_lt`, `marketplace_address`, `nft_address`, `nft_item`, `nft_owner_address`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/nft/sales?address=0%3AED1691307050047117B998B561D8DE82D31FBF84910CED6EB5FC92E7485EF8A7'

// Result
{
  "nft_sales": [],
  "address_book": {},
  "metadata": {}
}
```
{% endcode %}
