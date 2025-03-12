---
description: Returns trace at given position.
---

# trace\_get

#### **Parameters:**

**DATA, 32 Bytes** - Transaction hash.

**Array** - Index positions of the traces.

#### **Returns:**

**Object**- Trace object

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://fantom.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"trace_get","params":["0xa455c9030e7083763f0a71c2e2eda11f417d0ffadec9e64d482226f71585ea97",["0x0"]],"id":1,"jsonrpc":"2.0"}'
      
// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": [
        {
            "action": {
                "callType": "call",
                "from": "0x82487df5b4cf19db597a092c8103759466be9e5a",
                "gas": "0x66cb6c",
                "input": "0xc40493dc000000000000000000000000db73dde1867843fdca5244258f2fd4b6dc7b154e000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000446815434300000000000000000000000036694040dddb849f2a5323ce5972872dc47d99c2000000000000000000000000000000000000000000000000000000000000007800000000000000000000000000000000000000000000000000000000",
                "to": "0xc3df1eae0c26c6d71fda556ceec4cb679bfda240",
                "value": "0x0"
            },
            "blockHash": "0x0003dd5f00000cd3197456d4e7d96fe0dadbd29c48f11e1ddeb1789ab540eba8",
            "blockNumber": 72467584,
            "result": {
                "gasUsed": "0x16d0d",
                "output": "0x"
            },
            "subtraces": 1,
            "traceAddress": [
                0
            ],
            "transactionHash": "0xa455c9030e7083763f0a71c2e2eda11f417d0ffadec9e64d482226f71585ea97",
            "transactionPosition": 0,
            "type": "call"
        }
    ]
}
```
{% endcode %}
