---
description: >-
  Returns a list with a textual summary of all the transactions currently
  pending for inclusion in the next block(s), as well as the ones that are being
  scheduled for future execution only.
---

# txpool\_inspect

#### **Parameters:**

None

#### Returns:

**object** - with following fields:

* **pending** - Array of transaction objects,&#x20;
* **queued** - Array of transaction objects,&#x20;

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://linea.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"txpool_inspect","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "pending": {
            "0x0D06838D1DfBA9ef0a4166CCa9BE16Fb1D76DbfC": {
                "0": "0x0D06838D1DfBA9ef0a4166CCa9BE16Fb1D76DbfC: 0 wei + 57950000 gas × 64020011 wei",
                "1": "contract creation: 0 wei + 71933 gas × 58200010 wei",
                "2": "contract creation: 0 wei + 1874351 gas × 58800012 wei",
                "3": "0x0D06838D1DfBA9ef0a4166CCa9BE16Fb1D76DbfC: 0 wei + 71714 gas × 5500000000 wei"
            },
            "0x127531C03689C3D4fBFCd139ce4Fd35a53b5006c": {
                "193": "0x0B2c83B6e39E32f694a86633B4d1Fe69d13b63c5: 0 wei + 15005823 gas × 58200009 wei",
                "194": "0x8D95f56b0Bac46e8ac1d3A3F12FB1E5BC39b4c0c: 0 wei + 613098 gas × 58200009 wei"
            },
            ......
```
{% endcode %}
