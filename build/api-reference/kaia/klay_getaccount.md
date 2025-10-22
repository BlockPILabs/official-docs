---
description: >-
  Returns the account information of a given address. There are two different
  account types in Klaytn: Externally Owned Account (EOA) and Smart Contract
  Account.
---

# kaia\_getAccount

#### **Parameters**

| Name                 | Type                    | Description                                                                                                |
| -------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| address              | 20-byte DATA            | Address                                                                                                    |
| block number or hash | QUANTITY \| TAG \| HASH | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`, or block hash. |

#### **Return Value**

| Type    | Description                                 |
| ------- | ------------------------------------------- |
| Account | Each account type has different attributes. |

#### Example

{% code overflow="wrap" %}
```json
// Request (Account type: Externally Owned Account)
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"kaia_getAccount","params":["0x3111a0577f322e8fb54f78d9982a26ae7ca0f722", "latest"],"id":1}' http://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    accType: 1,
    account: {
      balance: 4985316100000000000,
      humanReadable: false,
      key: {
        key: {
          x: "0x230037a99462acd829f317d0ce5c8e2321ac2951de1c1b1a18f9af5cff66f0d7",
          y: "0x18a7fb1b9012d2ac87bc291cbf1b3b2339356f1ce7669ae68405389be7f8b3b6"
        },
        keyType: 2
      },
      nonce: 11
    }
  }
}
```
{% endcode %}
