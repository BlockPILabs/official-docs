# eth\_getproof

#### **Parameters:**

**DATA, 20 Bytes** - address of the account.

**Array of DATA, 32 Bytes** - array of storage keys to prove. Pass `[]` to prove the account only.

**QUANTITY|TAG** - integer block number, or the string "latest", "earliest" or "pending".

#### **Returns:**

**Object** - Proof object:

* **address: DATA, 20 Bytes** - the address of the account.
* **accountProof: Array of DATA** - array of rlp-serialized Merkle trie nodes of the account.
* **balance: QUANTITY** - the balance of the account in wei.
* **codeHash: DATA, 32 Bytes** - hash of the code of the account.
* **nonce: QUANTITY** - nonce of the account.
* **storageHash: DATA, 32 Bytes** - SHA3 of the StorageRoot.
* **storageProof: Array** - array of storage proof objects (`key`, `value`, `proof`).

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getProof","params":["0x148ddcefd47234b60d4fe0463f7497ef7a71a27b",[],"latest"],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "address": "0x148ddcefd47234b60d4fe0463f7497ef7a71a27b",
    "accountProof": [
      "0xf90211a0ae8a5878afe68cf4abccbdfe375d784470f488766871c0bddd...",
      "0xf90211a019eeb78e0b78bfea817d2bde1596bdf08266e9e57a2b0422b0...",
      "..."
    ],
    "balance": "0x1bb8b35c05fe41552",
    "codeHash": "0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470",
    "nonce": "0x10d",
    "storageHash": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "storageProof": []
  }
}
```
{% endcode %}
