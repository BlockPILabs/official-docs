# /getWalletInformation

Retrieve wallet information. This method parses contract state and currently supports more wallet types than getExtendedAddressInformation: simple wallet, standart wallet, v3 wallet, v4 wallet.

**Parameters**

**address - string,** Identifier of target TON account in any form.

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getWalletInformation?address=UQD6FHZ8Bm5K82FcRVV76SOAzB52VqOlWpgeNODQkJ9AVxtU' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "wallet": true,
    "balance": "14020735",
    "account_state": "active",
    "wallet_type": "wallet v4 r2",
    "seqno": 2,
    "last_transaction_id": {
      "@type": "internal.transactionId",
      "lt": "48756545000001",
      "hash": "JseckUUQ5BOUW3fAmggsXknXxQGwtoVwuo1/qTuDRDo="
    },
    "wallet_id": 698983191
  }
}
```
{% endcode %}
