---
description: Returns the latest global exit root used in a batch
---

# zkevm\_estimateCounters

**Parameters:**

**Object** - transaction

**Returns:**

**Object** - The counters used, limits and revert info when tx reverted

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://merlin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
{
    "method": "zkevm_estimateCounters",
    "params": [
        {
            "from": "0x8D97689C9818892B700e27F316cc3E41e17fBeb9",
            "to": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
            "gas": "0x5208"
        }
    ],
    "id": 1,
    "jsonrpc": "2.0"
}

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "countersUsed": {
            "gasUsed": "0x5208",
            "usedKeccakHashes": "0x6",
            "usedPoseidonHashes": "0x340",
            "usedPoseidonPaddings": "0x3",
            "usedMemAligns": "0x0",
            "usedArithmetics": "0x1d6",
            "usedBinaries": "0x25f",
            "usedSteps": "0x17a2",
            "usedSHA256Hashes": "0x0"
        },
        "countersLimit": {
            "maxGasUsed": "0x1c9c380",
            "maxKeccakHashes": "0x861",
            "maxPoseidonHashes": "0x3d9c5",
            "maxPoseidonPaddings": "0x21017",
            "maxMemAligns": "0x39c29",
            "maxArithmetics": "0x39c29",
            "maxBinaries": "0x73852",
            "maxSteps": "0x73846a",
            "maxSHA256Hashes": "0x63c"
        }
    }
}
```
{% endcode %}
