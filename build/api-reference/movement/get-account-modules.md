---
description: >-
  Retrieves all account modules' bytecode for a given account at a specific
  ledger version.
---

# Get account modules

The Aptos nodes prune account state history, via a configurable time window. If the requested ledger version has been pruned, the server responds with a 410.

#### **Path Parameters:**

**address**  string \<hex> required

Address of account with or without a `0x` prefix

#### Query Parameters：

**ledger\_version** string\<uint64>

Ledger version to get state of account. If not provided, it will be the latest version

**limit integer**

Max number of account resources to retrieve. If not provided, defaults to default page size

**start string**

Cursor specifying where to start for pagination. This cursor cannot be derived manually client-side. Instead, you must call this endpoint once without this query parameter specified, and then use the cursor returned in the X-Aptos-Cursor header in the response.

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

**array of:**

**bytecode** string\<hex>&#x20;

All bytes (Vec) data is represented as hex-encoded string prefixed with `0x` and fulfilled with two hex digits per byte.

**abi** object

A Move module

&#x20;   **address** string\<hex>

&#x20;   A hex encoded 32 byte Aptos account address.

&#x20;   **name** string&#x20;

&#x20;   **friends** array\[string]

&#x20;   Friends of the module

&#x20;   **exposed\_functions** array\[object]

&#x20;   Public functions of the module

&#x20;   **structs** array\[object]

&#x20;   Structs of the module

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/accounts/0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6/modules

// Result
[
    {
        "bytecode": "",
        "abi": {
            "address": "",
            "name": "",
            "friends": [],
            "exposed_functions": [
                {
                    "name": "",
                    "visibility": "",
                    "is_entry": false,
                    "generic_type_params": [],
                    "params": [
                        ""
                    ],
                    "return": [
                        ""
                    ]
                },
                {
                    "name": "",
                    "visibility": "",
                    "is_entry": true,
                    "generic_type_params": [],
                    "params": [
                        "",
                        ""
                    ],
                    "return": []
                },
                ......
```
{% endcode %}
