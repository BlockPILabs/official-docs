---
description: >-
  Get block headers for minHeight <= height <= maxHeight.  At most 20 items will
  be returned.  Upon success, the Cache-Control header will be set with the
  default maximum age.
---

# /blockchain

#### **Parameters:**

**minHeight - int**, Minimum block height to return

**maxHeight- int**, Maximumblock height to return

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://cosmos.blockpi.network/rpc/v1/<your-api-key>/blockchain

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "last_height": "14183787",
        "block_metas": [
            {
                "block_id": {
                    "hash": "2C05155623D32C429E683C35EDA20FE01D9665B2C787318C167DB0DF2BBE1EB0",
                    "parts": {
                        "total": 1,
                        "hash": "5915FE0AB841D5E41615A554E29879FDE7C7A810A38DD5F1E6F61DEA8401378A"
                    }
                },
                "block_size": "19457",
                "header": {
                    "version": {
                        "block": "11"
                    },
                    "chain_id": "cosmoshub-4",
                    "height": "14183787",
                    "time": "2023-02-22T06:58:45.769685617Z",
                    "last_block_id": {
                        "hash": "3BCBBEC45CAB7524A076327718FDBF7FF4FBF070771BD5243AE079874D733B19",
                        "parts": {
                            "total": 1,
                            "hash": "CB6EC9614063C6408CFC7D3093C0B6612FD9D1DE3EE257AEFE6BE299F055FB20"
                        }
                    },
                    "last_commit_hash": "52D5AFD048817DDCC6FCE02370EEF1D25397B66663F71B675F3FA26B768B6C92",
                    "data_hash": "2E14240B8E81B885888B02CD5E08999F249F14A08685B37E45192B08D9937166",
                    "validators_hash": "FA1F33B062C4992D5F430CBECD0F70285F2A561369485B5A0A98B30C08C28BC6",
                    "next_validators_hash": "826EFE978232583C39B78649711AED8963F67A1DA98764C210007234098DD6BE",
                    "consensus_hash": "80364965B7C2CC9DE961C0998B47A7F93F1970077EB882E0ED1C3822408888C7",
                    "app_hash": "0C191D3331951A69EE919DDB4E771CC6753268ACCA6C4223F8A56364F89DFA8F",
                    "last_results_hash": "6AAFA9E99988A588BF1DAE30CB4C71386EF0361491441A9542463905C8E2F7F4",
                    "evidence_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
                    "proposer_address": "CC87F56B58621811E2B5A47F38C6166E295CE36E"
                },
                "num_txs": "1"
            },
            {
                "block_id": {
                    "hash": "3BCBBEC45CAB7524A076327718FDBF7FF4FBF070771BD5243AE079874D733B19",
                    "parts": {
                        "total": 1,
                        "hash": "CB6EC9614063C6408CFC7D3093C0B6612FD9D1DE3EE257AEFE6BE299F055FB20"
                    }
                },
                "block_size": "19809",
                "header": {
                    "version": {
                        "block": "11"
                    },
                    "chain_id": "cosmoshub-4",
                    "height": "14183786",
                    "time": "2023-02-22T06:58:39.700465352Z",
                    "last_block_id": {
                        "hash": "0E9236A635FF416B33941D804A0ED1BFDACC4DAB49A951999C51D4DBBE80364D",
                        "parts": {
                            "total": 1,
                            "hash": "6A2954AD4B44DB889143D7274652E6597E2182FFB4D453FABC75A2FA0999F9AB"
                        }
                    },
                    "last_commit_hash": "A2303CD74D8FAAB7DF2B730DD72B758678AB8C520ACDCFF85D6B519104165A35",
                    "data_hash": "3892B1A7C7E347403DD4FCDAD1821FC3DB1F0ECD5EE12B26E77FC4A8A8DF6BEE",
                    "validators_hash": "FA1F33B062C4992D5F430CBECD0F70285F2A561369485B5A0A98B30C08C28BC6",
                    "next_validators_hash": "FA1F33B062C4992D5F430CBECD0F70285F2A561369485B5A0A98B30C08C28BC6",
                    "consensus_hash": "80364965B7C2CC9DE961C0998B47A7F93F1970077EB882E0ED1C3822408888C7",
                    "app_hash": "6C0D4B10E737B2205CAD2BBB3543BE6FF54531E9598557B9B2FDB5FF1D12DB54",
                    "last_results_hash": "D86C6CEF64948D50653E606CA52A8A6D94D6D7CEE629D7AF0A4BB5F732B45EF4",
                    "evidence_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
                    "proposer_address": "4EB1282675F724B59026F2173C23F0DC9936F118"
                },
                "num_txs": "2"
            },
            ......
        ]
    }
}
```
{% endcode %}
