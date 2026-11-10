# eth\_getfilterchanges

#### **Parameters:**

**QUANTITY** - the filter id.

#### **Returns:**

**Array** - Array of log objects, or an empty array if nothing has changed since last poll.

{% hint style="info" %}
Filter IDs are node-local and expire after a period of inactivity, so always create the filter and poll it against the same node.
{% endhint %}

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getFilterChanges","params":["0x469df3d1e142d845b7b59af4c0366c97"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "address": "0x953837ec73c577b299eac0f670b21c808b3c1725",
      "topics": [
        "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
        "0x0000000000000000000000005dd2662a647845f535b289b8393d15cb16317608",
        "0x000000000000000000000000a13f7611115752deb2b13813bdde16a5073e4b45"
      ],
      "data": "0x00000000000000000000000000000000000000000000841181bb15070ecbe6a0",
      "blockNumber": "0x37ad2b",
      "transactionHash": "0xb3cff0a9c1afc7ee599e6ed0ccc2108e2c2ffc6e6126fec359b013b1a9b791a0",
      "transactionIndex": "0x1",
      "blockHash": "0xfaa775e0526baa3b651c06f497f35b8c7f2630ebeedb5afeb6bd10c08e7b9e27",
      "blockTimestamp": "0x6af274a9",
      "logIndex": "0x0",
      "removed": false
    },
    {
      "address": "0xe2e105d3f7209a9da11f83ccf3e7398a753823f1",
      "topics": [
        "0x40e9cecb9f5f1f1c5b9c97dec2917b7ee92e57ba5563708daca94dd84ad7112f",
        "0xb853a372bf82d3f9323b310dc48c708842d314b348ea4c5e67d8181a1f859186",
        "0x000000000000000000000000a13f7611115752deb2b13813bdde16a5073e4b45"
      ],
      "data": "0xffffffffffffffffffffffffffffffffffffffffffff7bee7e44eaf8f1...",
      "blockNumber": "0x37ad2b",
      "transactionHash": "0xb3cff0a9c1afc7ee599e6ed0ccc2108e2c2ffc6e6126fec359b013b1a9b791a0",
      "transactionIndex": "0x1",
      "blockHash": "0xfaa775e0526baa3b651c06f497f35b8c7f2630ebeedb5afeb6bd10c08e7b9e27",
      "blockTimestamp": "0x6af274a9",
      "logIndex": "0x1",
      "removed": false
    },
    "..."
  ]
}
```
{% endcode %}
