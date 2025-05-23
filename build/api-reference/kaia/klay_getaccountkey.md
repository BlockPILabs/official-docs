---
description: >-
  Returns the account key of the Externally Owned Account (EOA) of a given
  address.
---

# klay\_getAccountKey

#### **Parameters**

| Type                    | Description                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| 20-byte DATA            | Address                                                                                                    |
| QUANTITY \| TAG \| HASH | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`, or block hash. |

#### **Return Value**

| Type       | Description                                              |
| ---------- | -------------------------------------------------------- |
| AccountKey | The account key consist of public key(s) and a key type. |

#### Example

{% code overflow="wrap" %}
```json
// Request (AccountKey type: AccountKeyPublic)
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_getAccountKey","params":["0x3111a0577f322e8fb54f78d9982a26ae7ca0f722", "latest"],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id":1,
  "result": {
    key: {
      x: "0x230037a99462acd829f317d0ce5c8e2321ac2951de1c1b1a18f9af5cff66f0d7",
      y: "0x18a7fb1b9012d2ac87bc291cbf1b3b2339356f1ce7669ae68405389be7f8b3b6"
    },
    keyType: 2
  }
}
```
{% endcode %}
