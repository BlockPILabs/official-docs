# nft transfers

Query NFT transfers that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND. `start_utime` / `end_utime` are Unix seconds (UTC); `*_lt` values are logical times and should be passed as strings.
{% endhint %}

**Parameters**

* **`owner_address`** — array of strings, optional. Address of the NFT owner in any form. Maximum: 1000 addresses.
* **`item_address`** — array of strings, optional. Address of the NFT item in any form. Maximum: 1000 addresses.
* **`collection_address`** — string, optional. Collection address in any form.
* **`direction`** — string, optional. Direction of the transfer.
* **`start_utime`** — integer, optional. Query transactions with a generation timestamp at or after the specified timestamp.
* **`end_utime`** — integer, optional. Query transactions with a generation timestamp at or before the specified timestamp.
* **`start_lt`** — integer, optional. Query transactions where `lt` is at or above the specified value.
* **`end_lt`** — integer, optional. Query transactions where `lt` is at or below the specified value.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.
* **`sort`** — string, optional, default `desc`. Sort transactions by `lt`.

**Returns**

* `address_book` — object
* `metadata` — object
* `nft_transfers` — array of objects with fields `custom_payload`, `decoded_custom_payload`, `decoded_forward_payload`, `forward_amount`, `forward_payload`, `new_owner`, `nft_address`, `nft_collection`, `old_owner`, `query_id`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/nft/transfers?limit=2'

// Result
{
  "nft_transfers": [
    {
      "query_id": "0",
      "nft_address": "0:9AB482CD6260254D8000B88D509102C929A7BD276D35CFD3097313A4C9766EAE",
      "nft_collection": "0:80D78A35F955A14B679FAA887FF4CD5BFC0F43B4A4EEA2A7E6927F3701B273C2",
      "transaction_hash": "nlLkgQ6Mfi6M27tTRvqCaRfQCAf31fM5AkJLNw3omWc=",
      "transaction_lt": "111332939000009",
      "transaction_now": 1792550085,
      "transaction_aborted": false,
      "old_owner": "0:3C43F2C3740AB71C24BE3E60DB3C30EB8D05F6D36D97E2703DFEF00B854CEC64",
      "new_owner": "0:1BAFAB7E448FB67B45B00C904717BA6F7CD5075035D1A4FA92919E700C064C14",
      "response_destination": "0:1BAFAB7E448FB67B45B00C904717BA6F7CD5075035D1A4FA92919E700C064C14",
      "custom_payload": null,
      "decoded_custom_payload": null,
      "forward_amount": "1",
      "forward_payload": null,
      "decoded_forward_payload": null,
      "trace_id": "hBqIWhNRJoJZYejUcEGD5dim+C0d7UpPQgewBPfkxkg="
    }
  ],
  "address_book": {
    "0:10528CE851C2B677CF371CA7F0348A802C4E9689C66139B93476C909730A48F8": {
      "user_friendly": "UQAQUozoUcK2d883HKfwNIqALE6WicZhObk0dskJcwpI-PAH",
      "domain": null,
      "interfaces": [
        "wallet_v4r2"
      ]
    },
    "0:1BAFAB7E448FB67B45B00C904717BA6F7CD5075035D1A4FA92919E700C064C14": {
      "user_friendly": "UQAbr6t-RI-2e0WwDJBHF7pvfNUHUDXRpPqSkZ5wDAZMFIkl",
      "domain": "unmiy.t.me",
      "interfaces": [
        "wallet_v4r2"
      ]
    },
    "0:307B9A454EBAAFFAC2EA1D05BC3B367E08E036769BB13CCFDDCE234119965CD6": {
      "user_friendly": "EQAwe5pFTrqv-sLqHQW8OzZ-COA2dpuxPM_dziNBGZZc1ixS",
      "domain": null,
      "interfaces": [
        "nft_collection"
      ]
    },
    "0:3C43F2C3740AB71C24BE3E60DB3C30EB8D05F6D36D97E2703DFEF00B854CEC64": {
      "user_friendly": "EQA8Q_LDdAq3HCS-PmDbPDDrjQX2022X4nA9_vALhUzsZP9K",
      "domain": null,
      "interfaces": [
        "nft_sale_getgems_v4"
      ]
    },
    "0:45FD317DB8D76736C6F77CC204E2B75413A22559AD6DB7D8E25ABDE6369A4551": {
      "user_friendly": "UQBF_TF9uNdnNsb3fMIE4rdUE6IlWa1tt9jiWr3mNppFUWcN",
      "domain": null,
      "interfaces": [
        "wallet_v4r2"
      ]
    },
    "0:75DD76F0BD9F1093B310B903FCAE950BA9614CC86F405B64EFB79CE9942D1710": {
      "user_friendly": "EQB13XbwvZ8Qk7MQuQP8rpULqWFMyG9AW2Tvt5zplC0XEJNa",
      "domain": null,
      "interfaces": [
        "nft_item"
      ]
    },
    "0:80D78A35F955A14B679FAA887FF4CD5BFC0F43B4A4EEA2A7E6927F3701B273C2": {
      "user_friendly": "EQCA14o1-VWhS2efqoh_9M1b_A9DtKTuoqfmkn83AbJzwnPi",
      "domain": null,
      "interfaces": [
        "dns"
      ]
    },
    "0:9AB482CD6260254D8000B88D509102C929A7BD276D35CFD3097313A4C9766EAE": {
      "user_friendly": "EQCatILNYmAlTYAAuI1QkQLJKae9J201z9MJcxOkyXZurutf",
      "domain": null,
      "interfaces": [
        "dns"
      ]
    }
  }
}
```
{% endcode %}
