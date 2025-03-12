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
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/accounts/0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6/events/0

// Result
[
    {
        "version": "26258912",
        "guid": {
            "creation_number": "0",
            "account_address": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6"
        },
        "sequence_number": "0",
        "type": "0x1::account::CoinRegisterEvent",
        "data": {
            "type_info": {
                "account_address": "0x1",
                "module_name": "0x6170746f735f636f696e",
                "struct_name": "0x4170746f73436f696e"
            }
        }
    },
    {
        "version": "26288123",
        "guid": {
            "creation_number": "0",
            "account_address": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6"
        },
        "sequence_number": "1",
        "type": "0x1::account::CoinRegisterEvent",
        "data": {
            "type_info": {
                "account_address": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6",
                "module_name": "0x6f7063",
                "struct_name": "0x4f5043"
            }
        }
    }
]
```
{% endcode %}
