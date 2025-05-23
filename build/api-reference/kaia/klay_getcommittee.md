---
description: >-
  Returns a list of all validators in the committee at the specified block. If
  the parameter is not set, returns a list of all validators in the committee at
  the latest block.
---

# klay\_getCommittee

#### **Parameters**

| Name            | Type         | Description                                                                               |
| --------------- | ------------ | ----------------------------------------------------------------------------------------- |
| address         | 20-byte DATA | Address                                                                                   |
| QUANTITY \| TAG | block number | (optional) Integer or hexadecimal block number, or the string `"earliest"` or `"latest"`  |

#### **Return Value**

`Array` - Array of addresses of all validators in the committee, or `null` when no committee was found:

| Type                  | Description                                   |
| --------------------- | --------------------------------------------- |
| Array of 20-byte DATA | Addresses of all validators in the committee. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "method":"klay_getCommittee", "params":["0x1b4"],"id":73}' http://klaytn.blockpi.network/v1/rpc/your-api-key
// Result
{
    "jsonrpc":"2.0",
    "id":73,
    "result":[
        "0x207e38864b45a538733741dc1ff92eff9d1a6159",
        "0x6d64bc82b93368a7f963d6c34483ca3893f405f6",
        "0xbc9c19f91878369776812039e4ebcdfa3c646716",
        "0xe3ed6fa287752b992f936b42360770c59731d9eb"
    ]
}
```
{% endcode %}
