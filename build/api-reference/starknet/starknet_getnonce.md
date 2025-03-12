---
description: Get the nonce associated with the given address in the given block
---

# starknet\_getNonce

#### **Parameters:**

**block\_id** - The hash of the requested block, or number (height) of the requested block, or a block tag

**contract\_address** - The address of the contract whose nonce we're seeking

#### **Returns:**

The contract's nonce at the requested state

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc":"2.0","method":"starknet_getNonce","params":["latest", "0x04c0a5193d58f74fbace4b74dcf65481e734ed1714121bdc571da345540efa05"],"id":1}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": "0x0"
}
```
{% endcode %}
