---
description: >-
  Retrieves an individual resource from a given account and at a specific ledger
  version.
---

# Get account resource

The Aptos nodes prune account state history, via a configurable time window. If the requested ledger version has been pruned, the server responds with a 410.

#### **Path Parameters:**

**address**  string \<hex> required

Address of account with or without a `0x` prefix

**resource\_type** string

Name of struct to retrieve e.g. `0x1::account::Account`

#### Query Parameters：

**ledger\_version** string\<uint64>

Ledger version to get state of account. If not provided, it will be the latest version

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

A parsed Move resource

**type** string

String representation of a MoveStructTag (on-chain Move struct type). This exists so you can specify MoveStructTags as path/query parameters, e.g. for get\_events\_by\_event\_handle.

**data** object

This is a JSON representation of some data within an account resource. More specifically, it is a map of strings to arbitrary JSON values/objects, where the keys are top level fields within the given resource.

To clarify, you might query for 0x1::account::Account and see the example data.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/accounts/0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>

// Result
{
    "type": "0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>",
    "data": {
        "coin": {
            "value": "2708570300"
        },
        "deposit_events": {
            "counter": "5",
            "guid": {
                "id": {
                    "addr": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6",
                    "creation_num": "2"
                }
            }
        },
        "frozen": false,
        "withdraw_events": {
            "counter": "13691",
            "guid": {
                "id": {
                    "addr": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6",
                    "creation_num": "3"
                }
            }
        }
    }
}
```
{% endcode %}
