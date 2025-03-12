---
description: Get the latest block
---

# /blocks/latest

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/blocks/latest

// Result
{
    "block_id": {
        "hash": "14FC35931025086863FDDC6286C07A54F3C05E70D19825D658D2A94CCB7FBB5E",
        "parts": {
            "total": 1,
            "hash": "DAED2CA81DCD286ADA8229873DC2E8EC80FAEA7435A81721620F1B5C40EEE475"
        }
    },
    "block": {
        "header": {
            "version": {
                "block": "11"
            },
            "chain_id": "cosmoshub-4",
            "height": "14090818",
            "time": "2023-02-15T08:55:04.699970863Z",
            "last_block_id": {
                "hash": "7035743FEEBE53980DADFCC06E437E557546186AB8907E1E34EAE16B2C614D16",
                "parts": {
                    "total": 1,
                    "hash": "4D98499E391A8EAD6FF845E1DB696BC80D940597E58F0DDDEA452E7271359AA7"
                }
            },
            "last_commit_hash": "EC7E64537856B13D54E8CFCAA6E77E9AC04ED2C6F308F4B8BCBB60778408F5EC",
            "data_hash": "1DE0902AEE02661F8F53086E57CC9EBF24C6D7520CF39744B40263133E98E9D4",
            "validators_hash": "D13B51B540D39BEFC109F96B20081EC93CB46766359AEB463F9DFD011BC6E369",
            "next_validators_hash": "D13B51B540D39BEFC109F96B20081EC93CB46766359AEB463F9DFD011BC6E369",
            "consensus_hash": "80364965B7C2CC9DE961C0998B47A7F93F1970077EB882E0ED1C3822408888C7",
            "app_hash": "62DD15D9C1645E1C852D9F7537FF189318719C17966653B578EA9CECD6E98E96",
            "last_results_hash": "8932AB9A9948A97D9EE2C3E95594F073C71D1D99467AB82ED5AE837B84A4CC2F",
            "evidence_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
            "proposer_address": "F59734A896A7689436BC3422244FD862AE189C5C"
        },
        "data": {
            "txs": [
                "CrgBCp4BCiMvY29zbW9zLnN0YWtpbmcudjFiZXRhMS5Nc2dEZWxlZ2F0ZRJ3Ci1jb3Ntb3MxdjdnOHA3anp6bmp4M2d2M2UwNXdxeTl0NjczYTR1d214bjlxNHASNGNvc21vc3ZhbG9wZXIxdGZsazMwbXE1dmdxamRseTkya2toaHEzcmFldjJobno2ZWV0ZTMaEAoFdWF0b20SBzE1NTMyMjgSFURlbGVnYXRlZCB3aXRoIEV4b2R1cxJnClAKRgofL2Nvc21vcy5jcnlwdG8uc2VjcDI1NmsxLlB1YktleRIjCiEClnsIVYPnxPOStPFjUt4uSaplp5KdGaf761+/+OfQfXISBAoCCAEYGBITCg0KBXVhdG9tEgQ3MDAwEMCLERpAsGbrWq0jUpxKpdHOSlxzj+Vo61HIqTl7buCFiMTQRlwvkfCxnPNvsRtCGhn7GPvOtAdXD+ZVeJ0OsR+KaoHTWQ=="
            ]
        },
        "evidence": {
            "evidence": []
        },
        "last_commit": {
            "height": "14090817",
            "round": 0,
            "block_id": {
                "hash": "7035743FEEBE53980DADFCC06E437E557546186AB8907E1E34EAE16B2C614D16",
                "parts": {
                    "total": 1,
                    "hash": "4D98499E391A8EAD6FF845E1DB696BC80D940597E58F0DDDEA452E7271359AA7"
                }
            },
            "signatures": [
                {
                    "block_id_flag": 2,
                    "validator_address": "AC2D56057CD84765E6FBE318979093E8E44AA18F",
                    "timestamp": "2023-02-15T08:55:04.66178963Z",
                    "signature": "ngSg9Q3lTQgQ5SWjWf285bcaIfapZzpV0h3ghN34l4UjNyDXu05mrH/1cAmWtPUIPxGhgrSC6wdmPkXf6lS/Ag=="
                },
            ]
        }
    }
}
```
{% endcode %}
