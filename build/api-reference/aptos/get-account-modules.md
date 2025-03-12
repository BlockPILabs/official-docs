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
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/accounts/0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6/modules

// Result
[
    {
        "bytecode": "0xa11ceb0b050000000b01000c020c0a03167304890114059d013107ce01eb0108b9034006f90324109d045e0afb04050c80058f0100000101010201030104010500060000041507010000000700010000080203000009000300000a040500000b060300000c000300000d030700000e060300000f0603000511000400021204010100030802030100031309030100021404050100030b06030100020c000301000216030a010004170b05010004180b0c0100020e06030100010e0603000a080b080c080d080e080f08100811071207130801060c010302060c03000105010103060c0503010401080005060c0a020a020201010b01010401060b0101090001060900036f70630d6170746f735f6163636f756e7404636f696e0c6d616e616765645f636f696e066f7074696f6e067369676e6572034f50430962616c616e63654f66046275726e0b696e69745f6d6f64756c650d69735f72656769737465726564046d696e740872656769737465720b746f74616c537570706c79087472616e736665720b7472616e736665724150540b64756d6d795f6669656c640a616464726573735f6f660762616c616e63650a696e697469616c697a651569735f6163636f756e745f72656769737465726564064f7074696f6e06737570706c790769735f736f6d6506626f72726f776de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d60000000000000000000000000000000000000000000000000000000000000001030801000000000000000a02100f4f6365616e205061726b20436f696e0a0204034f5043126170746f733a3a6d657461646174615f76304a01010000000000000010454e4f5f4341504142494c49544945532f4163636f756e7420686173206e6f206361706162696c697469657320286275726e2f6d696e742f667265657a65292e00020110010001000003040b0011093800020101040003040b000b013801020200000003070b00070107023106083802020301000003030b003803020401040003050b000b010b023804020501040003030b00380502060100000a0b38060c000e0038070307060100000000000000270e00380814020701040003050b000b010b023809020801040003050b000b010b0211140200",
        "abi": {
            "address": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6",
            "name": "opc",
            "friends": [],
            "exposed_functions": [
                {
                    "name": "balanceOf",
                    "visibility": "public",
                    "is_entry": false,
                    "generic_type_params": [],
                    "params": [
                        "&signer"
                    ],
                    "return": [
                        "u64"
                    ]
                },
                {
                    "name": "burn",
                    "visibility": "public",
                    "is_entry": true,
                    "generic_type_params": [],
                    "params": [
                        "&signer",
                        "u64"
                    ],
                    "return": []
                },
                {
                    "name": "is_registered",
                    "visibility": "public",
                    "is_entry": false,
                    "generic_type_params": [],
                    "params": [
                        "address"
                    ],
                    "return": [
                        "bool"
                    ]
                },
                {
                    "name": "mint",
                    "visibility": "public",
                    "is_entry": true,
                    "generic_type_params": [],
                    "params": [
                        "&signer",
                        "address",
                        "u64"
                    ],
                    "return": []
                },
                {
                    "name": "register",
                    "visibility": "public",
                    "is_entry": true,
                    "generic_type_params": [],
                    "params": [
                        "&signer"
                    ],
                    "return": []
                },
                {
                    "name": "totalSupply",
                    "visibility": "public",
                    "is_entry": false,
                    "generic_type_params": [],
                    "params": [],
                    "return": [
                        "u128"
                    ]
                },
                {
                    "name": "transfer",
                    "visibility": "public",
                    "is_entry": true,
                    "generic_type_params": [],
                    "params": [
                        "&signer",
                        "address",
                        "u64"
                    ],
                    "return": []
                },
                {
                    "name": "transferAPT",
                    "visibility": "public",
                    "is_entry": true,
                    "generic_type_params": [],
                    "params": [
                        "&signer",
                        "address",
                        "u64"
                    ],
                    "return": []
                }
            ],
            "structs": [
                {
                    "name": "OPC",
                    "is_native": false,
                    "abilities": [],
                    "generic_type_params": [],
                    "fields": [
                        {
                            "name": "dummy_field",
                            "type": "bool"
                        }
                    ]
                }
            ]
        }
    }
]
```
{% endcode %}
