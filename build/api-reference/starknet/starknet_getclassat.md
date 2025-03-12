---
description: Get the contract class definition in the given block at the given address
---

# starknet\_getClassAt

#### **Parameters:**

**BLOCK\_PARAM**  -  Expected one of `block_number`, `block_hash`, `latest`, `pending`.

**CONTRACT\_ADDRESS**  -  The address of the contract to read from.

#### **Returns:**

The contract class.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"starknet_getClassAt","params":["latest","0x47ce89d6bbea3ef36ac32e8ab32dd7c055f8af9b11718a2211168dcb225157"],"id":1}'

// Result
{
    
}
```
{% endcode %}
