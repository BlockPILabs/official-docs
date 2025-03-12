---
description: >-
  Get a table item at a specific ledger version from the table identified by
  {table_handle} in the path and the "key" (TableItemRequest) provided in the
  request body.
---

# Get table item

If the duration\_secs param is provided, this endpoint will return a 200 if the following condition is true:

`server_latest_ledger_info_timestamp >= server_current_time_timestamp - duration_secs`

#### **Path Parameters:**

**table\_handle** string required

Table handle hex encoded 32-byte string

#### Query Parameters：

**ledger\_version** string\<uint64>

Ledger version to get state of account. If not provided, it will be the latest version

#### Request Body

Table Item request for the GetTableItem API

**key\_type** string&#x20;

String representation of an on-chain Move type tag that is exposed in transaction payload. Values: - bool - u8 - u64 - u128 - address - signer - vector: `vector<{non-reference MoveTypeId}>` - struct: `{address}::{module_name}::{struct_name}::<{generic types}>`

**value\_type** string

String representation of an on-chain Move type tag that is exposed in transaction payload. Values: - bool - u8 - u64 - u128 - address - signer - vector: `vector<{non-reference MoveTypeId}>` - struct: `{address}::{module_name}::{struct_name}::<{generic types}>`

**key**&#x20;

The value of the table item's key

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

**object**

An enum of the possible Move value types

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/tables/tables/0x1b854694ae746cdbd8d44186ca4929b2b337df21d1c74633be19b2710552fdca/item
--data
{
  "key_type": "address",
  "value_type": "u128",
  "key": "0x0619dc29a0aac8fa146714058e8dd6d2d0f3bdf5f6331907bf91f3acd81e6935"
}

// Result
{
    
}
```
{% endcode %}
