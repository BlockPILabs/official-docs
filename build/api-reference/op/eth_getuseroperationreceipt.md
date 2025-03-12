---
description: returns a UserOperation by its hash returned from eth_sendUserOperation
---

# eth\_getUserOperationReceipt

#### **Parameters:**

**string**- hash of the UserOperation

#### **Returns:**

**Object**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 0,
  "method": "eth_getUserOperationByHash",
  "params": [userOpHash, entrypointAddress]
}'

// Result
{
    "jsonrpc": "2.0",
    "id": 0,
    "result": {
        userOpHash,
        sender,
        nonce,
        paymaster,
        actualGasCost, // actual (gas price * gas used) of the user operation
        actualGasUsed, // actual gas used of the user operation
        success, // user operation revert status
        reason, // If reverted, user operation revert reason
        logs,
        receipt, // The TransactionReceipt object. Note that the returned TransactionReceipt is for the entire bundle, not only for this UserOperation
    }
}
```
{% endcode %}
