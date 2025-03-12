# /getTransactions

Get transaction history of a given address.



**Parameters:**

**address - string,** Identifier of target TON account in any form.

#### Example:

{% code overflow="wrap" %}
```json
// Request
url -X 'GET' \
  'https://ton.blockpi.network/v1/rpc/your-rpc-key/getTransactions?address=UQD6FHZ8Bm5K82FcRVV76SOAzB52VqOlWpgeNODQkJ9AVxtU' \
  -H 'accept: application/json'

// Result
{
  "ok": true,
  "result": [
    {
      "@type": "raw.transaction",
      "address": {
        "@type": "accountAddress",
        "account_address": "EQD6FHZ8Bm5K82FcRVV76SOAzB52VqOlWpgeNODQkJ9AV0aR"
      },
      "utime": 1724739952,
      "data": "te6cckECFQEABKUAA7V/oUdnwGbkrzYVxFVXvpI4DMHnZWo6VamB404NCQn0BXAAAsWASLkkGxf5Jp9Lp3AtRc/KY7eZb8NUu9SXvDHGasbpWOjU0nIQAALFOfoHIBZs1xcAAHRonx9IAQIDAgHgBAUAgnJoi4mJnDEreuyZKgoYvn20vBZ7v6k1IwhXSvWt8ETm5zMm5gNalOH9b/Iw8tykf35/B7lnwyd/O9sqBnrHGr3wAhEMlYxGGOA4BEATFAPliAH0KOz4DNyV5sK4iqr30kcBmDzsrUdKtTA8acGhIT6ArgUSHOC8UZfVsDI9j79Uz0TnHNLylVbmr8tCXfBN5G00bKao9ww787cpLO5OXvtYywBcHAJT8OtunxO2tQ6vgRBRTU0YuzZrkjgAAAAIABgYHAYHCAIB2wkKAWRiAAMcxc17ZNBdCHaB0gSWMAvswAqO4wEPBUPi3O63c0AXkB9AAAAAAAAAAAAAAAAAAQ4BZGIAf3hsi78kWE2mqV/GBn0wMLhyM4t4fEPhLQ1hxlsw+52QH0AAAAAAAAAAAAAAAAABEACwQgB3TrUMUxs1/+zxONDRNNy6GZq5kYxLaNKWGe13wgGh9qJH7wH4AAAAAAAAAAAAAAAAAAAAAABOb3Rjb2luIEFpcmRyb3AgVmVyaWYuIFJlZjogIzgzNwIBIAsMAQFIEgEBIA0BASAPAa1oAfQo7PgM3JXmwriKqvfSRwGYPOytR0q1MDxpwaEhPoCvAAGOYua9smguhDtA6QJLGAX2YAVHcYCHgqHxbndbuaALyA+gBhIqCgAAWLAJFySEzZri4MAOAa4Pin6lAAAAAAAAAABlrzEHpAAIAfQo7PgM3JXmwriKqvfSRwGYPOytR0q1MDxpwaEhPoCvAD6FHZ8Bm5K82FcRVV76SOAzB52VqOlWpgeNODQkJ9AVwhURAa1oAfQo7PgM3JXmwriKqvfSRwGYPOytR0q1MDxpwaEhPoCvAD+8NkXfkiwm01Sv4wM+mBhcORnFvD4h8JaGsOMtmH3OyA+gBhIqCgAAWLAJFySGzZri4MAQAa4Pin6lAAAAAAAAAABuNfqTGgAIAfQo7PgM3JXmwriKqvfSRwGYPOytR0q1MDxpwaEhPoCvAD6FHZ8Bm5K82FcRVV76SOAzB52VqOlWpgeNODQkJ9AVwhURAFQAAAAA4pqg77iPIFJlY2VpdmUgb25seSBhZnRlciBjb25maXJtYXRpb24A+UgB9Cjs+AzclebCuIqq99JHAZg87K1HSrUwPGnBoSE+gK8AO6dahimNmv/2eJxoaJpuXQzNXMjGJbRpSwz2u+EA0PtRI/eA/AYII1oAAFiwCRckiM2a4uAAAAAAJze6Mbe0txAgtLkyOTe4ECsyuTSzFxApMrMdEBGcGZvAAJ1CPgMTiAAAAAAAAAAAFQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAG/JkKzATCx3JAAAAAAABgAAAAAABzQaOQJbpgJ+TSOwSPHC1Ubn4qL9lUJjp5ZziXhwQ3r8QdCKnCT7qNI=",
      "transaction_id": {
        "@type": "internal.transactionId",
        "lt": "48756545000001",
        "hash": "JseckUUQ5BOUW3fAmggsXknXxQGwtoVwuo1/qTuDRDo="
      },
      ......
```
{% endcode %}
