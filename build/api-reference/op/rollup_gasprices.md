---
description: >-
  Returns the L1 and L2 gas prices that are being used by the Sequencer to
  calculate fees.
---

# rollup\_gasPrices

#### **Parameters:**

None

#### **Returns:**

**Object:**

* **l1GasPrice: QUANTITY** - L1 gas price in wei that the Sequencer will use to estimate the L1 portion of fees (calldata costs).
* **l2GasPrice: QUANTITY** - L2 gas price in wei that the Sequencer will use to estimate the L2 portion of fees (execution costs).

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://optimism.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"rollup_gasPrices","params":[],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "l1GasPrice": "0x315b84ced",
        "l2GasPrice": "0xf4240"
    }
}
```
{% endcode %}
