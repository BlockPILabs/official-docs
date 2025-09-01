---
description: Returns the value from a storage position at a given address.
---

# eth\_getStorageAt

#### **Parameters:**

**DATA, 20 Bytes** - address of the storage.

**QUANTITY** - integer of the position in the storage.

**QUANTITY|TAG** - integer block number, or the string "latest"

#### **Returns:**

**DATA** - the value at this storage position.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://story-odyssey-evm.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getStorageAt","params":["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x0", "latest"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
```
{% endcode %}
