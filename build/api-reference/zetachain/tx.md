---
description: >-
  Get a transaction.  Upon success, the Cache-Control header will be set with
  the default maximum age.
---

# /tx

#### **Parameters:**

**hash- string**, hash of transaction to retrieve

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json'  https://zetachain.blockpi.network/rpc/v1/<your-api-key>/tx?hash=0x46D04F0B4ED3303B86554799E11659D16E144E6976385D65050FBAB56B862891

// Result
{
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "hash": "46D04F0B4ED3303B86554799E11659D16E144E6976385D65050FBAB56B862891",
        "height": "2115661",
        "index": 0,
        "tx_result": {
            "code": 0,
            "data": "CjsKOS96ZXRhY2hhaW4uemV0YWNvcmUuY3Jvc3NjaGFpbi5Nc2dWb3RlT25PYnNlcnZlZEluYm91bmRUeA==",
            "log": "[{\"events\":[{\"type\":\"crosschain/CctxCreated\",\"attributes\":[{\"key\":\"CctxIndex\",\"value\":\"0x42df7342fd8a609a97febc5fdd7013ad08589ebaa482d78a5d8e0c18f2b12e68\"},{\"key\":\"Sender\",\"value\":\"0x8A01c988376d5cEd12e7406E468554fb388E086D\"},{\"key\":\"SenderChain\",\"value\":\"BSCTESTNET\"},{\"key\":\"TxOrigin\",\"value\":\"0x8A01c988376d5cEd12e7406E468554fb388E086D\"},{\"key\":\"InTxObservedHash\",\"value\":\"0x315f6029f1ad99b6f4500523b67de67e7b36d1e5f738f2f598cb5f01255c4a12\"},{\"key\":\"Receiver\",\"value\":\"0x8A01c988376d5cEd12e7406E468554fb388E086D\"},{\"key\":\"ReceiverChain\",\"value\":\"ZETA\"},{\"key\":\"ZetaBurnt\",\"value\":\"35000000000000000\"},{\"key\":\"NewStatus\",\"value\":\"PendingInbound\"},{\"key\":\"LogIdentifiers\",\"value\":\"0x8A01c988376d5cEd12e7406E468554fb388E086D-BSCTESTNET-ZETA-0\"}]},{\"type\":\"crosschain/ZrcWithdrawCreated\",\"attributes\":[{\"key\":\"CctxIndex\",\"value\":\"0x86f6088a5a1241c21e94ba0fbfbdbf009695c50cfda9f88963b81fbeca4eb207\"},{\"key\":\"Sender\",\"value\":\"0x71Ec5c05Aa669c4922569c1D33F7a81aaa218138\"},{\"key\":\"SenderChain\",\"value\":\"ZETA\"},{\"key\":\"InTxObservedHash\",\"value\":\"0x0000000000000000000000000000000000000000000000000000000000000000\"},{\"key\":\"Receiver\",\"value\":\"0x0000000000000000000000008a01c988376d5ced12e7406e468554fb388e086d\"},{\"key\":\"ReceiverChain\",\"value\":\"GOERLI\"},{\"key\":\"ZetaBurnt\",\"value\":\"760524937963083\"},{\"key\":\"NewStatus\",\"value\":\"PendingOutbound\"},{\"key\":\"LogIdentifiers\",\"value\":\"0x71Ec5c05Aa669c4922569c1D33F7a81aaa218138-ZETA-GOERLI-0\"}]},{\"type\":\"ethereum_tx\",\"attributes\":[{\"key\":\"amount\",\"value\":\"0\"},{\"key\":\"ethereumTxHash\",\"value\":\"0xb48d38f93eaa084033fc5970bf96e559c33c4cdc07d889ab00b4d63f9590739d\"},{\"key\":\"txIndex\",\"value\":\"8888\"},{\"key\":\"txGasUsed\",\"value\":\"268690\"},{\"key\":\"txHash\",\"value\":\"46D04F0B4ED3303B86554799E11659D16E144E6976385D65050FBAB56B862891\"},{\"key\":\"recipient\",\"value\":\"0x239e96c8f17C85c30100AC26F635Ea15f23E9c67\"}]},{\"type\":\"message\",\"attributes\":[{\"key\":\"action\",\"value\":\"SendVoter\"},{\"key\":\"module\",\"value\":\"fungible\"},{\"key\":\"sender\",\"value\":\"0x735b14BB79463307AAcBED86DAf3322B1e6226aB\"},{\"key\":\"txType\",\"value\":\"88\"},{\"key\":\"module\",\"value\":\"zetacore\"},{\"key\":\"action\",\"value\":\"depositZRC4AndCallContract\"},{\"key\":\"contract\",\"value\":\"0x71Ec5c05Aa669c4922569c1D33F7a81aaa218138\"},{\"key\":\"data\",\"value\":\"00000000000000000000000091d18e54daf4f677cb28167158d6dd21f6ab39210000000000000000000000008a01c988376d5ced12e7406e468554fb388e086d0000000000000000000000000000000000000000000000000000000000000000\"},{\"key\":\"cctxIndex\",\"value\":\"0x42df7342fd8a609a97febc5fdd7013ad08589ebaa482d78a5d8e0c18f2b12e68\"}]},{\"type\":\"tx_log\",\"attributes\":[{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x13A0c5930C028511Dc02665E7285134B6d11A5f4\\\",\\\"topics\\\":[\\\"0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef\\\",\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHxYUIcjgAA=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":0}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x13A0c5930C028511Dc02665E7285134B6d11A5f4\\\",\\\"topics\\\":[\\\"0x67fc7bdaed5b0ec550d8706b87d60568ab70c6b781263c70101d54cd1564aab3\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfFhQhyOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUc1sUu3lGMweqy+2G2vMyKx5iJqsAAAAAAAAAAAAAAAA=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":1}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x13A0c5930C028511Dc02665E7285134B6d11A5f4\\\",\\\"topics\\\":[\\\"0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\",\\\"0x0000000000000000000000002ca7d64a7efe2d62a725e2b35cf7230d6677ffee\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHxYUIcjgAA=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":2}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x13A0c5930C028511Dc02665E7285134B6d11A5f4\\\",\\\"topics\\\":[\\\"0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\",\\\"0x0000000000000000000000000c0b35c5ef00d9cad8d2ce65b147ea2a27d526bc\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHxYUIcjgAA=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":3}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x13A0c5930C028511Dc02665E7285134B6d11A5f4\\\",\\\"topics\\\":[\\\"0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\",\\\"0x0000000000000000000000002ca7d64a7efe2d62a725e2b35cf7230d6677ffee\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":4}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x5F0b1a82749cb4E2278EC87F8BF6B618dC71a8bf\\\",\\\"topics\\\":[\\\"0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef\\\",\\\"0x0000000000000000000000000c0b35c5ef00d9cad8d2ce65b147ea2a27d526bc\\\",\\\"0x000000000000000000000000719e237dae24fe0b7a81ddcf4d54c69f48232406\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPrTImAwXED8=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":5}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x0C0B35C5eF00d9caD8D2ce65b147ea2A27d526Bc\\\",\\\"topics\\\":[\\\"0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYqeW2OIcE4HsAAAAAAAAAAAAAAAAAAAAAAAAAAAAADHliLUVxFBlNyg==\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":6}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x0C0B35C5eF00d9caD8D2ce65b147ea2A27d526Bc\\\",\\\"topics\\\":[\\\"0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822\\\",\\\"0x0000000000000000000000002ca7d64a7efe2d62a725e2b35cf7230d6677ffee\\\",\\\"0x000000000000000000000000719e237dae24fe0b7a81ddcf4d54c69f48232406\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHxYUIcjgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPrTImAwXED8=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":7}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x91d18e54DAf4F677cB28167158d6dd21F6aB3921\\\",\\\"topics\\\":[\\\"0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef\\\",\\\"0x000000000000000000000000719e237dae24fe0b7a81ddcf4d54c69f48232406\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoDHxT0KqM=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":8}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x719E237DaE24fe0b7A81DDcF4d54c69F48232406\\\",\\\"topics\\\":[\\\"0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4gusX79i3tRJYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJDLPdnbkqVOA==\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":9}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x719E237DaE24fe0b7A81DDcF4d54c69F48232406\\\",\\\"topics\\\":[\\\"0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822\\\",\\\"0x0000000000000000000000002ca7d64a7efe2d62a725e2b35cf7230d6677ffee\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPrTImAwXED8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoDHxT0KqM=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":10}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x91d18e54DAf4F677cB28167158d6dd21F6aB3921\\\",\\\"topics\\\":[\\\"0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\",\\\"0x00000000000000000000000091d18e54daf4f677cb28167158d6dd21f6ab3921\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdPbZIvBFg=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":11}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x91d18e54DAf4F677cB28167158d6dd21F6aB3921\\\",\\\"topics\\\":[\\\"0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\",\\\"0x000000000000000000000000735b14bb79463307aacbed86daf3322b1e6226ab\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdPbZIvBFg=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":12}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x91d18e54DAf4F677cB28167158d6dd21F6aB3921\\\",\\\"topics\\\":[\\\"0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\",\\\"0x00000000000000000000000091d18e54daf4f677cb28167158d6dd21f6ab3921\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":13}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x91d18e54DAf4F677cB28167158d6dd21F6aB3921\\\",\\\"topics\\\":[\\\"0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\",\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKzsYLFJks=\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":14}\"},{\"key\":\"txLog\",\"value\":\"{\\\"address\\\":\\\"0x91d18e54DAf4F677cB28167158d6dd21F6aB3921\\\",\\\"topics\\\":[\\\"0x9ffbffc04a397460ee1dbe8c9503e098090567d6b7f4b3c02a8617d800b6d955\\\",\\\"0x00000000000000000000000071ec5c05aa669c4922569c1d33f7a81aaa218138\\\"],\\\"data\\\":\\\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArOxgsUmSwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHT22SLwRYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAIoByYg3bVztEudAbkaFVPs4jght\\\",\\\"blockNumber\\\":2115661,\\\"transactionHash\\\":\\\"0x0000000000000000000000000000000000000000000000000000000000000000\\\",\\\"transactionIndex\\\":0,\\\"blockHash\\\":\\\"0x9dff465be04752b7685a6af50c9bd5681985ac6ae8763aa0f4d377633248dd46\\\",\\\"logIndex\\\":15}\"}]}]}]",
            "info": "",
            "gas_wanted": "10000000",
            "gas_used": "8837225",
            "events": [
                {
                    "type": "coin_spent",
                    "attributes": [
                        {
                            "key": "c3BlbmRlcg==",
                            "value": "emV0YTFrazlqcXd1ZmhjZXZlYWtjYWp2MzB3aGo2OGcyMjhkY2NzMnhlNQ==",
                            "index": true
                        },
                        {
                            "key": "YW1vdW50",
                            "value": "NDAwMDBhemV0YQ==",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "coin_received",
                    "attributes": [
                        {
                            "key": "cmVjZWl2ZXI=",
                            "value": "emV0YTE3eHBmdmFrbTJhbWc5NjJ5bHM2Zjg0ejNrZWxsOGM1bHhhZDQzZA==",
                            "index": true
                        },
                        {
                            "key": "YW1vdW50",
                            "value": "NDAwMDBhemV0YQ==",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "transfer",
                    "attributes": [
                        {
                            "key": "cmVjaXBpZW50",
                            "value": "emV0YTE3eHBmdmFrbTJhbWc5NjJ5bHM2Zjg0ejNrZWxsOGM1bHhhZDQzZA==",
                            "index": true
                        },
                        {
                            "key": "c2VuZGVy",
                            "value": "emV0YTFrazlqcXd1ZmhjZXZlYWtjYWp2MzB3aGo2OGcyMjhkY2NzMnhlNQ==",
                            "index": true
                        },
                        {
                            "key": "YW1vdW50",
                            "value": "NDAwMDBhemV0YQ==",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "message",
                    "attributes": [
                        {
                            "key": "c2VuZGVy",
                            "value": "emV0YTFrazlqcXd1ZmhjZXZlYWtjYWp2MzB3aGo2OGcyMjhkY2NzMnhlNQ==",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "tx",
                    "attributes": [
                        {
                            "key": "ZmVl",
                            "value": "NDAwMDBhemV0YQ==",
                            "index": true
                        },
                        {
                            "key": "ZmVlX3BheWVy",
                            "value": "emV0YTFrazlqcXd1ZmhjZXZlYWtjYWp2MzB3aGo2OGcyMjhkY2NzMnhlNQ==",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "tx",
                    "attributes": [
                        {
                            "key": "YWNjX3NlcQ==",
                            "value": "emV0YTFrazlqcXd1ZmhjZXZlYWtjYWp2MzB3aGo2OGcyMjhkY2NzMnhlNS8xNDA4OTQ1Mw==",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "tx",
                    "attributes": [
                        {
                            "key": "c2lnbmF0dXJl",
                            "value": "NUVNclA1WGxkdW1KY1gwYlUrVGxGRVR4cC9lRnNEL29aeS9KL1BaenNqc0hCMEM1ZlUxTENIcWhJVktEaEtubmsyTmM4VU9STUdkS3VmdWZzV2tXeWc9PQ==",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "message",
                    "attributes": [
                        {
                            "key": "YWN0aW9u",
                            "value": "U2VuZFZvdGVy",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "crosschain/CctxCreated",
                    "attributes": [
                        {
                            "key": "Q2N0eEluZGV4",
                            "value": "MHg0MmRmNzM0MmZkOGE2MDlhOTdmZWJjNWZkZDcwMTNhZDA4NTg5ZWJhYTQ4MmQ3OGE1ZDhlMGMxOGYyYjEyZTY4",
                            "index": true
                        },
                        {
                            "key": "U2VuZGVy",
                            "value": "MHg4QTAxYzk4ODM3NmQ1Y0VkMTJlNzQwNkU0Njg1NTRmYjM4OEUwODZE",
                            "index": true
                        },
                        {
                            "key": "U2VuZGVyQ2hhaW4=",
                            "value": "QlNDVEVTVE5FVA==",
                            "index": true
                        },
                        {
                            "key": "VHhPcmlnaW4=",
                            "value": "MHg4QTAxYzk4ODM3NmQ1Y0VkMTJlNzQwNkU0Njg1NTRmYjM4OEUwODZE",
                            "index": true
                        },
                        {
                            "key": "SW5UeE9ic2VydmVkSGFzaA==",
                            "value": "MHgzMTVmNjAyOWYxYWQ5OWI2ZjQ1MDA1MjNiNjdkZTY3ZTdiMzZkMWU1ZjczOGYyZjU5OGNiNWYwMTI1NWM0YTEy",
                            "index": true
                        },
                        {
                            "key": "UmVjZWl2ZXI=",
                            "value": "MHg4QTAxYzk4ODM3NmQ1Y0VkMTJlNzQwNkU0Njg1NTRmYjM4OEUwODZE",
                            "index": true
                        },
                        {
                            "key": "UmVjZWl2ZXJDaGFpbg==",
                            "value": "WkVUQQ==",
                            "index": true
                        },
                        {
                            "key": "WmV0YUJ1cm50",
                            "value": "MzUwMDAwMDAwMDAwMDAwMDA=",
                            "index": true
                        },
                        {
                            "key": "TmV3U3RhdHVz",
                            "value": "UGVuZGluZ0luYm91bmQ=",
                            "index": true
                        },
                        {
                            "key": "TG9nSWRlbnRpZmllcnM=",
                            "value": "MHg4QTAxYzk4ODM3NmQ1Y0VkMTJlNzQwNkU0Njg1NTRmYjM4OEUwODZELUJTQ1RFU1RORVQtWkVUQS0w",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "ethereum_tx",
                    "attributes": [
                        {
                            "key": "YW1vdW50",
                            "value": "MA==",
                            "index": true
                        },
                        {
                            "key": "ZXRoZXJldW1UeEhhc2g=",
                            "value": "MHhiNDhkMzhmOTNlYWEwODQwMzNmYzU5NzBiZjk2ZTU1OWMzM2M0Y2RjMDdkODg5YWIwMGI0ZDYzZjk1OTA3Mzlk",
                            "index": true
                        },
                        {
                            "key": "dHhJbmRleA==",
                            "value": "ODg4OA==",
                            "index": true
                        },
                        {
                            "key": "dHhHYXNVc2Vk",
                            "value": "MjY4Njkw",
                            "index": true
                        },
                        {
                            "key": "dHhIYXNo",
                            "value": "NDZEMDRGMEI0RUQzMzAzQjg2NTU0Nzk5RTExNjU5RDE2RTE0NEU2OTc2Mzg1RDY1MDUwRkJBQjU2Qjg2Mjg5MQ==",
                            "index": true
                        },
                        {
                            "key": "cmVjaXBpZW50",
                            "value": "MHgyMzllOTZjOGYxN0M4NWMzMDEwMEFDMjZGNjM1RWExNWYyM0U5YzY3",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "tx_log",
                    "attributes": [
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHgxM0EwYzU5MzBDMDI4NTExRGMwMjY2NUU3Mjg1MTM0QjZkMTFBNWY0IiwidG9waWNzIjpbIjB4ZGRmMjUyYWQxYmUyYzg5YjY5YzJiMDY4ZmMzNzhkYWE5NTJiYTdmMTYzYzRhMTE2MjhmNTVhNGRmNTIzYjNlZiIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMCIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBSHhZVUljamdBQT0iLCJibG9ja051bWJlciI6MjExNTY2MSwidHJhbnNhY3Rpb25IYXNoIjoiMHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidHJhbnNhY3Rpb25JbmRleCI6MCwiYmxvY2tIYXNoIjoiMHg5ZGZmNDY1YmUwNDc1MmI3Njg1YTZhZjUwYzliZDU2ODE5ODVhYzZhZTg3NjNhYTBmNGQzNzc2MzMyNDhkZDQ2IiwibG9nSW5kZXgiOjB9",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHgxM0EwYzU5MzBDMDI4NTExRGMwMjY2NUU3Mjg1MTM0QjZkMTFBNWY0IiwidG9waWNzIjpbIjB4NjdmYzdiZGFlZDViMGVjNTUwZDg3MDZiODdkNjA1NjhhYjcwYzZiNzgxMjYzYzcwMTAxZDU0Y2QxNTY0YWFiMyIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFFQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQWZGaFFoeU9BQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQVVjMXNVdTNsR013ZXF5KzJHMnZNeUt4NWlKcXNBQUFBQUFBQUFBQUFBQUFBPSIsImJsb2NrTnVtYmVyIjoyMTE1NjYxLCJ0cmFuc2FjdGlvbkhhc2giOiIweDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLCJ0cmFuc2FjdGlvbkluZGV4IjowLCJibG9ja0hhc2giOiIweDlkZmY0NjViZTA0NzUyYjc2ODVhNmFmNTBjOWJkNTY4MTk4NWFjNmFlODc2M2FhMGY0ZDM3NzYzMzI0OGRkNDYiLCJsb2dJbmRleCI6MX0=",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHgxM0EwYzU5MzBDMDI4NTExRGMwMjY2NUU3Mjg1MTM0QjZkMTFBNWY0IiwidG9waWNzIjpbIjB4OGM1YmUxZTVlYmVjN2Q1YmQxNGY3MTQyN2QxZTg0ZjNkZDAzMTRjMGY3YjIyOTFlNWIyMDBhYzhjN2MzYjkyNSIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMmNhN2Q2NGE3ZWZlMmQ2MmE3MjVlMmIzNWNmNzIzMGQ2Njc3ZmZlZSJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBSHhZVUljamdBQT0iLCJibG9ja051bWJlciI6MjExNTY2MSwidHJhbnNhY3Rpb25IYXNoIjoiMHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidHJhbnNhY3Rpb25JbmRleCI6MCwiYmxvY2tIYXNoIjoiMHg5ZGZmNDY1YmUwNDc1MmI3Njg1YTZhZjUwYzliZDU2ODE5ODVhYzZhZTg3NjNhYTBmNGQzNzc2MzMyNDhkZDQ2IiwibG9nSW5kZXgiOjJ9",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHgxM0EwYzU5MzBDMDI4NTExRGMwMjY2NUU3Mjg1MTM0QjZkMTFBNWY0IiwidG9waWNzIjpbIjB4ZGRmMjUyYWQxYmUyYzg5YjY5YzJiMDY4ZmMzNzhkYWE5NTJiYTdmMTYzYzRhMTE2MjhmNTVhNGRmNTIzYjNlZiIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMGMwYjM1YzVlZjAwZDljYWQ4ZDJjZTY1YjE0N2VhMmEyN2Q1MjZiYyJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBSHhZVUljamdBQT0iLCJibG9ja051bWJlciI6MjExNTY2MSwidHJhbnNhY3Rpb25IYXNoIjoiMHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidHJhbnNhY3Rpb25JbmRleCI6MCwiYmxvY2tIYXNoIjoiMHg5ZGZmNDY1YmUwNDc1MmI3Njg1YTZhZjUwYzliZDU2ODE5ODVhYzZhZTg3NjNhYTBmNGQzNzc2MzMyNDhkZDQ2IiwibG9nSW5kZXgiOjN9",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHgxM0EwYzU5MzBDMDI4NTExRGMwMjY2NUU3Mjg1MTM0QjZkMTFBNWY0IiwidG9waWNzIjpbIjB4OGM1YmUxZTVlYmVjN2Q1YmQxNGY3MTQyN2QxZTg0ZjNkZDAzMTRjMGY3YjIyOTFlNWIyMDBhYzhjN2MzYjkyNSIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMmNhN2Q2NGE3ZWZlMmQ2MmE3MjVlMmIzNWNmNzIzMGQ2Njc3ZmZlZSJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQT0iLCJibG9ja051bWJlciI6MjExNTY2MSwidHJhbnNhY3Rpb25IYXNoIjoiMHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidHJhbnNhY3Rpb25JbmRleCI6MCwiYmxvY2tIYXNoIjoiMHg5ZGZmNDY1YmUwNDc1MmI3Njg1YTZhZjUwYzliZDU2ODE5ODVhYzZhZTg3NjNhYTBmNGQzNzc2MzMyNDhkZDQ2IiwibG9nSW5kZXgiOjR9",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHg1RjBiMWE4Mjc0OWNiNEUyMjc4RUM4N0Y4QkY2QjYxOGRDNzFhOGJmIiwidG9waWNzIjpbIjB4ZGRmMjUyYWQxYmUyYzg5YjY5YzJiMDY4ZmMzNzhkYWE5NTJiYTdmMTYzYzRhMTE2MjhmNTVhNGRmNTIzYjNlZiIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMGMwYjM1YzVlZjAwZDljYWQ4ZDJjZTY1YjE0N2VhMmEyN2Q1MjZiYyIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzE5ZTIzN2RhZTI0ZmUwYjdhODFkZGNmNGQ1NGM2OWY0ODIzMjQwNiJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFQclRJbUF3WEVEOD0iLCJibG9ja051bWJlciI6MjExNTY2MSwidHJhbnNhY3Rpb25IYXNoIjoiMHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidHJhbnNhY3Rpb25JbmRleCI6MCwiYmxvY2tIYXNoIjoiMHg5ZGZmNDY1YmUwNDc1MmI3Njg1YTZhZjUwYzliZDU2ODE5ODVhYzZhZTg3NjNhYTBmNGQzNzc2MzMyNDhkZDQ2IiwibG9nSW5kZXgiOjV9",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHgwQzBCMzVDNWVGMDBkOWNhRDhEMmNlNjViMTQ3ZWEyQTI3ZDUyNkJjIiwidG9waWNzIjpbIjB4MWM0MTFlOWE5NmUwNzEyNDFjMmYyMWY3NzI2YjE3YWU4OWUzY2FiNGM3OGJlNTBlMDYyYjAzYTlmZmZiYmFkMSJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQVlxZVcyT0ljRTRIc0FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBREhsaUxVVnhGQmxOeWc9PSIsImJsb2NrTnVtYmVyIjoyMTE1NjYxLCJ0cmFuc2FjdGlvbkhhc2giOiIweDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLCJ0cmFuc2FjdGlvbkluZGV4IjowLCJibG9ja0hhc2giOiIweDlkZmY0NjViZTA0NzUyYjc2ODVhNmFmNTBjOWJkNTY4MTk4NWFjNmFlODc2M2FhMGY0ZDM3NzYzMzI0OGRkNDYiLCJsb2dJbmRleCI6Nn0=",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHgwQzBCMzVDNWVGMDBkOWNhRDhEMmNlNjViMTQ3ZWEyQTI3ZDUyNkJjIiwidG9waWNzIjpbIjB4ZDc4YWQ5NWZhNDZjOTk0YjY1NTFkMGRhODVmYzI3NWZlNjEzY2UzNzY1N2ZiOGQ1ZTNkMTMwODQwMTU5ZDgyMiIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMmNhN2Q2NGE3ZWZlMmQ2MmE3MjVlMmIzNWNmNzIzMGQ2Njc3ZmZlZSIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzE5ZTIzN2RhZTI0ZmUwYjdhODFkZGNmNGQ1NGM2OWY0ODIzMjQwNiJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBSHhZVUljamdBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQVByVEltQXdYRUQ4PSIsImJsb2NrTnVtYmVyIjoyMTE1NjYxLCJ0cmFuc2FjdGlvbkhhc2giOiIweDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLCJ0cmFuc2FjdGlvbkluZGV4IjowLCJibG9ja0hhc2giOiIweDlkZmY0NjViZTA0NzUyYjc2ODVhNmFmNTBjOWJkNTY4MTk4NWFjNmFlODc2M2FhMGY0ZDM3NzYzMzI0OGRkNDYiLCJsb2dJbmRleCI6N30=",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHg5MWQxOGU1NERBZjRGNjc3Y0IyODE2NzE1OGQ2ZGQyMUY2YUIzOTIxIiwidG9waWNzIjpbIjB4ZGRmMjUyYWQxYmUyYzg5YjY5YzJiMDY4ZmMzNzhkYWE5NTJiYTdmMTYzYzRhMTE2MjhmNTVhNGRmNTIzYjNlZiIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzE5ZTIzN2RhZTI0ZmUwYjdhODFkZGNmNGQ1NGM2OWY0ODIzMjQwNiIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQW9ESHhUMEtxTT0iLCJibG9ja051bWJlciI6MjExNTY2MSwidHJhbnNhY3Rpb25IYXNoIjoiMHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidHJhbnNhY3Rpb25JbmRleCI6MCwiYmxvY2tIYXNoIjoiMHg5ZGZmNDY1YmUwNDc1MmI3Njg1YTZhZjUwYzliZDU2ODE5ODVhYzZhZTg3NjNhYTBmNGQzNzc2MzMyNDhkZDQ2IiwibG9nSW5kZXgiOjh9",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHg3MTlFMjM3RGFFMjRmZTBiN0E4MUREY0Y0ZDU0YzY5RjQ4MjMyNDA2IiwidG9waWNzIjpbIjB4MWM0MTFlOWE5NmUwNzEyNDFjMmYyMWY3NzI2YjE3YWU4OWUzY2FiNGM3OGJlNTBlMDYyYjAzYTlmZmZiYmFkMSJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBNGd1c1g3OWkzdFJKWUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFKRExQZG5ia3FWT0E9PSIsImJsb2NrTnVtYmVyIjoyMTE1NjYxLCJ0cmFuc2FjdGlvbkhhc2giOiIweDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLCJ0cmFuc2FjdGlvbkluZGV4IjowLCJibG9ja0hhc2giOiIweDlkZmY0NjViZTA0NzUyYjc2ODVhNmFmNTBjOWJkNTY4MTk4NWFjNmFlODc2M2FhMGY0ZDM3NzYzMzI0OGRkNDYiLCJsb2dJbmRleCI6OX0=",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHg3MTlFMjM3RGFFMjRmZTBiN0E4MUREY0Y0ZDU0YzY5RjQ4MjMyNDA2IiwidG9waWNzIjpbIjB4ZDc4YWQ5NWZhNDZjOTk0YjY1NTFkMGRhODVmYzI3NWZlNjEzY2UzNzY1N2ZiOGQ1ZTNkMTMwODQwMTU5ZDgyMiIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMmNhN2Q2NGE3ZWZlMmQ2MmE3MjVlMmIzNWNmNzIzMGQ2Njc3ZmZlZSIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFQclRJbUF3WEVEOEFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBb0RIeFQwS3FNPSIsImJsb2NrTnVtYmVyIjoyMTE1NjYxLCJ0cmFuc2FjdGlvbkhhc2giOiIweDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLCJ0cmFuc2FjdGlvbkluZGV4IjowLCJibG9ja0hhc2giOiIweDlkZmY0NjViZTA0NzUyYjc2ODVhNmFmNTBjOWJkNTY4MTk4NWFjNmFlODc2M2FhMGY0ZDM3NzYzMzI0OGRkNDYiLCJsb2dJbmRleCI6MTB9",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHg5MWQxOGU1NERBZjRGNjc3Y0IyODE2NzE1OGQ2ZGQyMUY2YUIzOTIxIiwidG9waWNzIjpbIjB4OGM1YmUxZTVlYmVjN2Q1YmQxNGY3MTQyN2QxZTg0ZjNkZDAzMTRjMGY3YjIyOTFlNWIyMDBhYzhjN2MzYjkyNSIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwOTFkMThlNTRkYWY0ZjY3N2NiMjgxNjcxNThkNmRkMjFmNmFiMzkyMSJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQWRQYlpJdkJGZz0iLCJibG9ja051bWJlciI6MjExNTY2MSwidHJhbnNhY3Rpb25IYXNoIjoiMHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidHJhbnNhY3Rpb25JbmRleCI6MCwiYmxvY2tIYXNoIjoiMHg5ZGZmNDY1YmUwNDc1MmI3Njg1YTZhZjUwYzliZDU2ODE5ODVhYzZhZTg3NjNhYTBmNGQzNzc2MzMyNDhkZDQ2IiwibG9nSW5kZXgiOjExfQ==",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHg5MWQxOGU1NERBZjRGNjc3Y0IyODE2NzE1OGQ2ZGQyMUY2YUIzOTIxIiwidG9waWNzIjpbIjB4ZGRmMjUyYWQxYmUyYzg5YjY5YzJiMDY4ZmMzNzhkYWE5NTJiYTdmMTYzYzRhMTE2MjhmNTVhNGRmNTIzYjNlZiIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzM1YjE0YmI3OTQ2MzMwN2FhY2JlZDg2ZGFmMzMyMmIxZTYyMjZhYiJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQWRQYlpJdkJGZz0iLCJibG9ja051bWJlciI6MjExNTY2MSwidHJhbnNhY3Rpb25IYXNoIjoiMHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidHJhbnNhY3Rpb25JbmRleCI6MCwiYmxvY2tIYXNoIjoiMHg5ZGZmNDY1YmUwNDc1MmI3Njg1YTZhZjUwYzliZDU2ODE5ODVhYzZhZTg3NjNhYTBmNGQzNzc2MzMyNDhkZDQ2IiwibG9nSW5kZXgiOjEyfQ==",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHg5MWQxOGU1NERBZjRGNjc3Y0IyODE2NzE1OGQ2ZGQyMUY2YUIzOTIxIiwidG9waWNzIjpbIjB4OGM1YmUxZTVlYmVjN2Q1YmQxNGY3MTQyN2QxZTg0ZjNkZDAzMTRjMGY3YjIyOTFlNWIyMDBhYzhjN2MzYjkyNSIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwOTFkMThlNTRkYWY0ZjY3N2NiMjgxNjcxNThkNmRkMjFmNmFiMzkyMSJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQT0iLCJibG9ja051bWJlciI6MjExNTY2MSwidHJhbnNhY3Rpb25IYXNoIjoiMHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidHJhbnNhY3Rpb25JbmRleCI6MCwiYmxvY2tIYXNoIjoiMHg5ZGZmNDY1YmUwNDc1MmI3Njg1YTZhZjUwYzliZDU2ODE5ODVhYzZhZTg3NjNhYTBmNGQzNzc2MzMyNDhkZDQ2IiwibG9nSW5kZXgiOjEzfQ==",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHg5MWQxOGU1NERBZjRGNjc3Y0IyODE2NzE1OGQ2ZGQyMUY2YUIzOTIxIiwidG9waWNzIjpbIjB4ZGRmMjUyYWQxYmUyYzg5YjY5YzJiMDY4ZmMzNzhkYWE5NTJiYTdmMTYzYzRhMTE2MjhmNTVhNGRmNTIzYjNlZiIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMCJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUt6c1lMRkprcz0iLCJibG9ja051bWJlciI6MjExNTY2MSwidHJhbnNhY3Rpb25IYXNoIjoiMHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwIiwidHJhbnNhY3Rpb25JbmRleCI6MCwiYmxvY2tIYXNoIjoiMHg5ZGZmNDY1YmUwNDc1MmI3Njg1YTZhZjUwYzliZDU2ODE5ODVhYzZhZTg3NjNhYTBmNGQzNzc2MzMyNDhkZDQ2IiwibG9nSW5kZXgiOjE0fQ==",
                            "index": true
                        },
                        {
                            "key": "dHhMb2c=",
                            "value": "eyJhZGRyZXNzIjoiMHg5MWQxOGU1NERBZjRGNjc3Y0IyODE2NzE1OGQ2ZGQyMUY2YUIzOTIxIiwidG9waWNzIjpbIjB4OWZmYmZmYzA0YTM5NzQ2MGVlMWRiZThjOTUwM2UwOTgwOTA1NjdkNmI3ZjRiM2MwMmE4NjE3ZDgwMGI2ZDk1NSIsIjB4MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzOCJdLCJkYXRhIjoiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFJQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFyT3hnc1VtU3dBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFIVDIyU0x3UllBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFJQUFBQUFBQUFBQUFBQUFBQUlvQnlZZzNiVnp0RXVkQWJrYUZWUHM0amdodCIsImJsb2NrTnVtYmVyIjoyMTE1NjYxLCJ0cmFuc2FjdGlvbkhhc2giOiIweDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLCJ0cmFuc2FjdGlvbkluZGV4IjowLCJibG9ja0hhc2giOiIweDlkZmY0NjViZTA0NzUyYjc2ODVhNmFmNTBjOWJkNTY4MTk4NWFjNmFlODc2M2FhMGY0ZDM3NzYzMzI0OGRkNDYiLCJsb2dJbmRleCI6MTV9",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "message",
                    "attributes": [
                        {
                            "key": "bW9kdWxl",
                            "value": "ZnVuZ2libGU=",
                            "index": true
                        },
                        {
                            "key": "c2VuZGVy",
                            "value": "MHg3MzViMTRCQjc5NDYzMzA3QUFjQkVEODZEQWYzMzIyQjFlNjIyNmFC",
                            "index": true
                        },
                        {
                            "key": "dHhUeXBl",
                            "value": "ODg=",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "crosschain/ZrcWithdrawCreated",
                    "attributes": [
                        {
                            "key": "Q2N0eEluZGV4",
                            "value": "MHg4NmY2MDg4YTVhMTI0MWMyMWU5NGJhMGZiZmJkYmYwMDk2OTVjNTBjZmRhOWY4ODk2M2I4MWZiZWNhNGViMjA3",
                            "index": true
                        },
                        {
                            "key": "U2VuZGVy",
                            "value": "MHg3MUVjNWMwNUFhNjY5YzQ5MjI1NjljMUQzM0Y3YTgxYWFhMjE4MTM4",
                            "index": true
                        },
                        {
                            "key": "U2VuZGVyQ2hhaW4=",
                            "value": "WkVUQQ==",
                            "index": true
                        },
                        {
                            "key": "SW5UeE9ic2VydmVkSGFzaA==",
                            "value": "MHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw",
                            "index": true
                        },
                        {
                            "key": "UmVjZWl2ZXI=",
                            "value": "MHgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDA4YTAxYzk4ODM3NmQ1Y2VkMTJlNzQwNmU0Njg1NTRmYjM4OGUwODZk",
                            "index": true
                        },
                        {
                            "key": "UmVjZWl2ZXJDaGFpbg==",
                            "value": "R09FUkxJ",
                            "index": true
                        },
                        {
                            "key": "WmV0YUJ1cm50",
                            "value": "NzYwNTI0OTM3OTYzMDgz",
                            "index": true
                        },
                        {
                            "key": "TmV3U3RhdHVz",
                            "value": "UGVuZGluZ091dGJvdW5k",
                            "index": true
                        },
                        {
                            "key": "TG9nSWRlbnRpZmllcnM=",
                            "value": "MHg3MUVjNWMwNUFhNjY5YzQ5MjI1NjljMUQzM0Y3YTgxYWFhMjE4MTM4LVpFVEEtR09FUkxJLTA=",
                            "index": true
                        }
                    ]
                },
                {
                    "type": "message",
                    "attributes": [
                        {
                            "key": "bW9kdWxl",
                            "value": "emV0YWNvcmU=",
                            "index": true
                        },
                        {
                            "key": "YWN0aW9u",
                            "value": "ZGVwb3NpdFpSQzRBbmRDYWxsQ29udHJhY3Q=",
                            "index": true
                        },
                        {
                            "key": "Y29udHJhY3Q=",
                            "value": "MHg3MUVjNWMwNUFhNjY5YzQ5MjI1NjljMUQzM0Y3YTgxYWFhMjE4MTM4",
                            "index": true
                        },
                        {
                            "key": "ZGF0YQ==",
                            "value": "MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwOTFkMThlNTRkYWY0ZjY3N2NiMjgxNjcxNThkNmRkMjFmNmFiMzkyMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDhhMDFjOTg4Mzc2ZDVjZWQxMmU3NDA2ZTQ2ODU1NGZiMzg4ZTA4NmQwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw",
                            "index": true
                        },
                        {
                            "key": "Y2N0eEluZGV4",
                            "value": "MHg0MmRmNzM0MmZkOGE2MDlhOTdmZWJjNWZkZDcwMTNhZDA4NTg5ZWJhYTQ4MmQ3OGE1ZDhlMGMxOGYyYjEyZTY4",
                            "index": true
                        }
                    ]
                }
            ],
            "codespace": ""
        },
        "tx": "CtEECs4ECjkvemV0YWNoYWluLnpldGFjb3JlLmNyb3NzY2hhaW4uTXNnVm90ZU9uT2JzZXJ2ZWRJbmJvdW5kVHgSkAQKK3pldGExa2s5anF3dWZoY2V2ZWFrY2FqdjMwd2hqNjhnMjI4ZGNjczJ4ZTUSKjB4OEEwMWM5ODgzNzZkNWNFZDEyZTc0MDZFNDY4NTU0ZmIzODhFMDg2RBoKQlNDVEVTVE5FVCIqMHg4QTAxYzk4ODM3NmQ1Y0VkMTJlNzQwNkU0Njg1NTRmYjM4OEUwODZEKgRaRVRBMhEzNTAwMDAwMDAwMDAwMDAwMELoATcxZWM1YzA1YWE2NjljNDkyMjU2OWMxZDMzZjdhODFhYWEyMTgxMzgwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDA5MWQxOGU1NGRhZjRmNjc3Y2IyODE2NzE1OGQ2ZGQyMWY2YWIzOTIxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwOGEwMWM5ODgzNzZkNWNlZDEyZTc0MDZlNDY4NTU0ZmIzODhlMDg2ZDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDBKQjB4MzE1ZjYwMjlmMWFkOTliNmY0NTAwNTIzYjY3ZGU2N2U3YjM2ZDFlNWY3MzhmMmY1OThjYjVmMDEyNTVjNGExMlClzMwNWJC/BWABaioweDhBMDFjOTg4Mzc2ZDVjRWQxMmU3NDA2RTQ2ODU1NGZiMzg4RTA4NkQSbApTCkYKHy9jb3Ntb3MuY3J5cHRvLnNlY3AyNTZrMS5QdWJLZXkSIwohAyHsLaSbjnESa6q9T6VdUOsSSRCwM5A3+Ug87UNXVR1TEgQKAggBGO352wYSFQoOCgVhemV0YRIFNDAwMDAQgK3iBBpA5EMrP5XldumJcX0bU+TlFETxp/eFsD/oZy/J/PZzsjsHB0C5fU1LCHqhIVKDhKnnk2Nc8UORMGdKufufsWkWyg=="
    }
}                 
```
{% endcode %}
