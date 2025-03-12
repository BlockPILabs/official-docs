---
description: GetBlockByHeight queries block for given height.
---

# /cosmos/base/tendermint/v1beta1/blocks/{height}

#### **Parameters:**

**height-string,** block height

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/base/tendermint/v1beta1/blocks/2053617

// Result
{
    "block_id": {
        "hash": "XnjqWfVER1vXDaQWt+NltWe1QFpjU+ohrUy/CwpOhGo=",
        "part_set_header": {
            "total": 1,
            "hash": "nvvNR5SFLSnQORkJnyA+JDer0OGWJ9SahW0G8eGZgek="
        }
    },
    "block": {
        "header": {
            "version": {
                "block": "11",
                "app": "0"
            },
            "chain_id": "athens_7001-1",
            "height": "2053617",
            "time": "2023-03-27T07:37:13.148246033Z",
            "last_block_id": {
                "hash": "NVjqZL70NusrT0t8CDMGDlz81R7z0tT1WEC1/2V1mIE=",
                "part_set_header": {
                    "total": 2,
                    "hash": "yvdEe0UhG4OTBAbaMKJbASqgeD5evvK1bDt+TXXDzYA="
                }
            },
            "last_commit_hash": "O30gAwkd+jxk0odK7oA513MlvLyOEbRqaoc1OxDVcY0=",
            "data_hash": "nQ0kfpJBF/yYGWmUAl5kFdX3AKqqFmmD2E3EooBRs/o=",
            "validators_hash": "1nMqMNTtp6cbdZH0WUasrKzh41tkw6AwNPFKtbGWFSk=",
            "next_validators_hash": "1nMqMNTtp6cbdZH0WUasrKzh41tkw6AwNPFKtbGWFSk=",
            "consensus_hash": "2XYFHxYg0ViArdTG4tVb4szm+pZCb2vZjS9L6A2Afao=",
            "app_hash": "PdEI6HBX7yItuRHDcm7D1ly1wa1A6hkN1Y8BxtE+VUg=",
            "last_results_hash": "7h3PafGbYkHp7v7JKocAsxRM0Ap+tSz1PfD6F3DJA4I=",
            "evidence_hash": "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
            "proposer_address": "DOd6ZkImkhhfTufa/CEtKiKUu64="
        },
        "data": {
            "txs": [
                "CtAECs0ECjkvemV0YWNoYWluLnpldGFjb3JlLmNyb3NzY2hhaW4uTXNnVm90ZU9uT2JzZXJ2ZWRJbmJvdW5kVHgSjwQKK3pldGExNmMwd3R3ZXoyNzM2eHNoaGE2N2ZmOWc4N2M4bmg1OHc5Mm1lZWsSKjB4RkFDM0JiMUFFQmZFMGNjNGFENzREQTMxODlFQjNkYWJjOTYzMEYwNxoGTVVNQkFJIioweEZBQzNCYjFBRUJmRTBjYzRhRDc0REEzMTg5RUIzZGFiYzk2MzBGMDcqBFpFVEEyFDM1MTMxNDAxODk5MTg4MTEzODk5QugBNzFlYzVjMDVhYTY2OWM0OTIyNTY5YzFkMzNmN2E4MWFhYTIxODEzODAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDEzYTBjNTkzMGMwMjg1MTFkYzAyNjY1ZTcyODUxMzRiNmQxMWE1ZjQwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDBmYWMzYmIxYWViZmUwY2M0YWQ3NGRhMzE4OWViM2RhYmM5NjMwZjA3MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMEpCMHg1ODg5YzI5NmM1ZmU5MzI1M2I5NDY0ZDc2NDkwNWE2NjY1ZWUxZGMwOGFlYTlhNzJjZjJmYTNhYWFlYWVjNjFlUJqUhBBYkL8FYAFqKjB4RkFDM0JiMUFFQmZFMGNjNGFENzREQTMxODlFQjNkYWJjOTYzMEYwNxJsClMKRgofL2Nvc21vcy5jcnlwdG8uc2VjcDI1NmsxLlB1YktleRIjCiEDvfhUl0K4fLH/9XlgY6uu6RtUUq7BBDk4VRXH7ovMoXYSBAoCCAEYrMykBxIVCg4KBWF6ZXRhEgU0MDAwMBCAreIEGkD6NHCRP4sz/NK1GK1BdLo0U0MwvjjE848qOI0CPsdywSsCTYvh9PdrRCKNPjumtH2lq36oViqUqHgNMSfC5VQb",
                ......
                ]
        },
        "evidence": {
            "evidence": []
        },
        "last_commit": {
            "height": "2053616",
            "round": 0,
            "block_id": {
                "hash": "NVjqZL70NusrT0t8CDMGDlz81R7z0tT1WEC1/2V1mIE=",
                "part_set_header": {
                    "total": 2,
                    "hash": "yvdEe0UhG4OTBAbaMKJbASqgeD5evvK1bDt+TXXDzYA="
                }
            },
            "signatures": [
                {
                    "block_id_flag": "BLOCK_ID_FLAG_COMMIT",
                    "validator_address": "DOd6ZkImkhhfTufa/CEtKiKUu64=",
                    "timestamp": "2023-03-27T07:37:13.159891681Z",
                    "signature": "Y1iG8xZDG4UFyt3kl6zBflEJsXcxFCmwTyVbF9t8HAlMLcSx474OXSFesqEeYWi56D6oOxFyK7PfpU11+bUUDA=="
                },
                {
                    "block_id_flag": "BLOCK_ID_FLAG_COMMIT",
                    "validator_address": "e6EFKZklmDLqXSN+VtpGVHAGyp0=",
                    "timestamp": "2023-03-27T07:37:13.111480807Z",
                    "signature": "1hL/NGJuvoU1U1HOGErsvFocsj0z652LS7LbjRbuvDrXnciaIgEZ8lUUoCcegAZffo/0MeCdYonLyorWjDtADg=="
                },
                {
                    "block_id_flag": "BLOCK_ID_FLAG_COMMIT",
                    "validator_address": "jVgEve+jnt+kiAYsH2dxglDDZs0=",
                    "timestamp": "2023-03-27T07:37:13.158965307Z",
                    "signature": "BW8Mbcd+TZA7jfUZY00tZ1rpoiyJMS0lDWDSC2AStq94dQKYQva0GdT1EgXe51pH/5LWbcq4n2K/0FUl9rcjDg=="
                },
                {
                    "block_id_flag": "BLOCK_ID_FLAG_COMMIT",
                    "validator_address": "2EkI/cFUmRcCjHcntejXgDYh9XM=",
                    "timestamp": "2023-03-27T07:37:13.148246033Z",
                    "signature": "A5oHBfpWEpGm98GscoNEDWiEUM4dfPjwMJpuo6kIEM4ObEkQyfpwGr3j2e0dV83G3K15mDpeirKv057mLBIrBg=="
                },
                {
                    "block_id_flag": "BLOCK_ID_FLAG_COMMIT",
                    "validator_address": "TcRf4RHQi0eOps7EXeSPm4mzv2I=",
                    "timestamp": "2023-03-27T07:37:13.126295031Z",
                    "signature": "/jfC7V6/oqFNyQ+Xbmc1c/nbWnEwWSKH3BRFgWCRy20sha8A1QeQhuJWqKkTli9roqiH3Z3UqRQIQCoDJR3TDA=="
                },
                {
                    "block_id_flag": "BLOCK_ID_FLAG_COMMIT",
                    "validator_address": "LSdP9IcDQzpGrW+tY24DR7etw/g=",
                    "timestamp": "2023-03-27T07:37:13.135575840Z",
                    "signature": "yXksfdgR0GFm5d/pe96BXAxhZN4avINX5nSq+ZFMn6nPigQD4H1Keu5ZEGLUy8trY5r9rUt/92JqnsQ4qYu/DQ=="
                }
            ]
        }
    }
}
```
{% endcode %}
