# klay\_sign

The sign method calculates a Klaytn-specific signature with:

```
sign(keccak256("\x19Klaytn Signed Message:\n" + len(message) + message)))
```

Adding a prefix to the message makes the calculated signature recognizable as a Klaytn-specific signature. This prevents misuse where a malicious dApp can sign arbitrary data, _e.g._, transaction, and use the signature to impersonate the victim.

**NOTE**: The address to sign with must be unlocked.

#### **Parameters**

| Name    | Type         | Description     |
| ------- | ------------ | --------------- |
| account | 20-byte DATA | Address         |
| message | N-byte DATA  | Message to sign |

#### **Return Value**

| Type | Description |
| ---- | ----------- |
| DATA | Signature   |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_sign","params":["0x9b2055d370f73ec7d8a03e965129118dc8f5bf83", "0xdeadbeaf"],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc": "2.0",
  "id":1,
  "result": "0xa3f20717a250c2b0b729b7e5becbff67fdaef7e0699da4de7ca5895b02a170a12d887fd3b17bfdce3481f10bea41f45ba9f709d39ce8325427b57afcfc994cee1b"
}
```
{% endcode %}
