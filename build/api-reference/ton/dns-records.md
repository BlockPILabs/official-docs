# dns records

Query DNS records matching the specified filters. Supports `.ton` and `.t.me` records.

{% hint style="info" %}
Paginate with `limit` / `offset`. Filters combine with AND.
{% endhint %}

**Parameters**

* **`wallet`** — string, optional. Wallet address in any form. Returns DNS records in the wallet category that contain this address.
* **`domain`** — string, optional. Domain name to search for. Returns DNS records with this exact domain name.
* **`limit`** — integer, optional, default `100`. Limit the number of rows to return. Use with `offset` to batch requests.
* **`offset`** — integer, optional, default `0`. Skip the first N rows. Use with `limit` to batch requests.

**Returns**

* `address_book` — object
* `records` — array of objects with fields `dns_next_resolver`, `dns_site_adnl`, `dns_storage_bag_id`, `dns_wallet`, `domain`, `nft_item_address`, `nft_item_owner`

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET 'https://ton.blockpi.network/v1/api/your-api-key/api/v3/dns/records?domain=tonkeeper.ton'

// Result
{
  "records": [
    {
      "nft_item_address": "0:DF98BD937CC40C6644F98F7E04C911E5FB41BB214ED915CBC7FE221636CFD20C",
      "nft_item_owner": "0:8D75B35CDBC66B704DC02860EA2B5F3E3456DC4B385319A44F784AA730826242",
      "domain": "tonkeeper.ton",
      "dns_next_resolver": null,
      "dns_wallet": null,
      "dns_site_adnl": null,
      "dns_storage_bag_id": null,
      "self_assigned": false
    }
  ],
  "address_book": {
    "0:8D75B35CDBC66B704DC02860EA2B5F3E3456DC4B385319A44F784AA730826242": {
      "user_friendly": "UQCNdbNc28ZrcE3AKGDqK18-NFbcSzhTGaRPeEqnMIJiQpS6",
      "domain": null,
      "interfaces": [
        "wallet_v4r2"
      ]
    },
    "0:DF98BD937CC40C6644F98F7E04C911E5FB41BB214ED915CBC7FE221636CFD20C": {
      "user_friendly": "EQDfmL2TfMQMZkT5j34EyRHl-0G7IU7ZFcvH_iIWNs_SDHrs",
      "domain": null,
      "interfaces": [
        "dns"
      ]
    }
  }
}
```
{% endcode %}
