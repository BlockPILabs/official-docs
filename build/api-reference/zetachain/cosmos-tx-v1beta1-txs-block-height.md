---
description: GetBlockWithTxs fetches a block with decoded txs
---

# /cosmos/tx/v1beta1/txs/block/{height}

#### **Parameters:**

**height- string**, height is the height of the block to query.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/tx/v1beta1/txs/block/{height}

// Result
{
  "txs": [
    {
      "body": {
        "messages": [
          {
            "@type": "string"
          }
        ],
        "memo": "string",
        "timeout_height": "string",
        "extension_options": [
          {
            "@type": "string"
          }
        ],
        "non_critical_extension_options": [
          {
            "@type": "string"
          }
        ]
      },
      "auth_info": {
        "signer_infos": [
          {
            "public_key": {
              "@type": "string"
            },
            "mode_info": {
              "single": {
                "mode": "SIGN_MODE_UNSPECIFIED"
              },
              "multi": {
                "bitarray": {
                  "extra_bits_stored": 0,
                  "elems": "string"
                },
                "mode_infos": [
                  null
                ]
              }
            },
            "sequence": "string"
          }
        ],
        "fee": {
          "amount": [
            {
              "denom": "string",
              "amount": "string"
            }
          ],
          "gas_limit": "string",
          "payer": "string",
          "granter": "string"
        }
      },
      "signatures": [
        "string"
      ]
    }
  ],
  "block_id": {
    "hash": "string",
    "part_set_header": {
      "total": 0,
      "hash": "string"
    }
  },
  "block": {
    "header": {
      "version": {
        "block": "string",
        "app": "string"
      },
      "chain_id": "string",
      "height": "string",
      "time": "2023-03-29T06:47:56.928Z",
      "last_block_id": {
        "hash": "string",
        "part_set_header": {
          "total": 0,
          "hash": "string"
        }
      },
      "last_commit_hash": "string",
      "data_hash": "string",
      "validators_hash": "string",
      "next_validators_hash": "string",
      "consensus_hash": "string",
      "app_hash": "string",
      "last_results_hash": "string",
      "evidence_hash": "string",
      "proposer_address": "string"
    },
    "data": {
      "txs": [
        "string"
      ]
    },
    "evidence": {
      "evidence": [
        {
          "duplicate_vote_evidence": {
            "vote_a": {
              "type": "SIGNED_MSG_TYPE_UNKNOWN",
              "height": "string",
              "round": 0,
              "block_id": {
                "hash": "string",
                "part_set_header": {
                  "total": 0,
                  "hash": "string"
                }
              },
              "timestamp": "2023-03-29T06:47:56.928Z",
              "validator_address": "string",
              "validator_index": 0,
              "signature": "string"
            },
            "vote_b": {
              "type": "SIGNED_MSG_TYPE_UNKNOWN",
              "height": "string",
              "round": 0,
              "block_id": {
                "hash": "string",
                "part_set_header": {
                  "total": 0,
                  "hash": "string"
                }
              },
              "timestamp": "2023-03-29T06:47:56.928Z",
              "validator_address": "string",
              "validator_index": 0,
              "signature": "string"
            },
            "total_voting_power": "string",
            "validator_power": "string",
            "timestamp": "2023-03-29T06:47:56.928Z"
          },
          "light_client_attack_evidence": {
            "conflicting_block": {
              "signed_header": {
                "header": {
                  "version": {
                    "block": "string",
                    "app": "string"
                  },
                  "chain_id": "string",
                  "height": "string",
                  "time": "2023-03-29T06:47:56.928Z",
                  "last_block_id": {
                    "hash": "string",
                    "part_set_header": {
                      "total": 0,
                      "hash": "string"
                    }
                  },
                  "last_commit_hash": "string",
                  "data_hash": "string",
                  "validators_hash": "string",
                  "next_validators_hash": "string",
                  "consensus_hash": "string",
                  "app_hash": "string",
                  "last_results_hash": "string",
                  "evidence_hash": "string",
                  "proposer_address": "string"
                },
                "commit": {
                  "height": "string",
                  "round": 0,
                  "block_id": {
                    "hash": "string",
                    "part_set_header": {
                      "total": 0,
                      "hash": "string"
                    }
                  },
                  "signatures": [
                    {
                      "block_id_flag": "BLOCK_ID_FLAG_UNKNOWN",
                      "validator_address": "string",
                      "timestamp": "2023-03-29T06:47:56.929Z",
                      "signature": "string"
                    }
                  ]
                }
              },
              "validator_set": {
                "validators": [
                  {
                    "address": "string",
                    "pub_key": {
                      "ed25519": "string",
                      "secp256k1": "string"
                    },
                    "voting_power": "string",
                    "proposer_priority": "string"
                  }
                ],
                "proposer": {
                  "address": "string",
                  "pub_key": {
                    "ed25519": "string",
                    "secp256k1": "string"
                  },
                  "voting_power": "string",
                  "proposer_priority": "string"
                },
                "total_voting_power": "string"
              }
            },
            "common_height": "string",
            "byzantine_validators": [
              {
                "address": "string",
                "pub_key": {
                  "ed25519": "string",
                  "secp256k1": "string"
                },
                "voting_power": "string",
                "proposer_priority": "string"
              }
            ],
            "total_voting_power": "string",
            "timestamp": "2023-03-29T06:47:56.929Z"
          }
        }
      ]
    },
    "last_commit": {
      "height": "string",
      "round": 0,
      "block_id": {
        "hash": "string",
        "part_set_header": {
          "total": 0,
          "hash": "string"
        }
      },
      "signatures": [
        {
          "block_id_flag": "BLOCK_ID_FLAG_UNKNOWN",
          "validator_address": "string",
          "timestamp": "2023-03-29T06:47:56.929Z",
          "signature": "string"
        }
      ]
    }
  },
  "pagination": {
    "next_key": "string",
    "total": "string"
  }
}
```
{% endcode %}
