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
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/accounts/0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6/resources

// Result
[
    {
        "type": "0x1::code::PackageRegistry",
        "data": {
            "packages": [
                {
                    "deps": [
                        {
                            "account": "0x1",
                            "package_name": "AptosFramework"
                        },
                        {
                            "account": "0x1",
                            "package_name": "AptosStdlib"
                        },
                        {
                            "account": "0x1",
                            "package_name": "MoveStdlib"
                        }
                    ],
                    "extension": {
                        "vec": []
                    },
                    "manifest": "0x1f8b08000000000002ff3d4e4d6bc3300cbdfb5784dc97da314deac30e63b0eb762f65c892524c13cbd85db731f6df1b435bd0417a4fef639f004f70e4838ab070f3dcb4ef1faf1262ab2e9c4b905821d3e94eb7ea2b1d33107f269903fe56026549700e7ee656a93d10652e85cb4149c2caeb9f81786b4630bb496b3bf45b1e270fce3bc2de796bf4d4b3d5fde03d7be3dce82d103862c316197734545fe2c4913862a8d62fe92ce52daf6dbf259fd694bf661684b9e675dd661da81f4f28996feb2217de4c77c90d7cdc6df3afaefe587b6d07010000",
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
                    "name": "OPCoin",
                    "source_digest": "3F53E41C4FD27343491C4D308FBFA64902B48C1817221724DA72BBA9B622292C",
                    "upgrade_number": "0",
                    "upgrade_policy": {
                        "policy": 1
                    }
                }
            ]
        }
    },
    {
        "type": "0x1::coin::CoinInfo<0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6::opc::OPC>",
        "data": {
            "decimals": 6,
            "name": "Ocean Park Coin",
            "supply": {
                "vec": [
                    {
                        "aggregator": {
                            "vec": []
                        },
                        "integer": {
                            "vec": [
                                {
                                    "limit": "340282366920938463463374607431768211455",
                                    "value": "318775339200000"
                                }
                            ]
                        }
                    }
                ]
            },
            "symbol": "OPC"
        }
    },
    {
        "type": "0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>",
        "data": {
            "coin": {
                "value": "2720669100"
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
                "counter": "13663",
                "guid": {
                    "id": {
                        "addr": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6",
                        "creation_num": "3"
                    }
                }
            }
        }
    },
    {
        "type": "0x1::coin::CoinStore<0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6::opc::OPC>",
        "data": {
            "coin": {
                "value": "17887445100000"
            },
            "deposit_events": {
                "counter": "7",
                "guid": {
                    "id": {
                        "addr": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6",
                        "creation_num": "4"
                    }
                }
            },
            "frozen": false,
            "withdraw_events": {
                "counter": "31090",
                "guid": {
                    "id": {
                        "addr": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6",
                        "creation_num": "5"
                    }
                }
            }
        }
    },
    {
        "type": "0x1::account::Account",
        "data": {
            "authentication_key": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6",
            "coin_register_events": {
                "counter": "2",
                "guid": {
                    "id": {
                        "addr": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6",
                        "creation_num": "0"
                    }
                }
            },
            "guid_creation_num": "6",
            "key_rotation_events": {
                "counter": "0",
                "guid": {
                    "id": {
                        "addr": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6",
                        "creation_num": "1"
                    }
                }
            },
            "rotation_capability_offer": {
                "for": {
                    "vec": []
                }
            },
            "sequence_number": "45399",
            "signer_capability_offer": {
                "for": {
                    "vec": []
                }
            }
        }
    },
    {
        "type": "0x1::managed_coin::Capabilities<0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6::opc::OPC>",
        "data": {
            "burn_cap": {
                "dummy_field": false
            },
            "freeze_cap": {
                "dummy_field": false
            },
            "mint_cap": {
                "dummy_field": false
            }
        }
    }
]
```
{% endcode %}
