# dns activeauctions

Returns DNS auctions where the address is the current leading bidder. Use `bidding` for open auctions and `won` for ended but unclaimed auctions. Claimed auctions are no longer returned. Ordering for `bidding` and `all` can change as auctions update. Use larger limits when paginating. Set `include_nft_items` to include NFT details. NFT and collection metadata is returned separately.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`bidder`** — string, required. Address of the current leading bidder.
* **`state`** — string, optional, default `all`. Filter by auction state.
* **`include_nft_items`** — boolean, optional, default `False`. Include NFT item details.
* **`after`** — string, optional. Opaque pagination cursor from `next_cursor` of the previous page. Returns rows strictly after it and is preferred over `offset`.
* **`limit`** — integer, optional, default `100`. Limit the number of rows to return.
* **`offset`** — integer, optional, default `0`. Rows to skip. Do not combine this parameter with `after`.

**Returns**

* `address_book` — object
* `auctions` — array of objects with fields `auction_end_time`, `domain`, `finished`, `last_fill_up_time`, `max_bid_address`, `max_bid_amount`, `nft_item`, `nft_item_address`
* `metadata` — object
* `next_cursor` — string

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/dns/activeAuctions?bidder=0%3AED1691307050047117B998B561D8DE82D31FBF84910CED6EB5FC92E7485EF8A7'

// Result
{
  "auctions": [],
  "address_book": {},
  "metadata": {},
  "next_cursor": null
}
```
{% endcode %}
