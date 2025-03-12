---
description: >-
  Retrieves transactions from an account. If the start version is too far in the
  past a 410 will be returned.  If no start version is given, it will start at 0
---

# Get account transactions

#### Path Parameters：

**address** string required

Address of account with or without a `0x` prefix

#### Query Parameters:

**limit** integer

Max number of transactions to retrieve. If not provided, defaults to default page size

**start** string\<uint64>

Ledger version to start list of transactions. If not provided, defaults to showing the latest transactions

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

array

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://aptos.blockpi.network/aptos/v1/your_api_key/v1/accounts/0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2/transactions


// Result
[
    {
        "version": "36173264",
        "hash": "0xe4cc358f3c1184cb1787b41fc52dfcfc25a2609ada71b8aa6fc9b3e4428d9475",
        "state_change_hash": "0x733e205fd66281683722f1a9446aa18a66b67ad7cdb2b01c8f947eda91f20b16",
        "event_root_hash": "0x8aa679c968e4450352db938fad90be53fb8fc3b18c97cebc39b396bea173ae22",
        "state_checkpoint_hash": null,
        "gas_used": "994",
        "success": true,
        "vm_status": "Executed successfully",
        "accumulator_root_hash": "0x87aa62641c889446f6c20673354eefd2a568e6730f5e19fe12ad12fc33ac0e32",
        "changes": [
            {
                "address": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
                "state_key_hash": "0xb59d2fe490a2aaa6aa8907958508e7e9aab8a6ca0371466b0d58beabe9cdc15a",
                "data": {
                    "type": "0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>",
                    "data": {
                        "coin": {
                            "value": "600"
                        },
                        "deposit_events": {
                            "counter": "1",
                            "guid": {
                                "id": {
                                    "addr": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
                                    "creation_num": "2"
                                }
                            }
                        },
                        "frozen": false,
                        "withdraw_events": {
                            "counter": "0",
                            "guid": {
                                "id": {
                                    "addr": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
                                    "creation_num": "3"
                                }
                            }
                        }
                    }
                },
                "type": "write_resource"
            },
            {
                "address": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
                "state_key_hash": "0x27900227132855a653e08f2e0d992df3362b0c099b58ce8992c1d9bf744e0984",
                "data": {
                    "type": "0x1::coin::CoinStore<0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6::opc::OPC>",
                    "data": {
                        "coin": {
                            "value": "0"
                        },
                        "deposit_events": {
                            "counter": "0",
                            "guid": {
                                "id": {
                                    "addr": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
                                    "creation_num": "4"
                                }
                            }
                        },
                        "frozen": false,
                        "withdraw_events": {
                            "counter": "0",
                            "guid": {
                                "id": {
                                    "addr": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
                                    "creation_num": "5"
                                }
                            }
                        }
                    }
                },
                "type": "write_resource"
            },
            {
                "address": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
                "state_key_hash": "0x1a41b2d0196e13823ddf1eccc83624522dee831a483250394b838c57cb148fe5",
                "data": {
                    "type": "0x1::account::Account",
                    "data": {
                        "authentication_key": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
                        "coin_register_events": {
                            "counter": "2",
                            "guid": {
                                "id": {
                                    "addr": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
                                    "creation_num": "0"
                                }
                            }
                        },
                        "guid_creation_num": "6",
                        "key_rotation_events": {
                            "counter": "0",
                            "guid": {
                                "id": {
                                    "addr": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
                                    "creation_num": "1"
                                }
                            }
                        },
                        "rotation_capability_offer": {
                            "for": {
                                "vec": []
                            }
                        },
                        "sequence_number": "1",
                        "signer_capability_offer": {
                            "for": {
                                "vec": []
                            }
                        }
                    }
                },
                "type": "write_resource"
            },
            {
                "state_key_hash": "0x6e4b28d40f98a106a65163530924c0dcb40c1349d3aa915d108b4d6cfc1ddb19",
                "handle": "0x1b854694ae746cdbd8d44186ca4929b2b337df21d1c74633be19b2710552fdca",
                "key": "0x0619dc29a0aac8fa146714058e8dd6d2d0f3bdf5f6331907bf91f3acd81e6935",
                "value": "0xf64ca977878065010000000000000000",
                "data": null,
                "type": "write_table_item"
            }
        ],
        "sender": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2",
        "sequence_number": "0",
        "max_gas_amount": "1000",
        "gas_unit_price": "100",
        "expiration_timestamp_secs": "1669084567",
        "payload": {
            "function": "0x6de517a18f003625e7fba9b9dc29b310f2e3026bbeb1997b3ada9de1e3cec8d6::opc::register",
            "type_arguments": [],
            "arguments": [],
            "type": "entry_function_payload"
        },
        "signature": {
            "public_key": "0x67bb99480a4b9aa7f83ba56570a6fe939b5a80286b1456cb0e52972f3af44698",
            "signature": "0x2b47a221992fba90f8a11efef9a1b6cd82c9a3a17cf684fb80419ba5deada52dc52e77d8b01c780141126ac319df4256db7521ed0cf1930a347e70de04f8cd0a",
            "type": "ed25519_signature"
        },
        "events": [
            {
                "guid": {
                    "creation_number": "0",
                    "account_address": "0x9e5cf6e900fecbb716eb64781d40a5b1db9652caa6b61c188184b28c41687db2"
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
        ],
        "timestamp": "1669084548326324",
        "type": "user_transaction"
    }
]
```
{% endcode %}
