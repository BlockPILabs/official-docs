---
description: >-
  Encodes an account key using the Recursive Length Prefix (RLP) encoding
  scheme.
---

# klay\_encodeAccountKey

#### **Parameters**

| Name    | Type      | Description                                                                                                                                                              |
| ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| keytype | QUANTITY  | Integer value indicating account key type. For the value of each account key type, see [Klaytn Docs](https://docs.klaytn.foundation/klaytn/design/accounts#account-key). |
| key     | JSON DATA | Account key object                                                                                                                                                       |

#### **Return Value**

| Type | Description             |
| ---- | ----------------------- |
| DATA | RLP encoded account key |

#### Example

{% code overflow="wrap" %}
```json
// Request to encode AccountKeyNil
curl -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "method": "klay_encodeAccountKey", "params": [{"keyType": 0, "key": {}}], "id": 66}' http://127.0.0.1:8551

// Result
{
    "id": 66,
    "jsonrpc": "2.0",
    "result": "0x80"
}
```
{% endcode %}
