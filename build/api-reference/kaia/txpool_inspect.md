---
description: >-
  list a textual summary of all the transactions currently pending for inclusion
  in the next block(s), as well as the ones that are being scheduled for future
  execution only.
---

# txpool\_inspect

This is a method specifically tailored to developers to quickly see the transactions in the pool and find any potential issues.

#### **Parameters**

**None**

#### **Return Value**

| Type        | Description                                |
| ----------- | ------------------------------------------ |
| JSON string | A list of pending and queued transactions. |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"txpool_inspect","id":1}' https://kaia.blockpi.network/v1/rpc/your-api-key

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "pending": {
            "0x11Af0E6E34d8a067FdA5De79E6EbcEFB1638995d": {
                "0": "0xAfdE910130C335fA5bD5fe991053E3E0a49dcE7b: 0 peb + 300000 gas × 50000000000 peb"
            },
            "0x707CE8E9BB32005800f1a99D11C6ec6f96486aA7": {
                "44530": "0xf50782A24afCb26ACb85d086Cf892bFfFB5731B5: 100000000000000000000 peb + 200000000 gas × 50000000000 peb"
            },
            "0xAa98DE5a58250e3ab9F70A028c2E4E2bcdBc9A91": {
                "26683": "0x782Aa061b15a06a729bBFB54F85DD81296DF268a: 0 peb + 3960000 gas × 50000000000 peb"
            },
            "0xCEFF58Dd3811060992352292531b4ad0E7Fc21fA": {
                "1": "0x5eA4D7714B1a7BF34b38052E8449fD64C198b458: 0 peb + 197868 gas × 50000000000 peb"
            },
            "0xbe02ABa56bae1624e2c4f029e3a79308e2a19E98": {
                "91143450": "0x42D877932366DcafF751405c3185393f2803962d: 0 peb + 1000000 gas × 750000000000 peb",
                "91143451": "0x42D877932366DcafF751405c3185393f2803962d: 0 peb + 1000000 gas × 750000000000 peb",
                "91143452": "0x42D877932366DcafF751405c3185393f2803962d: 0 peb + 1000000 gas × 750000000000 peb",
                "91143453": "0x42D877932366DcafF751405c3185393f2803962d: 0 peb + 1000000 gas × 750000000000 peb",
                "91143454": "0x42D877932366DcafF751405c3185393f2803962d: 0 peb + 1000000 gas × 750000000000 peb"
            }
        },
        "queued": {}
    }
}
```
{% endcode %}
