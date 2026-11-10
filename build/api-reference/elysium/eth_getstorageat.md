# eth\_getstorageat

#### **Parameters:**

**DATA, 20 Bytes** - address of the storage.

**QUANTITY** - integer of the position in the storage.

**QUANTITY|TAG** - integer block number, or the string "latest", "earliest" or "pending".

#### **Returns:**

**DATA** - the value at this storage position.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getStorageAt","params":["0x063f7cc5339f92a5fd7baf3d22233044fda1f327","0x0","latest"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x0000000000000000000000002796005dc02e04d84cb6a91420259e921a0d5ae1"
}
```
{% endcode %}
