---
description: Returns the receipt of a transaction by sender transaction hash.
---

# klay\_getTransactionReceiptBySenderTxHash

#### **Parameters**

| Name | Type         | Description                                                              |
| ---- | ------------ | ------------------------------------------------------------------------ |
| Hash | 32-byte DATA | Hash of a transaction before signing of feePayer(senderTransactionHash). |

#### **Return Value**

`Object` - A transaction object, or `null` when no transaction was found:

| Name               | Type                    | Description                                                                                                                                                                                                  |
| ------------------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| blockHash          | 32-byte DATA            | Hash of the block where this transaction was in.                                                                                                                                                             |
| blockNumber        | QUANTITY                | Block number where this transaction was in.                                                                                                                                                                  |
| codeFormat         | String                  | (optional) The code format of smart contract code.                                                                                                                                                           |
| contractAddress    | DATA                    | The contract address created, if the transaction was a contract creation, otherwise `null`.                                                                                                                  |
| feePayer           | 20-byte DATA            | Address of the fee payer.                                                                                                                                                                                    |
| feePayerSignatures | Array                   | (optional) An array of fee payer's signature objects. A signature object contains three fields (V, R, and S). V contains ECDSA recovery id. R contains ECDSA signature r while S contains ECDSA signature s. |
| feeRatio           | QUANTITY                | (optional) Fee ratio of the fee payer. If it is 30, 30% of the fee will be paid by the fee payer. 70% will be paid by the sender.                                                                            |
| from               | 20-byte DATA            | Address of the sender.                                                                                                                                                                                       |
| gas                | QUANTITY                | Gas provided by the sender.                                                                                                                                                                                  |
| gasPrice           | QUANTITY                | Gas price provided by the sender in peb.                                                                                                                                                                     |
| gasUsed            | QUANTITY                | The amount of gas used by this specific transaction alone.                                                                                                                                                   |
| humanReadable      | Boolean                 | (optional) `true` if the address is humanReadable, `false` if the address is not humanReadable.                                                                                                              |
| key                | String                  | (optional) Key of the newly created account.                                                                                                                                                                 |
| input              | DATA                    | (optional) The data sent along with the transaction.                                                                                                                                                         |
| logs               | Array                   | Array of log objects, which this transaction generated.                                                                                                                                                      |
| logsBloom          | 256-byte DATA           | Bloom filter for light clients to quickly retrieve related logs.                                                                                                                                             |
| nonce              | QUANTITY                | The number of transactions made by the sender prior to this one.                                                                                                                                             |
| senderTxHash       | (optional) 32-byte DATA | Hash of the tx without the fee payer's address and signature. This value is always the same as the value of transactionHash for non fee-delegated transactions.                                              |
| signatures         | Array                   | An array of signature objects. A signature object contains three fields (V, R, and S). V contains ECDSA recovery id. R contains ECDSA signature r while S contains ECDSA signature s.                        |
| status             | QUANTITY                | Either `1` (success) or `0` (failure).                                                                                                                                                                       |
| txError            | QUANTITY                | (optional) detailed error code if `status` is equal to zero.                                                                                                                                                 |
| to                 | 20-byte DATA            | Address of the receiver. `null` when it is a contract creation transaction.                                                                                                                                  |
| transactionHash    | 32-byte DATA            | Hash of the transaction.                                                                                                                                                                                     |
| transactionIndex   | QUANTITY                | Integer of the transaction index position in the block.                                                                                                                                                      |
| type               | String                  | A string representing the type of the transaction.                                                                                                                                                           |
| typeInt            | QUANTITY                | An integer representing the type of the transaction.                                                                                                                                                         |
| value              | QUANTITY                | Value transferred in peb.                                                                                                                                                                                    |

#### Example

{% code overflow="wrap" %}
```json
// Request
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"klay_getTransactionReceiptBySenderTxHash","params":["0x18fe9e1007da7d20aad77778557fb8acc58c80054daba65124c8c843aadd3478"],"id":1}' http://klaytn.blockpi.network/v1/rpc/your-api-key

// Result
{
  "jsonrpc":"2.0",
  "id":1,
  "result":{
    "blockHash":"0x4d97cf1f686a925ed4f1ad42c635cedb54974fe23a2941c7825e1ed3163c0e41",
    "blockNumber":"0x7008",
    "contractAddress":null,
    "feePayer":"0xa9d2cc2bb853163b6eadfb6f962d72f7e00bc2e6",
    "feePayerSignatures":[
      {
        "V":"0x4e44",
        "R":"0xa665e17d92e1c671c8b062cecb19790d49138a21854fc15c460c91035b1884e",
        "S":"0x17165688acc01736f1221a39399e3aac7e1ece14731fcab31631e3e4a59b7441"
      }
    ],
    "from":"0xab0833d744a8943fe3c783f9cc70c13cbd70fcf4",
    "gas":"0xdbba0",
    "gasPrice":"0x5d21dba00",
    "gasUsed":"0x7918",
    "logs":[],
    "logsBloom":"0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "nonce":"0x26",
    "senderTxHash":"0x18fe9e1007da7d20aad77778557fb8acc58c80054daba65124c8c843aadd3478",
    "signatures":[
      {
        "V":"0x4e44",
        "R":"0x1b6bb3d996d903d0528565d13e8d9d122b2220ed09c5baf384114193a6977027",
        "S":"0x20c506ce9f1bdd42183c40c44f414a3930f339f856e8be3cfcdf5ca0852fd378"
      }
    ],
    "status":"0x1",
    "to":"0x15a9119104e1bf0ec6d408b3cc188685e4402a2c",
    "transactionHash":"0xaca5d9a1ed8b86b1ef61431b2bedfc99a66eaefc3a7e1cffdf9ff53653956a67",
    "transactionIndex":"0x0",
    "type":"TxTypeFeeDelegatedValueTransfer",
    "typeInt":9,
    "value":"0x1"
  }
}
```
{% endcode %}
