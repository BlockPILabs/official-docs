---
description: >-
  Given a block, a sender, a message, and an optional message log index in the
  block containing the L1->L2 message, it returns the proof for the message sent
  via the L1Messenger system contract.
---

# zks\_getL2ToL1MsgProof

**Parameters:**

**block-uint32**, The number of the block where the message was emitted.&#x20;

**sender-address**, The sender of the message (i.e. the account that called the L1Messenger system contract).&#x20;

**msg-bytes32**, The keccak256 hash of the sent message.&#x20;

**l2\_log\_position-uint256,** The index in the block of the event that was emitted by the L1Messenger when submitting this message. If it is omitted, the proof for the first message returns. #curl example

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getL2ToL1MsgProof", "params": [ 5187, "0x87869cb87c4Fa78ca278dF358E890FF73B42a39E", "0x22de7debaa98758afdaee89f447ff43bab5da3de6acca7528b281cc2f1be2ee9" ]}'

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
