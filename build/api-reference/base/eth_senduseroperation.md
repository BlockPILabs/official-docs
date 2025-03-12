---
description: asks the bundler to sign and submit a User Operation
---

# eth\_sendUserOperation

#### **Parameters:**

**Object**

#### **Returns:**

**String** - UserOperation hash

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://Base.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 0,
  "method": "eth_sendUserOperation",
  "params": [
    {
      sender,
      nonce,
      initCode,
      callData,
      callGasLimit,
      verificationGasLimit,
      preVerificationGas,
      maxFeePerGas,
      maxPriorityFeePerGas,
      paymasterAndData,
      signature,
    },
    entrypointAddress,
  ]
}'

// Result
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": "0x..." // UserOpHash
}
```
{% endcode %}
