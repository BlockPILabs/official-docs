# jetton transfers

Query jetton transfers that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND. `start_utime` / `end_utime` are Unix seconds (UTC); `*_lt` values are logical times and should be passed as strings.
{% endhint %}

**Parameters**

* **`owner_address`** — array of strings, optional. Address of the jetton wallet owner in any form. Maximum: 1000 addresses.
* **`jetton_wallet`** — array of strings, optional. Jetton wallet address in any form. Maximum: 1000 addresses.
* **`jetton_master`** — string, optional. Jetton master address in any form.
* **`direction`** — string, optional. Direction of the transfer. Applies only when `owner_address` is provided.
* **`start_utime`** — integer, optional. Query transactions with a generation timestamp at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query transactions with a generation timestamp at or before the specified timestamp.
* **`start_lt`** — integer, optional. Query transactions where `lt` is at or above the specified value.
* **`end_lt`** — integer, optional. Query transactions where `lt` is at or below the specified value.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional, default `desc`. Sort transactions by `lt`.

**Returns**

* `address_book` — object
* `jetton_transfers` — array of objects with fields `amount`, `custom_payload`, `decoded_custom_payload`, `decoded_forward_payload`, `destination`, `forward_payload`, `forward_ton_amount`, `jetton_master`, `query_id`, `response_destination`
* `metadata` — object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/jetton/transfers?limit=2'

// Result
{
  "jetton_transfers": [
    {
      "query_id": "16901608857448193594",
      "source": "0:F785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78",
      "destination": "0:852443F8599FE6A5DA34FE43049AC4E0BEB3071BB2BFB56635EA9421287C283A",
      "amount": "900000",
      "source_wallet": "0:35F94592910A839F6977122D4DE04DCB0FB184BEC5F7BBE0889436B62AD99442",
      "jetton_master": "0:B113A994B5024A16719F69139328EB759596C38A25F59028B146FECDC3621DFE",
      "transaction_hash": "9AHrS0yLmvFddIvPKpCcaQbmueO0UzsxeiGWBrfeHAI=",
      "transaction_lt": "111332924000012",
      "transaction_now": 1792550079,
      "transaction_aborted": false,
      "response_destination": "0:F785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78",
      "custom_payload": null,
      "decoded_custom_payload": null,
      "forward_ton_amount": "1",
      "forward_payload": "te6cckEBAQEAJwAASgAAAAA2MCBUZWxlZ3JhbSBTdGFycyAKClJlZiN1dHhid05XcXCyUIbO",
      "decoded_forward_payload": {
        "@type": "text_comment",
        "comment": "60 Telegram Stars \n\nRef#utxbwNWqp",
        "type": "text_comment"
      },
      "trace_id": "J40sZCP7Y24/XGnJmnpiMtm18o1QjTSQnSm6sBmhLEM="
    }
  ],
  "address_book": {
    "0:0C83008C452ABDBB5F76795C9F87D5252FA646A014F505859244655FC78C3774": {
      "user_friendly": "UQAMgwCMRSq9u192eVyfh9UlL6ZGoBT1BYWSRGVfx4w3dCi9",
      "domain": null,
      "interfaces": [
        "wallet_v4r2"
      ]
    },
    "0:35F94592910A839F6977122D4DE04DCB0FB184BEC5F7BBE0889436B62AD99442": {
      "user_friendly": "EQA1-UWSkQqDn2l3Ei1N4E3LD7GEvsX3u-CIlDa2KtmUQkPd",
      "domain": null,
      "interfaces": [
        "jetton_wallet_governed"
      ]
    },
    "0:57F631F311841CC3A742ECB64BCBB636DCE081D1DF98F7DFC33A0645ECA74620": {
      "user_friendly": "EQBX9jHzEYQcw6dC7LZLy7Y23OCB0d-Y99_DOgZF7KdGIMhc",
      "domain": null,
      "interfaces": []
    },
    "0:852443F8599FE6A5DA34FE43049AC4E0BEB3071BB2BFB56635EA9421287C283A": {
      "user_friendly": "EQCFJEP4WZ_mpdo0_kMEmsTgvrMHG7K_tWY16pQhKHwoOoy2",
      "domain": null,
      "interfaces": [
        "wallet_highload_v3r1"
      ]
    },
    "0:95DAB184FAB09C1DA88E82B16EA81B7DF297050991069B8ED9B3FDE620B3BEDA": {
      "user_friendly": "EQCV2rGE-rCcHaiOgrFuqBt98pcFCZEGm47Zs_3mILO-2hxe",
      "domain": null,
      "interfaces": [
        "jetton_master"
      ]
    },
    "0:B113A994B5024A16719F69139328EB759596C38A25F59028B146FECDC3621DFE": {
      "user_friendly": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",
      "domain": null,
      "interfaces": [
        "jetton_master"
      ]
    },
    "0:F6F7FA82331E7F14B078B9BD38655210DD558A04277EC50450D3DC1A7797E27B": {
      "user_friendly": "EQD29_qCMx5_FLB4ub04ZVIQ3VWKBCd-xQRQ09wad5fie6mO",
      "domain": null,
      "interfaces": [
        "jetton_wallet_v1"
      ]
    },
    "0:F785629E3E268E1CF3B22C8DEFD99DEB9487E5DC979B913EC67B007F1C2D5E78": {
      "user_friendly": "UQD3hWKePiaOHPOyLI3v2Z3rlIfl3JebkT7GewB_HC1eeP-y",
      "domain": null,
      "interfaces": [
        "wallet_v4r2"
      ]
    }
  }
}
```
{% endcode %}
