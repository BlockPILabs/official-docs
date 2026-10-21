# vesting

Query vesting contracts that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`contract_address`** — array of strings, optional. Vesting contract address in any form. Maximum: 1000 addresses.
* **`wallet_address`** — array of strings, optional. Wallet address to filter by owner or sender. Maximum: 1000 addresses.
* **`check_whitelist`** — boolean, optional, default `False`. Check whether the wallet address is on the whitelist.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.

**Returns**

* `address_book` — object
* `vesting_contracts` — array of objects with fields `address`, `cliff_duration`, `owner_address`, `sender_address`, `start_time`, `total_amount`, `total_duration`, `unlock_period`, `whitelist`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/vesting?wallet_address=0%3AF785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78&limit=2'

// Result
{
  "vesting_contracts": [],
  "address_book": {}
}
```
{% endcode %}
