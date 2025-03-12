---
description: Get the value of the storage at the given address and key
---

# starknet\_getStorageAt

#### **Parameters:**

**CONTRACT\_ADDRESS**  -  The address of the contract to read from

**STORAGE\_POSITION**  -  A hex code of an integer that represents the position in the storage.

**BLOCK\_PARAM**  -  "latest", "pending", or the hash of a block.&#x20;

#### **Returns:**

The value at the given key for the given contract. 0 if no value is found

#### Example:

<pre class="language-json" data-overflow="wrap"><code class="lang-json">// Request
<strong>curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_getStorageAt","params": ["0x04D88BeCbd1DC984ae04A96E77828E603c5244e68224903D92CA0a1Ff1C8e807", "0x21", "latest"],"id":1}'
</strong>
// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": "0x0"
}
</code></pre>
