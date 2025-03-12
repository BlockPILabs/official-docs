---
description: Returns the receipt information of a transaction by its l2 hash
---

# zkevm\_getTransactionReceiptByL2Hash

**Parameters:**

**DATA , 32 Bytes** - Hash of a block.

**Returns:**

**Object** - Transaction receipt result, or null when no block was found

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://merlin.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data 
{
    "jsonrpc": "2.0",
    "id": 18,
    "method": "zkevm_getTransactionReceiptByL2Hash",
    "params": [
      "0xb28b90c0cb796beade4c8642d19217129ae096c04a1c998bc2f4aec59cb866a7"
    ]
  }

// Result
{
    "jsonrpc": "2.0",
    "id": 18,
    "result": null
}
```
{% endcode %}
