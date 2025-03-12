---
description: >-
  Retrieves all account resources for a given account and a specific ledger
  version.
---

# Get account resources

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

**type** string

String representation of a MoveStructTag (on-chain Move struct type). This exists so you can specify MoveStructTags as path/query parameters, e.g. for get\_events\_by\_event\_handle.

**data** object

This is a JSON representation of some data within an account resource. More specifically, it is a map of strings to arbitrary JSON values/objects, where the keys are top level fields within the given resource.

To clarify, you might query for 0x1::account::Account and see the example data.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/accounts/0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6/resources

// Result
[
    {
        "type": "",
        "data": {
            "packages": [
                {
                    "deps": [
                        {
                            "account": "",
                            "package_name": ""
                        },
                        {
                            "account": "",
                            "package_name": ""
                        },
                        {
                            "account": "",
                            "package_name": ""
                        }
                    ],
                    "extension": {
                        "vec": []
                    },
                    "manifest": "",
                    "modules": [
                        {
                            "extension": {
                                "vec": []
                            },
                            "name": "opc",
                            "source": "0x",
                            "source_map": "0x"
                        }
                    ],
                    "name": "",
                    "source_digest": "",
                    "upgrade_number": "",
                    "upgrade_policy": {
                        "policy": 1
                    }
                }
            ]
        }
    },
   ......
```
{% endcode %}
