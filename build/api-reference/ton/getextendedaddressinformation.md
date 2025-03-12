# /getExtendedAddressInformation

Similar to previous one but tries to parse additional information for known contract types. This method is based on tonlib's function _getAccountState_. For detecting wallets we recommend to use _getWalletInformation_.

**Parameters**

**address - string,** Identifier of target TON account in any form.

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getExtendedAddressInformation?address=UQD6FHZ8Bm5K82FcRVV76SOAzB52VqOlWpgeNODQkJ9AVxtU' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": {
    "@type": "fullAccountState",
    "address": {
      "@type": "accountAddress",
      "account_address": "UQD6FHZ8Bm5K82FcRVV76SOAzB52VqOlWpgeNODQkJ9AVxtU"
    },
    "balance": "14020735",
    "last_transaction_id": {
      "@type": "internal.transactionId",
      "lt": "48756545000001",
      "hash": "JseckUUQ5BOUW3fAmggsXknXxQGwtoVwuo1/qTuDRDo="
    },
    "block_id": {
      "@type": "ton.blockIdExt",
      "workchain": -1,
      "shard": "-9223372036854775808",
      "seqno": 39984042,
      "root_hash": "t4MsIVXi7xpR0jUk6NSSwqp3lIZjAwQp09ao7Kc8n0U=",
      "file_hash": "LkzbZ94NSNwdFH8HWEb5Dyaiv1+rEA2JskjkfR+u1KA="
    },
    "sync_utime": 1724742773,
    "account_state": {
      "@type": "wallet.v4.accountState",
      "wallet_id": "698983191",
      "seqno": 2
    },
    "revision": 2,
    "@extra": "1724742851.074307:8:0.7692532966881773"
  }
}
```
{% endcode %}
