---
description: >-
  Traces a call to eth_sendRawTransaction without making the call, returning the
  traces.
---

# trace\_replayTransaction

#### **Parameters:**

**DATA, 32 Bytes** - Transaction hash.

**Array** - Type of trace, one or more of: "vmTrace", "trace", "stateDiff".

#### **Returns:**

**Object** - Block traces.

#### Example:

{% code overflow="wrap" %}
```python
// Request
curl https://ethereum.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"method":"trace_replayTransaction","params":["0x023b70dc940203684ef33fa8292973f159c6ddd46a9190224472dae9175986aa",["trace"]],"id":1,"jsonrpc":"2.0"}'
      
// Result
{
      "jsonrpc":"2.0",
      "id":1,
      "result":{
            "output":"0x",
            "stateDiff":null,
            "trace":[{
                  "action":{
                        "from":"0xdafea492d9c6733ae3d56b7ed1adb60692c98bc5",
                        "callType":"call",
                        "gas":"0x0",
                        "input":"0x",
                        "to":"0x4675c7e5baafbffbca748158becba61ef3b0a263",
                        "value":"0x95315d765ced2f"
                  },
                  "result":{
                        "gasUsed":"0x0",
                        "output":"0x"
                  },
                  "subtraces":0,
                  "traceAddress":[],
                  "type":"call"
            }],
            "vmTrace":null
      }
}
```
{% endcode %}
