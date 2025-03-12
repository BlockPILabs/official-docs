# Get events by event handle

This API uses the given account `address`, `eventHandle`, and `fieldName` to build a key that can globally identify an event types. It then uses this key to return events emitted to the given account matching that event type.

#### **Path Parameters:**

**address** string required

Hex-encoded 32 byte Aptos account, with or without a `0x` prefix, for which events are queried. This refers to the account that events were emitted to, not the account hosting the move module that emits that event type.

**event\_handle** string\<uint64> required

Name of struct to lookup event handle e.g. `0x1::account::Account`

**field\_name** string required

Name of field to lookup event handle e.g. `withdraw_events`

#### Query Parameters：

**limit** integer

Max number of events to retrieve. If unspecified, defaults to default page size.

**start** string\<uint64>

Starting sequence number of events. If unspecified, by default will retrieve the most recent events

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

array of:

**version** string\<uint64>

A string containing a 64-bit unsigned integer.

**guid** object&#x20;

&#x20;   **creation\_number** string\<uint64>

&#x20;   A string containing a 64-bit unsigned integer.Show all...

&#x20;   **account\_address** string\<hex>

&#x20;   A hex encoded 32 byte Aptos account address.Show all...

**sequence\_number** string\<uint64>

A string containing a 64-bit unsigned integer.

**type** string

String representation of an on-chain Move type tag that is exposed in transaction payload. Values: - bool - u8 - u64 - u128 - address - signer - vector: `vector<{non-reference MoveTypeId}>` - struct: `{address}::{module_name}::{struct_name}::<{generic types}>`...

**data**

The JSON representation of the event

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/accounts/0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6/events//0x1%3A%3Acoin%3A%3ACoinStore%3C0x1%3A%3Amovement_coin%3A%3AMovementCoin%3E/withdraw_events

// Result
[

]
```
{% endcode %}
