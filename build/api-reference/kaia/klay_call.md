---
description: >-
  Executes a new message call immediately without creating a transaction on the
  block chain. It returns data or an error object of JSON RPC if error occurs.
---

# klay\_call

#### **Parameters**

| Name              | Type                    | Description                                                                                |
| ----------------- | ----------------------- | ------------------------------------------------------------------------------------------ |
| callObject        | Object                  | The transaction call object. See the next table for the object's properties.               |
| blockNumberOrHash | QUANTITY \| TAG \| HASH | Integer or hexadecimal block number, or the string `"earliest"`, `"latest"` or `"pending"` |

`callObject` has the following properties:

<table><thead><tr><th>Name</th><th width="310">Type</th><th>Description</th></tr></thead><tbody><tr><td>from</td><td>20-byte DATA</td><td>(optional) The address the transaction is sent from.</td></tr><tr><td>to</td><td>20-byte DATA</td><td>(optional when testing the deployment of a new contract) The address the transaction is directed to.</td></tr><tr><td>gas</td><td>QUANTITY</td><td>(optional) Integer of the gas provided for the transaction execution. <code>klay_call</code> consumes zero gas, but this parameter may be needed by some executions.<br></td></tr><tr><td>gasPrice</td><td>QUANTITY</td><td>(optional) Integer of the gasPrice used for each paid gas.</td></tr><tr><td>value</td><td>QUANTITY</td><td>(optional) Integer of the value sent with this transaction.</td></tr><tr><td>data</td><td>DATA</td><td>(optional) Hash of the method signature and encoded parameters. Data size is limited to 20KB.</td></tr></tbody></table>

#### **Return Value**

| Type | Description                            |
| ---- | -------------------------------------- |
| DATA | The return value of executed contract. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "method": "klay_call", "params": [{"from": "0x3f71029af4e252b25b9ab999f77182f0cd3bc085", "to": "0x87ac99835e67168d4f9a40580f8f5c33550ba88b", "gas": "0x100000", "gasPrice": "0x5d21dba00", "value": "0x0", "data": "0x8ada066e"}, "latest"], "id": 1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{"jsonrpc":"2.0","id":1,"result":"0x000000000000000000000000000000000000000000000000000000000000000a"}
```
{% endcode %}
