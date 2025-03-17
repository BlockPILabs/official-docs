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
    "block_hash": "0x8304462ff3637bc8da83ee9173945843759780e0b11faaeb27ac88e464d3c0e4",
    "block_timestamp": "1733442582812330",
    "first_version": "1",
    "last_version": "3",
    "transactions": [
        {
            "version": "1",
            "hash": "0x9b923a3d9018d5ea3dd1cbf359d943a3ee52134f9ec30ec0df04593919f622f5",
            "state_change_hash": "0xd258336122e3b692ce6b611d79007b837a207e0758d28e0579d3dc5e4a820789",
            "event_root_hash": "0xebfa8ecfe93e77cb1720370471248221f65f0390e242d894e7d34e26554b9bbc",
            "state_checkpoint_hash": null,
            "gas_used": "0",
            "success": true,
            "vm_status": "Executed successfully",
            "accumulator_root_hash": "0x5930ac1c5cb72b316189f7240d370c24bea0e1064a12e652cc1d35d87c9ea860",
            "changes": [
                {
                    "address": "0x1",
```
````
{% endcode %}
