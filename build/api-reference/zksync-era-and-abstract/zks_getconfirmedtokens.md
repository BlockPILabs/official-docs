---
description: >-
  Returns [address, symbol, name, and decimal] information of all tokens within
  a range of ids given by parameters from and limit.
---

# zks\_getConfirmedTokens

#### **Parameters:**

**from-uint32**, The token id from which to start returning the information about the tokens.

**limit-uint8**, The number of tokens to be returned from the API.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://zksync-era.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "id": 1, "method": "zks_getConfirmedTokens", "params": [ 1, 3 ]}'

// Result
{{
  "jsonrpc": "2.0",
  "result": [
    {
      "decimals": 18,
      "l1Address": "0xba100000625a3754423978a60c9317c58a424e3d",
      "l2Address": "0xaff169fca5086940c890c8a04c6db4b1db6e0dd6",
      "name": "Balancer",
      "symbol": "BAL"
    },
    {
      "decimals": 18,
      "l1Address": "0xffffffff2ba8f66d4e51811c5190992176930278",
      "l2Address": "0xc2b13bb90e33f1e191b8aa8f44ce11534d5698e3",
      "name": "Furucombo",
      "symbol": "COMBO"
    },
    {
      "decimals": 18,
      "l1Address": "0xa487bf43cf3b10dffc97a9a744cbb7036965d3b9",
      "l2Address": "0x140d5bc5b62d6cb492b1a475127f50d531023803",
      "name": "Deri",
      "symbol": "DERI"
    }
  ],
  "id": 1
}



```
{% endcode %}
