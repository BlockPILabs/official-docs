---
description: >-
  Get the contract class hash in the given block for the contract deployed at
  the given address
---

# starknet\_getClassHashAt

#### **Parameters:**

**BLOCK\_PARAM**  -  Expected one of `block_number`, `block_hash`, `latest`, `pending`

**CONTRACT\_ADDRESS**  -  The address of the contract to read from

#### **Returns:**

The class hash of the given contract

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://starknet.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data '{"jsonrpc":"2.0","method":"starknet_getClassHashAt","params":["latest", "0x04c0a5193d58f74fbace4b74dcf65481e734ed1714121bdc571da345540efa05"],"id":1}'

// Result
{
    "id": 1,
    "jsonrpc": "2.0",
    "result": "0x7d1bd0a80107d8ffdb7fe5158548ac852ff02e8823fda8704d8cfa5b2f532e4"
}
```
{% endcode %}
