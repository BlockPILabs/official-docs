---
description: >-
  This endpoint allows you to get the transactions in a block and the
  corresponding block information given a version in the block.
---

# Get blocks by version

Transactions are limited by max default transactions size. If not all transactions are present, the user will need to query for the rest of the transactions via the get transactions API.

If the block is pruned, it will return a 410.

#### **Path Parameters:**

**version** integer required

Ledger version to lookup block information for

#### Query Parameters：

**with\_transactions** boolean

If set to true, include all transactions in the block. If not provided, no transactions will be retrieved

#### **Response Header:**

**X-APTOS-BLOCK-HEIGHT** integer&#x20;

Current block height of the chain

**X-APTOS-CHAIN-ID** integer&#x20;

Chain ID of the current chain

**X-APTOS-EPOCH** integer&#x20;

Current epoch of the chain

**X-APTOS-LEDGER-OLDEST-VERSION** integer&#x20;

Oldest non-pruned ledger version of the chain

**X-APTOS-LEDGER-TIMESTAMPUSEC** integer&#x20;

Current timestamp of the chain

**X-APTOS-LEDGER-VERSION** integer&#x20;

Current ledger version of the chain

**X-APTOS-OLDEST-BLOCK-HEIGHT** integer&#x20;

Oldest non-pruned block height of the chain

#### **Response Body:**

A Block with or without transactions

**block\_height** string\<uint64>

A string containing a 64-bit unsigned integer.

**block\_hash** string&#x20;

**block\_timestamp** string\<uint64>

A string containing a 64-bit unsigned integer.

**first\_version** string\<uint64>

A string containing a 64-bit unsigned integer.

**last\_version** string\<uint64>

A string containing a 64-bit unsigned integer.

**transactions** array&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/accounts/blocks/by_version/1

// Result
{
    "block_height": "11631405",
    "block_hash": "0xee76aa9f24a008390e98d73739adaa311f1ad05b8d75ad0a6b1213dcc5ceebbc",
    "block_timestamp": "1669084548326324",
    "first_version": "36173262",
    "last_version": "36173265",
    "transactions": [<array of transactions>]
}
```
{% endcode %}
