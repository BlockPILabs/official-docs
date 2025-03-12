---
description: Returns the information about a transaction requested by transaction hash.
---

# eth\_getTransactionByHash

#### **Parameters:**

**DATA, 32 Bytes** - hash of a transaction

#### **Returns:**

**Object** - A transaction object, or null when no transaction was found:

* **blockHash: DATA, 32 Bytes** - hash of the block where this transaction was in.
* **blockNumber: QUANTITY** - block number where this transaction was in.
* **from: DATA, 20 Bytes** - address of the sender.
* **gas: QUANTITY** - gas provided by the sender.
* **gasPrice: QUANTITY** - gas price provided by the sender in Wei.
* **hash: DATA, 32 Bytes** - hash of the transaction.
* **input: DATA** - the data send along with the transaction.
* **nonce: QUANTITY** - the number of transactions made by the sender prior to this one.
* **to: DATA, 20 Bytes** - address of the receiver. null when its a contract creation transaction.
* **transactionIndex: QUANTITY** - integer of the transactions index position in the block.
* **value: QUANTITY** - value transferred in Wei.
* **v: QUANTITY** - ECDSA recovery id
* **r: DATA, 32 Bytes** - ECDSA signature r
* **s: DATA, 32 Bytes** - ECDSA signature s

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0x32e69225d68e2d3969776b33011c984b0ab030a71907008ff88d4757922883e2"],"id":1}'

// Result
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "blockHash": "0x9639114abbde6058f5fa4fa8c6db0a67be88bde27e37c825f47b462f716ef5cc",
        "blockNumber": "0x92e869",
        "chainId": "0x118",
        "from": "0xcb6f7e93f0fcbadee2fe746001eab7107069c1fe",
        "gas": "0x1c9c380",
        "gasPrice": "0xee6b280",
        "hash": "0x32e69225d68e2d3969776b33011c984b0ab030a71907008ff88d4757922883e2",
        "input": "0xbb2cd72800000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000100000000000000000000000020b28b1e4665fff290650586ad76e977eab90c5d00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000002ecb1f7bac",
        "maxFeePerGas": "0x77359400",
        "maxPriorityFeePerGas": "0x77359400",
        "nonce": "0xd867c",
        "r": "0xcdd1147205d06b432f165fb76ee1020d35ee153f7ac1b75372dd5641e6bfc35b",
        "s": "0x547271a525a171225f6407e77717a123201f800ee6d142eb582e8e83c1616e43",
        "to": "0x01767c7f08e2ac33df97cb74e80bbd184058c8cc",
        "transactionIndex": "0x0",
        "type": "0x0",
        "v": "0x0",
        "value": "0x0"
    }
}
```
{% endcode %}
