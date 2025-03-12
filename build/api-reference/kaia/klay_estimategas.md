---
description: >-
  Generates and returns an estimate of how much gas is necessary to allow the
  transaction to complete.
---

# klay\_estimateGas

#### **Parameters**

| Name       | Type   | Description                                                                  |
| ---------- | ------ | ---------------------------------------------------------------------------- |
| callObject | Object | The transaction call object. See the next table for the object's properties. |

`callObject` has the following properties:

| Name     | Type         | Description                                                                                                                                                               |
| -------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from     | 20-byte DATA | (optional) The address the transaction is sent from.                                                                                                                      |
| to       | 20-byte DATA | (optional when testing the deployment of a new contract) The address the transaction is directed to.                                                                      |
| gas      | QUANTITY     | (optional) Integer of the upper gas limit provided for the gas estimation. If no gas limit is specified, the Klaytn node uses the designated gas limit as an upper bound. |
| gasPrice | QUANTITY     | (optional) Integer of the gasPrice used for each paid gas.                                                                                                                |
| value    | QUANTITY     | (optional) Integer of the value sent with this transaction.                                                                                                               |
| data     | DATA         | (optional) Hash of the method signature and encoded parameters.                                                                                                           |

#### **Return Value**

| Type     | Description             |
| -------- | ----------------------- |
| QUANTITY | The amount of gas used. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "method": "klay_estimateGas", "params": [{"from": "0x3f71029af4e252b25b9ab999f77182f0cd3bc085", "to": "0x87ac99835e67168d4f9a40580f8f5c33550ba88b", "gas": "0x100000", "gasPrice": "0x5d21dba00", "value": "0x0", "data": "0x8ada066e"}], "id": 1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0","id":1,
  "result": "0x5208" // 21000
}
```
{% endcode %}
