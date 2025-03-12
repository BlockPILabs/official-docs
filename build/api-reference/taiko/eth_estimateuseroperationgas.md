---
description: >-
  generates and returns an estimate of how much gas is necessary to allow the
  transaction to complete, given a UserOperation.
---

# eth\_estimateUserOperationGas

#### **Parameters:**

**Object** -&#x20;

#### **Returns:**

**Object**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://taiko.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 0,
  "method": "eth_estimateUserOperationGas",
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
    "result": {
        callGasLimit
        preVerificationGas,
        verificationGas,
    },
}
```
{% endcode %}
