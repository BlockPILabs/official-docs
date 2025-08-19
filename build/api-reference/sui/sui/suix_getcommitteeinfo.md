---
description: Return the committee information for the asked epoch.
---

# suix\_getCommitteeInfo

#### **Parameters:**

**epoch< BigInt\_for\_uint64 >** - The epoch of interest. If None, default to the latest epoch

#### **Returns:**

SuiCommittee< CommitteeInfo >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getCommitteeInfo",
  "params": [
    "5"
  ]
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "epoch": "5",
        "validators": [
            [
                "gHcc2rJLuqE2EX+S1nvErlvh2CtcMkoTVJieRgH/k8gNEDjQaZ87OkdgmaR1RQjqBKwk5wCiKcMrfjeAwcSnqI4EVKTuWw12Rj6qIhjCqulY+E3y0zCvsgd81MgqTzCs",
                "43"
            ],
            ......
```
{% endcode %}
