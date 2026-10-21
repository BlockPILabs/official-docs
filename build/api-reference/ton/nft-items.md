# nft items

Query NFT items that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`address`** — array of strings, optional. NFT item address in any form. Maximum: 1000 addresses.
* **`owner_address`** — array of strings, optional. Address of the NFT item owner in any form. Maximum: 1000 addresses.
* **`collection_address`** — array of strings, optional. Collection address in any form.
* **`index`** — array of strings, optional. Item index for the specified collection. Maximum: 1000 indexes.
* **`include_on_sale`** — boolean, optional, default `False`. Include NFT items listed in sales or auctions. Applies only when `owner_address` is provided.
* **`sort_by_last_transaction_lt`** — boolean, optional. Sort NFT items by `last_transaction_lt` in descending order. Results may be inconsistent while paginating with `limit` and `offset`.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.

**Returns**

* `address_book` — object
* `metadata` — object
* `nft_items` — array of objects with fields `address`, `auction_contract_address`, `code_hash`, `collection`, `collection_address`, `content`, `data_hash`, `index`, `init`, `last_transaction_lt`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/nft/items?limit=2'

// Result
{
  "nft_items": [
    {
      "address": "0:000000F6FCDC61D96265CA6B31BD98505AC3823B77FA8346264A5EBD7D1AB446",
      "init": true,
      "index": "4723",
      "collection_address": "0:4357CFBB796F7E1CD0FF86111FEA43EAFF16A6184265FAA6A7BBC085CB550F2D",
      "owner_address": "0:BFC8EC1A8F60A38B598DC404B3039B6A51452837DB30ABA5C09C5EEA7ED79013",
      "content": {
        "uri": "https://aquabreezewave.com/nft/guzlik0new.json"
      },
      "last_transaction_lt": "46816713000001",
      "code_hash": "Bn/BKm/wQyuuG8RfXTYvb+AegQqlOYtL2Er3eSUWWrI=",
      "data_hash": "S3LHQHsX63JZ8VBxtz7vcFFe2YDhycGxxwrSapmQaYg=",
      "collection": {
        "address": "0:4357CFBB796F7E1CD0FF86111FEA43EAFF16A6184265FAA6A7BBC085CB550F2D",
        "owner_address": "0:C71674D0FF9987A1CD71554D1C37B029E124214060B84CCADA068338B42627E9",
        "last_transaction_lt": "46816814000001",
        "next_item_index": "4897",
        "collection_content": {
          "uri": "https://aquabreezewave.com/colnew.json"
        },
        "data_hash": "OoNgxCTmdeSxHdQzKmDE40D7m3+mBgrn9HxTvfNQ3Mk=",
        "code_hash": "OshXvoj/zX5LKjBX5ydHu1G6QrsDn98PWZhU0sXLXT0="
      },
      "on_sale": false,
      "real_owner": "0:BFC8EC1A8F60A38B598DC404B3039B6A51452837DB30ABA5C09C5EEA7ED79013"
    }
  ],
  "address_book": {
    "0:000000F6FCDC61D96265CA6B31BD98505AC3823B77FA8346264A5EBD7D1AB446": {
      "user_friendly": "EQAAAAD2_Nxh2WJlymsxvZhQWsOCO3f6g0YmSl69fRq0RjKj",
      "domain": null,
      "interfaces": [
        "nft_item"
      ]
    },
    "0:000001340F4644EF4BF504118F1C8C04CC75FDF1721925295F90DD44ED8F0A86": {
      "user_friendly": "EQAAAAE0D0ZE70v1BBGPHIwEzHX98XIZJSlfkN1E7Y8KhlPm",
      "domain": null,
      "interfaces": []
    },
    "0:4357CFBB796F7E1CD0FF86111FEA43EAFF16A6184265FAA6A7BBC085CB550F2D": {
      "user_friendly": "EQBDV8-7eW9-HND_hhEf6kPq_xamGEJl-qanu8CFy1UPLQDG",
      "domain": null,
      "interfaces": [
        "nft_collection"
      ]
    },
    "0:70842A9D4A36C5823C70D045E68C69C80B3CD707A1433421073596CC8C5DF255": {
      "user_friendly": "UQBwhCqdSjbFgjxw0EXmjGnICzzXB6FDNCEHNZbMjF3yVcFr",
      "domain": "8833.ton",
      "interfaces": [
        "wallet_v5r1"
      ]
    },
    "0:9E7EB8E1083DBFEC7448AF6966C2DF596AA786FED76C781BC00C2EBAF37DE405": {
      "user_friendly": "EQCefrjhCD2_7HRIr2lmwt9ZaqeG_tdseBvADC66833kBS3y",
      "domain": null,
      "interfaces": [
        "nft_collection"
      ]
    },
    "0:BFC8EC1A8F60A38B598DC404B3039B6A51452837DB30ABA5C09C5EEA7ED79013": {
      "user_friendly": "UQC_yOwaj2Cji1mNxASzA5tqUUUoN9swq6XAnF7qfteQE4j7",
      "domain": null,
      "interfaces": [
        "wallet_v4r2"
      ]
    }
  }
}
```
{% endcode %}
