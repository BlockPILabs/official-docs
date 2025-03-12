# /eth/v1/validator/register\_validator

Prepares the beacon node for engaging with external builders. The information must be sent by the beacon node to the builder network. It is expected that the validator client will send this information periodically to ensure the beacon node has correct and timely registration information to provide to builders. The validator client should not sign blinded beacon blocks that do not adhere to their latest fee recipient and gas limit preferences.

Note that only registrations for active or pending validators must be sent to the builder network. Registrations for unknown or exited validators must be filtered out and not sent to the builder network.

#### Parameters:

**None**

**Request body:**

array\<object>

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/register_validator

'
[
  {
    "message": {
      "fee_recipient": "0xAbcF8e0d4e9587369b2301D0790347320302cc09",
      "gas_limit": "1",
      "timestamp": "1",
      "pubkey": "0x93247f2209abcacf57b75a51dafae777f9dd38bc7053d1af526f220a7489a6d3a2753e5f3e8b1cfe39b56f43611df74a"
    },
    "signature": "0x1b66ac1fb663c9bc59509846d6ec05345bd908eda73e670af888da41af171505cc411d61252fb6cb3fa0017b679f8bb2305b26a285fa2737f175668d0dff91cc1b66ac1fb663c9bc59509846d6ec05345bd908eda73e670af888da41af171505"
  }
]
'

// Result

```
{% endcode %}
