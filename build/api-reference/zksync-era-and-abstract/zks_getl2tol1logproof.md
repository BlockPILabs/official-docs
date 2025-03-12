---
description: >-
  Given a transaction hash, and an index of the L2 to L1 log produced within the
  transaction, it returns the proof for the corresponding L2 to L1 log.
---

# zks\_getL2ToL1LogProof

**Parameters:**

**tx\_hash-bytes32**, Hash of the L2 transaction the L2 to L1 log was produced within.

**l2\_to\_l1\_log\_index-number,** The index of the L2 to L1 log in the transaction (optional). #

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getL2ToL1LogProof", "params": [ "0x2a1c6c74b184965c0cb015aae9ea134fd96215d2e4f4979cfec12563295f610e" ]}'

// Result
{
  "jsonrpc": "2.0",
  "result": {
    "id": 0,
    "proof": [
      "0x8c48910df2ca7de509daf50b3182fcdf2dd6c422c6704054fd857d6c9516d6fc",
      "0xc5028885760b8b596c4fa11497c783752cb3a3fb3b8e6b52d7e54b9f1c63521e",
      "0xeb1f451eb8163723ee19940cf3a8f2a2afdf51100ce8ba25839bd94a057cda16",
      "0x7aabfd367dea2b5306b8071c246b99566dae551a1dbd40da791e66c4f696b236",
      "0xe4733f281f18ba3ea8775dd62d2fcd84011c8c938f16ea5790fd29a03bf8db89",
      "0x1798a1fd9c8fbb818c98cff190daa7cc10b6e5ac9716b4a2649f7c2ebcef2272",
      "0x66d7c5983afe44cf15ea8cf565b34c6c31ff0cb4dd744524f7842b942d08770d",
      "0xb04e5ee349086985f74b73971ce9dfe76bbed95c84906c5dffd96504e1e5396c",
      "0xac506ecb5465659b3a927143f6d724f91d8d9c4bdb2463aee111d9aa869874db"
    ],
    "root": "0x920c63cb0066a08da45f0a9bf934517141bd72d8e5a51421a94b517bf49a0d39"
  },
  "id": 1
}



```
{% endcode %}
