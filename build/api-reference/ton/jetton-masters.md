# jetton masters

Query jetton masters that match the specified filters.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`address`** — array of strings, optional. Jetton master address in any form. Maximum: 1024 addresses.
* **`admin_address`** — array of strings, optional. Address of the jetton master's administrator in any form. Maximum: 1024 addresses.
* **`limit`** — integer, optional, default `10`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.

**Returns**

* `address_book` — object
* `jetton_masters` — array of objects with fields `address`, `admin_address`, `code_hash`, `data_hash`, `jetton_content`, `jetton_wallet_code_hash`, `last_transaction_lt`, `mintable`, `total_supply`
* `metadata` — object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/jetton/masters?limit=2'

// Result
{
  "jetton_masters": [
    {
      "address": "-1:A6FDDC65A0DC39BECD63FB75987D47B6991B168886729B0F7285340C409087FC",
      "total_supply": "20000000000000000000",
      "mintable": true,
      "admin_address": "0:0000000000000000000000000000000000000000000000000000000000000000",
      "jetton_content": {
        "uri": "https://magenta-fast-starfish-986.mypinata.cloud/ipfs/bafkreihw2t76dhpiahzaiwa2cdm4nf3aljh3qxpebrlb5w7acdey7xjfd4"
      },
      "jetton_wallet_code_hash": "vrBoPr64kn/p/I7AoYvH3ReJlomCWhIeq0bFo6hg0M4=",
      "code_hash": "mg+Y3W+/Il7vgWXk5kQX7pMffuoABlNDnntdzcBkTNY=",
      "data_hash": "jmgZpaZDHEvCp3YG5yZE42LK5fq+AIRsciK0/UItQsI=",
      "last_transaction_lt": "57317035000001"
    }
  ],
  "address_book": {
    "-1:4F04B71CC27A9B5E5180478FA1DE0B3A450D39D51C4553418465800FEC15831D": {
      "user_friendly": "Uf9PBLccwnqbXlGAR4-h3gs6RQ051RxFU0GEZYAP7BWDHYQD",
      "domain": null,
      "interfaces": [
        "wallet_v4r2"
      ]
    },
    "-1:A6FDDC65A0DC39BECD63FB75987D47B6991B168886729B0F7285340C409087FC": {
      "user_friendly": "Ef-m_dxloNw5vs1j-3WYfUe2mRsWiIZymw9yhTQMQJCH_AAA",
      "domain": null,
      "interfaces": [
        "jetton_master"
      ]
    },
    "-1:AAB395C13B81F2AE700A860AA2F44F8C47E82CD130E81B92376A45002D19F002": {
      "user_friendly": "Ef-qs5XBO4HyrnAKhgqi9E-MR-gs0TDoG5I3akUALRnwArP8",
      "domain": null,
      "interfaces": [
        "jetton_master"
      ]
    },
    "0:0000000000000000000000000000000000000000000000000000000000000000": {
      "user_friendly": "UQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJKZ",
      "domain": null,
      "interfaces": []
    }
  },
  "metadata": {
    "-1:A6FDDC65A0DC39BECD63FB75987D47B6991B168886729B0F7285340C409087FC": {
      "is_indexed": true,
      "token_info": [
        {
          "valid": true,
          "type": "jetton_masters",
          "name": "Ttt",
          "symbol": "TT",
          "description": "TT ttt.",
          "image": "https://bitcoincash-example.github.io/website/logo.png",
          "is_nsfw": false,
          "is_scam": false,
          "extra": {
            "_image_big": "https://proxy.toncenter.com/dls_1J6JXvJtaKL_wT-VnS-jK-p_qKQLF4DjOaXx03c/pr:big/bG9jYWw6Ly8vZTMvMDkvZTMwOTE5YTA3N2ExNDlmN…",
            "_image_medium": "https://proxy.toncenter.com/w8Ud_qGWd6i-hfHkwfaF401Bnf82oZMIaTytuxXt0kA/pr:medium/bG9jYWw6Ly8vZTMvMDkvZTMwOTE5YTA3N2ExND…",
            "_image_small": "https://proxy.toncenter.com/9aq22EZ6Zgru7SQ-lFLnCJ3e4G6_fkFdyxBtt4InwvQ/pr:small/bG9jYWw6Ly8vZTMvMDkvZTMwOTE5YTA3N2ExNDl…",
            "decimals": "9",
            "uri": "https://magenta-fast-starfish-986.mypinata.cloud/ipfs/bafkreihw2t76dhpiahzaiwa2cdm4nf3aljh3qxpebrlb5w7acdey7xjfd4"
          }
        }
      ]
    },
    "-1:AAB395C13B81F2AE700A860AA2F44F8C47E82CD130E81B92376A45002D19F002": {
      "is_indexed": true,
      "token_info": [
        {
          "valid": false,
          "type": "jetton_masters"
        }
      ]
    }
  }
}
```
{% endcode %}
