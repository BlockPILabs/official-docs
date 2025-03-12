---
description: estimate the fee for of StarkNet transactions
---

# starknet\_estimateFee

#### **Parameters:**

**OBJECT** - The transaction call object

* `contract_address -` Address the transaction is sent from
* `entry_point_selector -`Smart contract entry points
* `call_data -`The hash of method signature and encoded parameters.

**BLOCK\_PARAM**  -  Expected one of `block_number`, `block_hash`, `latest`, `pending`

#### **Returns:**

The fee estimation

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc":"2.0","method":"starknet_estimateFee","params":[""],"id":1}'

// Result
{

}
```
{% endcode %}
