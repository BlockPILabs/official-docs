---
description: >-
  This endpoint allows you to get the transactions in a block and the
  corresponding block information.
---

# Get blocks by height

Transactions are limited by max default transactions size. If not all transactions are present, the user will need to query for the rest of the transactions via the get transactions API.

If the block is pruned, it will return a 410.

#### **Path Parameters:**

**block\_height** integer required

Block height to lookup. Starts at 0

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

**transactions** array

#### Example:

{% code overflow="wrap" %}
````json
// Request
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/blocks/by_height/1?with_transactions=true

// Result
{
    "block_height": "1",
    "block_hash": "0xae57c688b78602035ff36d54f9cd72bb2c8e64129705e6c70d8fa942a1cc0a3f",
    "block_timestamp": "1732636311639215",
    "first_version": "1",
    "last_version": "3",
    "transactions": [
        {
            "version": "1",
            "hash": "0xc1a8d79713f5a6698a1ccd67697b768f51c1b6cfb7403f0e8a5518b0759aba5b",
            "state_change_hash": "0x8b1a2959bd38488aa965f258126e606a50accd86430a4d9bcd898124d8978a3c",
            "event_root_hash": "0x9ba1dcda40a58fe8895821afc58728ca01ba9f643812a18313e0d31b2ca01a80",
            "state_checkpoint_hash": null,
            "gas_used": "0",
            "success": true,
            "vm_status": "Executed successfully",
            "accumulator_root_hash": "0xb1ee85b938b66326a88a35a671d2b641739c5120efcc369dd51aa77b8ce82115",
            "changes": [
```
````
{% endcode %}
