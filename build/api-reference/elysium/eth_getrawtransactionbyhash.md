# eth\_getrawtransactionbyhash

#### **Parameters:**

**DATA, 32 Bytes** - hash of a transaction.

#### **Returns:**

**DATA** - the raw, RLP-encoded signed transaction payload (including the type prefix byte for typed transactions).

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getRawTransactionByHash","params":["0xc6ed0a1582d665eca7f4d61f87d9ec72c58b6643ec864af2b6ed8dd665356a03"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x02f8b58301863d8201038459a3b1608459a3b16083030d4094063f7cc5339f92a5fd7baf3d22233044fda1f32780b844095ea7b3000000000000000000000000ca0d2b3047e547fd256c325db04634fa923aab52000000000000000000000000000000000000000000000d51097a8a84d0836dc5c080a00f1ef715f38f239286cb6fe348f1c5c37291ba7a977d68e286b8e596637aa849a00b5551377a881419f2a4badff9585c7e22cf824f044203bdb30ea7875516400f"
}
```
{% endcode %}
