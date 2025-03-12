---
description: Gets a batch for a given number
---

# zkevm\_getBatchByNumber

#### **Parameters:**

An array of strings

**String** - the batch number (in hex) or batch tag

The optional batch height descriptions are:

`latest` - This is the most recent batch in the canonical chain observed by the client. This batch may be re-orged out of the canonical chain even under healthy/normal conditions.

`earliest` - This is the lowest-numbered batch the client has available. Intuitively, you can think of this as the first batch created.

#### **Returns:**

**number: string** - the hex representation of given batch number

**coinbase: string** - the Coinbase address

**stateRoot: string** - the state root

**globalExitRoot: string** - the global exit root

**mainnetExitRoot: string** - the mainnet exit root

**rollupExitRoot: string** - the rollup exit root

**localExitRoot: string** - the local exit root

**accInputHash: string** - the accumulated input hash

**timestamp: string** - the timestamp

**sendSequencesTxHash: string** - the send sequences transaction hash

**verifyBatchTxHash: string** - the verify batch transaction hash

**transactions: array\[String]** - the transactions

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://polygon-zkevm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
'{
    "jsonrpc": "2.0",
    "method": "zkevm_getBatchByNumber",
    "params": [],
    "id": 1
}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": {as described above}
}
```
{% endcode %}
