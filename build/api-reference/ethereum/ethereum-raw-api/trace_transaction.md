---
description: Returns all traces of given transaction.
---

# trace\_transaction

#### **Parameters:**

**DATA, 32 Bytes** - Transaction hash.

#### **Returns:**

**Array**- Trace object

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"trace_transaction","params":["0x023b70dc940203684ef33fa8292973f159c6ddd46a9190224472dae9175986aa"],"id":1,"jsonrpc":"2.0"}'
      
// Result
{
      "jsonrpc":"2.0",
      "id":1,
      "result":[{
            "action":{
                  "from":"0xdafea492d9c6733ae3d56b7ed1adb60692c98bc5",
                  "callType":"call",
                  "gas":"0x0",
                  "input":"0x",
                  "to":"0x4675c7e5baafbffbca748158becba61ef3b0a263",
                  "value":"0x95315d765ced2f"
            },
            "blockHash":"0x9ed304f0736ba4acaa45a33a31ae15e81ac4e8a4eaaec8cfd5b080d46fa1acc9",
            "blockNumber":15923417,
            "result":{
                  "gasUsed":"0x0",
                  "output":"0x"
            },
            "subtraces":0,
            "traceAddress":[],
            "transactionHash":"0x023b70dc940203684ef33fa8292973f159c6ddd46a9190224472dae9175986aa",
            "transactionPosition":129,"type":"call"
      }]
}
```
{% endcode %}
