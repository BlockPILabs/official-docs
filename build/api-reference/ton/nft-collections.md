# nft collections

Query NFT collections that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`collection_address`** — array of strings, optional. Collection address in any form. Maximum: 1024 addresses.
* **`owner_address`** — array of strings, optional. Address of the collection owner in any form. Maximum: 1024 addresses.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.

**Returns**

* `address_book` — object
* `metadata` — object
* `nft_collections` — array of objects with fields `address`, `code_hash`, `collection_content`, `data_hash`, `last_transaction_lt`, `next_item_index`, `owner_address`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/nft/collections?limit=2'

// Result
{
  "nft_collections": [
    {
      "address": "-1:035D180AA6918B9F3D9756DEA7D599CB908290E18FEE14CD4B0788DC2B60CED7",
      "owner_address": null,
      "last_transaction_lt": "52186208000001",
      "next_item_index": "-1",
      "collection_content": {
        "name": "test collection"
      },
      "data_hash": "YWFEYzei52qsvP40CDWUihGoTH62cqW6/NgClIVm5nQ=",
      "code_hash": "iEEMIg+CIYFmgmnOg+ucwNOznCGZnItV3gM2CiDnwoI="
    }
  ],
  "address_book": {
    "-1:035D180AA6918B9F3D9756DEA7D599CB908290E18FEE14CD4B0788DC2B60CED7": {
      "user_friendly": "Ef8DXRgKppGLnz2XVt6n1ZnLkIKQ4Y_uFM1LB4jcK2DO17mi",
      "domain": null,
      "interfaces": [
        "nft_collection"
      ]
    },
    "-1:80D78A35F955A14B679FAA887FF4CD5BFC0F43B4A4EEA2A7E6927F3701B273C2": {
      "user_friendly": "Ef-A14o1-VWhS2efqoh_9M1b_A9DtKTuoqfmkn83AbJzwoyq",
      "domain": null,
      "interfaces": [
        "dns"
      ]
    }
  },
  "metadata": {
    "-1:035D180AA6918B9F3D9756DEA7D599CB908290E18FEE14CD4B0788DC2B60CED7": {
      "is_indexed": true,
      "token_info": [
        {
          "valid": true,
          "type": "nft_collections",
          "name": "test collection",
          "is_nsfw": false,
          "is_scam": false
        }
      ]
    },
    "-1:80D78A35F955A14B679FAA887FF4CD5BFC0F43B4A4EEA2A7E6927F3701B273C2": {
      "is_indexed": true,
      "token_info": [
        {
          "valid": true,
          "type": "nft_collections",
          "name": "Telegram Usernames",
          "description": "Unique addresses in Telegram’s ecosystem of more than 700 million active users.",
          "image": "https://nft.fragment.com/usernames.svg",
          "is_nsfw": false,
          "is_scam": false,
          "extra": {
            "_image_big": "https://proxy.toncenter.com/kC6_m6KgfDLvpR5GN2mlkfI9-OJrNmF7RFST2xdy33w/pr:big/bG9jYWw6Ly8vZmYvYjEvZmZiMTNkNjEyZmFlYWUyO…",
            "_image_medium": "https://proxy.toncenter.com/Dqyi0h-mtWc78Y8Kc7EsSx7sEIcW766kdR3fRKOpHaw/pr:medium/bG9jYWw6Ly8vZmYvYjEvZmZiMTNkNjEyZmFlYW…",
            "_image_small": "https://proxy.toncenter.com/eVckAgBLqVyxMUGEmH418Pv7klMXf6q52m5UZXGPqsE/pr:small/bG9jYWw6Ly8vZmYvYjEvZmZiMTNkNjEyZmFlYWU…",
            "external_link": "https://fragment.com/",
            "uri": "https://nft.fragment.com/usernames.json"
          }
        }
      ]
    }
  }
}
```
{% endcode %}
