---
description: >-
  Polling method for a filter, which returns an array of logs that occurred
  since the last poll.
---

# eth\_getFilterChanges

#### **Parameters:**

**QUANTITY** - the filter id.

#### **Returns:**

**Array** - Array of log objects, or an empty array if nothing has changed since last poll.

* For filters created with eth\_newBlockFilter the return are block hashes (DATA, 32 Bytes), e.g. \["0x3454645634534..."].
* For filters created with eth\_newFilter logs are objects with the following params:
  * **removed: TAG** - true when the log was removed, due to a chain reorganization. false if its a valid log.
  * **logIndex: QUANTITY** - integer of the log index position in the block. null when its pending log.
  * **transactionIndex: QUANTITY** - integer of the transactions index position log was created from. null when its pending log.
  * **transactionHash: DATA, 32 Bytes** - hash of the transactions this log was created from. null when its pending log.
  * **blockHash: DATA, 32 Bytes** - hash of the block where this log was in. null when its pending log.
  * **blockNumber: QUANTITY** - the block number where this log was in. null when its pending log.
  * **address: DATA, 20 Bytes** - address from which this log originated.
  * **data: DATA** - contains one or more 32 Bytes non-indexed arguments of the log.
  * **topics: Array of DATA** - Array of 0 to 4 32 Bytes DATA of indexed log arguments. (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://berachain-bartio.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getFilterChanges","params":["0x927f6d0d98f5870982fbbb72a134a8b0"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": [
        "0xca6ae08fdd004912c2c4b7805071029af3500f11c73bce96db6e3285be084b44",
        "0xd7c0b754f6a939e61c3db90a50cfc69dab5a0bbe2ed7e4df07e0f8268bcd07e1",
        "0x637ef980fd4eaca6a0999c67fc732759ed83ed8ac730f723f8e64df43f32b6b0",
        "0xa57dc9ed6626eade4b1d3755d6eef70b1934affafe98aab67c6cfa9ba0e20c1b",
        "0xd399ad100953d36bb0e76c18ccb9e4a3022b98e65a88ce8b7272b4d7170cc3cb",
        "0x13fd12a09a3c8e1d7bb9c062cf493719a0880388951d749766ca6bd1b0913730",
        "0x0359c8b7b39e58b0c3e9c21c26a224701d22a835ad91139a482dc6d6e1bc0346",
        "0x596796d606495472534c5e63cded99b048c1cda0fc5232c5e1be1ab2d1356efb",
        "0x45d086e46bf210f655787d7cb529e237c28837c689832b8bcd56a35625228da0",
        "0xce632677ef859576275de0e7e2b27028b1e6d2e5b247c04e3aa922e0cd0b26c2",
        "0x836b682100f47ce6ef11a703ad9032182dafcfb9bc9c37d8cfb0cf2e8ebb8051",
        "0xdc778e8efd53ec813666a0baa5eb8e141ddcf449c2ed4be93ede31bfeca03470",
        "0xb68e3a020e18998da0155cbe0fb79e3ad9c80f00a0ced3dee2b206622b9603c0",
        "0x202e52ffa1c65f57ca7720a7360d7344aa15a6d0c1cf1ecb04548b74d23ffdab",
        "0x3654bb1a17e1ce177630634d1dd374805880b6aac5d3ad3fca04164ccefe6ad0"
    ]
}
```
{% endcode %}
