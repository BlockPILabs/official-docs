---
description: estimate the L2 fee of a message sent on L1
---

# starknet\_estimateMessageFee

#### **Parameters:**

**OBJECT** - The transaction call object

* `from_address -` The address of the L1 contract sending the message
* `to_address -`The target L2 address the message is sent to
* `entry_point_selector-`The selector of the l1\_handler to invoke in the target contract
* `payload`-  The payload of the message

**BLOCK\_PARAM**  -  Expected one of `block_number`, `block_hash`, `latest`, `pending`

#### **Returns:**

the fee estimation

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{
  "method": "starknet_estimateMessageFee",
  "params": [
    "latest",
    {
      "from_address": "0xAbCdEf0123456789aBcDeF0123456789AbCdEf01",
      "to_address": "0x044e5b3f0471a26bc749ffa1d8dd8e43640e05f1b33cf05cef6adee6f5b1b4cf",
      "entry_point_selector": "0x00000"
    }
  ]
}'

// Result
{

}
```
{% endcode %}
