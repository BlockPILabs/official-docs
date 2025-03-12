---
description: >-
  Creates a filter object, based on filter options, to notify when the state
  changes (logs).
---

# klay\_newFilter

The execution of this API can be limited by two node configurations to manage resources of Klaytn node safely.

#### **Parameters**

`Object` - The filter options:

| Name      | Type                  | Description                                                                                                                     |
| --------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| fromBlock | QUANTITY \| TAG       | (optional, default: `"latest"`) Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`      |
| toBlock   | QUANTITY \| TAG       | (optional, default: `"latest"`) Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"`      |
| address   | 20-byte DATA \| Array | (optional) Contract address or a list of addresses from which logs should originate.                                            |
| topics    | Array of DATA         | (optional) Array of 32-byte DATA topics. Topics are order-dependent. Each topic can also be an array of DATA with "or" options. |

#### **Return Value**

| Type     | Description  |
| -------- | ------------ |
| QUANTITY | A filter id. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_newFilter","params":[{"fromBlock":"earliest","toBlock":"latest","address":"0x87ac99835e67168d4f9a40580f8f5c33550ba88b","topics":["0xd596fdad182d29130ce218f4c1590c4b5ede105bee36690727baa6592bd2bfc8"]}],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{"jsonrpc":"2.0","id":1,"result":"0xd32fd16b6906e67f6e2b65dcf48fc272"}
```
{% endcode %}
