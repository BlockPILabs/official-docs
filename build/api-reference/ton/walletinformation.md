# walletinformation

Get wallet smart contract information. Supports the following wallet versions: `v1r1`, `v1r2`, `v1r3`, `v2r1`, `v2r2`, `v3r1`, `v3r2`, `v4r1`, `v4r2`, `v5beta`, and `v5r1`. If the account is not a wallet, returns error code `409`.

{% hint style="info" %}
Returns `409 not a wallet` when the address is not a supported wallet contract.
{% endhint %}

**Parameters**

* **`address`** — string, required. Account address in any form.
* **`use_v2`** — boolean, optional, default `True`. Use the API v2 method. This option is not recommended.

**Returns**

* `balance` — string
* `last_transaction_hash` — string
* `last_transaction_lt` — string
* `seqno` — integer
* `status` — string
* `suspended` — boolean
* `wallet_id` — integer
* `wallet_type` — string

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/walletInformation?address=0%3AF785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78'

// Result
{
  "balance": "5307033668",
  "wallet_type": "wallet v4 r2",
  "seqno": 29203,
  "wallet_id": 698983191,
  "last_transaction_lt": "111332924000017",
  "last_transaction_hash": "a30PDWY23++d6YkYp6C1Q/n8XAdFudT+tvnywZjeNlw=",
  "status": "active"
}
```
{% endcode %}
