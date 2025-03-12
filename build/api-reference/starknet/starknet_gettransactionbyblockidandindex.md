---
description: >-
  Get the details of the transaction given by the identified block and index in
  that block. If no transaction is found, null is returned.
---

# starknet\_getTransactionByBlockIdAndIndex

#### **Parameters:**

**BLOCK\_PARAM**  -  Expected one of `block_number`, `block_hash`, `latest`, `pending`

**TRANSACTION\_INDEX**  -  he index in the block to search for the transaction

#### **Returns:**

A transaction object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_getTransactionByBlockIdAndIndex","params": ["latest", 1],"id":1}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
        "calldata": [
            "0x1",
            "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
            "0x83afd3f4caedc6eebf44246fe54e38c95e3179a5ec9ea81740eca5b482d12e",
            "0x0",
            "0x3",
            "0x3",
            "0x66f9b127e01714d77cc3eb94d9bc2bb50c1f290fbfeab40b2998a71278bdf7a",
            "0x190bf009aaa000",
            "0x0"
        ],
        "max_fee": "0x258d5be746a000",
        "nonce": "0x11aef6",
        "sender_address": "0x3a20d4f7b4229e7c4863dab158b4d076d7f454b893d90a62011882dc4caca2a",
        "signature": [
            "0x790c2fea2fce9a73cc9a48d53267914e3b3ed5b34ac1032dce625102a2d5b7",
            "0x59c6ea501659d8c310daa8c45446f8b4cb2e0c957774659ff09540137fbf48c"
        ],
        "transaction_hash": "0x151dc00880ad98fba7c614eaa9ddec270987787be290eddde4b346e8660f63f",
        "type": "INVOKE",
        "version": "0x1"
    }
}
```
{% endcode %}
