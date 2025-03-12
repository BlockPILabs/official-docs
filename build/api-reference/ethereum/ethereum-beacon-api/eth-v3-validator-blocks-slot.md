# /eth/v3/validator/blocks/{slot}

Requests a beacon node to produce a valid block, which can then be signed by a validator. The returned block may be blinded or unblinded, depending on the current state of the network as decided by the execution and beacon nodes.

The beacon node must return an unblinded block if it obtains the execution payload from its paired execution node. It must only return a blinded block if it obtains the execution payload header from an MEV relay.

Metadata in the response indicates the type of block produced, and the supported types of block will be added to as forks progress.

#### Parameters:

**slot-string**, The slot for which the block should be proposed.

**randao\_reveal-strin**g, The validator's randao reveal value.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v3/validator/blocks/9091319?randao_reveal=0xab786d85b52942b47599e403b98f53539aca5242d5e2435e3e8b43afd4e5d14d03c8e008f26f3151c9aad7aa488af33004e5afdc9bea2efd59cee3300c7ee5cf331bdba8163f835e70ace8f14b4991224f6c94ad1bd38a890b00b059b30e28e7

// Result

```
{% endcode %}
