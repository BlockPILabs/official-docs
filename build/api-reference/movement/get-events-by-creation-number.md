# Get events by creation number

Event types are globally identifiable by an account `address` and monotonically increasing `creation_number`, one per event type emitted to the given account. This API returns events corresponding to that that event type.

#### **Path Parameters:**

**address** string required

Hex-encoded 32 byte Aptos account, with or without a `0x` prefix, for which events are queried. This refers to the account that events were emitted to, not the account hosting the move module that emits that event type.

**creation\_number** string\<uint64> required

Creation number corresponding to the event stream originating from the given account.

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
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/accounts/0xdb42353b3f77383dce21d9c55a9f6a51149b2a45d1f376def4d2ea43d1b7e399/events/0

// Result
[
    
]
```
{% endcode %}
