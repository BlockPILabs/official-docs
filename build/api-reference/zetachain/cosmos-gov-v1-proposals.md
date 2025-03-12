---
description: Proposals queries all proposals based on given status.
---

# /cosmos/gov/v1/proposals

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/gov/v1/proposals

// Result
{
  "proposals": [
    {
      "proposal_id": "1",
      "content": {
        "@type": "/cosmos.upgrade.v1beta1.SoftwareUpgradeProposal",
        "title": "v2.0.0",
        "description": "Zeta Release v2.0.0",
        "plan": {
          "name": "v2.0.0",
          "time": "0001-01-01T00:00:00Z",
          "height": "392589",
          "info": "{\"binaries\": {\"zetacored-linux/amd64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetacored-ubuntu-22-amd64?checksum=sha256:fecaece4530c7358a3f331bb3461c7903614189250964b34bdb60eba113d8a77\",\"zetacored-linux/arm64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetacored-ubuntu-22-arm64?checksum=sha256:324988e195e4d0b5233bed43568fbf9ef7ccc1bdef3a7a73174075be366a8b3a\",\"zetaclientd-linux/amd64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetaclientd-ubuntu-22-arm64?checksum=sha256:94c8cc0171da3b6300ae7a43337496742e29628c249e84a6ef4041e7e4b520f2\",\"zetaclientd-linux/arm64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetaclientd-ubuntu-22-amd64?checksum=sha256:f36f070e7636ce36e66f230996491fab370d4f4084b5bcadc22cbd5cd547b701\"}}",
          "upgraded_client_state": null
        }
      },
      "status": "PROPOSAL_STATUS_FAILED",
      "final_tally_result": {
        "yes": "11890200000000000000000",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-19T16:45:07.743798724Z",
      "deposit_end_time": "2023-06-21T16:45:07.743798724Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-19T16:45:07.743798724Z",
      "voting_end_time": "2023-06-19T18:45:07.743798724Z"
    },
    {
      "proposal_id": "2",
      "content": {
        "@type": "/cosmos.upgrade.v1beta1.SoftwareUpgradeProposal",
        "title": "v2.0.0",
        "description": "Zeta Release v2.0.0",
        "plan": {
          "name": "v2.0.0",
          "time": "0001-01-01T00:00:00Z",
          "height": "394563",
          "info": "{\"binaries\": {\"zetacored-linux/amd64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetacored-ubuntu-22-amd64?checksum=sha256:fecaece4530c7358a3f331bb3461c7903614189250964b34bdb60eba113d8a77\",\"zetacored-linux/arm64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetacored-ubuntu-22-arm64?checksum=sha256:324988e195e4d0b5233bed43568fbf9ef7ccc1bdef3a7a73174075be366a8b3a\",\"zetaclientd-linux/amd64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetaclientd-ubuntu-22-arm64?checksum=sha256:94c8cc0171da3b6300ae7a43337496742e29628c249e84a6ef4041e7e4b520f2\",\"zetaclientd-linux/arm64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v2.0.0/zetaclientd-ubuntu-22-amd64?checksum=sha256:f36f070e7636ce36e66f230996491fab370d4f4084b5bcadc22cbd5cd547b701\"}}",
          "upgraded_client_state": null
        }
      },
      "status": "PROPOSAL_STATUS_PASSED",
      "final_tally_result": {
        "yes": "11890200000000000000000",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-19T19:43:03.443287572Z",
      "deposit_end_time": "2023-06-21T19:43:03.443287572Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-19T19:43:03.443287572Z",
      "voting_end_time": "2023-06-19T21:43:03.443287572Z"
    },
    {
      "proposal_id": "3",
      "content": {
        "@type": "/cosmos.params.v1beta1.ParameterChangeProposal",
        "title": "Gov Param Change",
        "description": "Update voting period",
        "changes": [
          {
            "subspace": "gov",
            "key": "votingparams",
            "value": "{\n        \"voting_period\": \"86400\"\n      }"
          },
          {
            "subspace": "gov",
            "key": "depositparams",
            "value": "{\n        \"min_deposit\": [\n          {\n            \"denom\": \"azeta\",\n            \"amount\": \"1000000\"\n          }\n        ],\n        \"max_deposit_period\": \"86400\"\n      }"
          }
        ]
      },
      "status": "PROPOSAL_STATUS_REJECTED",
      "final_tally_result": {
        "yes": "0",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-22T18:52:01.825961684Z",
      "deposit_end_time": "2023-06-24T18:52:01.825961684Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "11000000"
        }
      ],
      "voting_start_time": "2023-06-22T18:54:46.590912540Z",
      "voting_end_time": "2023-06-22T20:54:46.590912540Z"
    },
    {
      "proposal_id": "4",
      "content": {
        "@type": "/cosmos.params.v1beta1.ParameterChangeProposal",
        "title": "Gov Param Change",
        "description": "Update voting period",
        "changes": [
          {
            "subspace": "gov",
            "key": "votingparams",
            "value": "{         \"voting_period\": \"86400\"       }"
          },
          {
            "subspace": "gov",
            "key": "depositparams",
            "value": "{         \"min_deposit\": [           {             \"denom\": \"azeta\",             \"amount\": \"1000000\"           }         ],         \"max_deposit_period\": \"86400\"       }"
          }
        ]
      },
      "status": "PROPOSAL_STATUS_REJECTED",
      "final_tally_result": {
        "yes": "0",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-22T19:12:58.791540437Z",
      "deposit_end_time": "2023-06-24T19:12:58.791540437Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-22T19:12:58.791540437Z",
      "voting_end_time": "2023-06-22T21:12:58.791540437Z"
    },
    {
      "proposal_id": "5",
      "content": {
        "@type": "/cosmos.params.v1beta1.ParameterChangeProposal",
        "title": "Gov Param Change",
        "description": "Update voting period",
        "changes": [
          {
            "subspace": "gov",
            "key": "votingparams",
            "value": "{         \"voting_period\": \"86400\"       }"
          },
          {
            "subspace": "gov",
            "key": "depositparams",
            "value": "{         \"min_deposit\": [           {             \"denom\": \"azeta\",             \"amount\": \"1000000\"           }         ],         \"max_deposit_period\": \"86400\"       }"
          }
        ]
      },
      "status": "PROPOSAL_STATUS_REJECTED",
      "final_tally_result": {
        "yes": "0",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-22T19:16:23.182328658Z",
      "deposit_end_time": "2023-06-24T19:16:23.182328658Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-22T19:16:23.182328658Z",
      "voting_end_time": "2023-06-22T21:16:23.182328658Z"
    },
    {
      "proposal_id": "6",
      "content": {
        "@type": "/cosmos.params.v1beta1.ParameterChangeProposal",
        "title": "Gov Param Change",
        "description": "Update voting period",
        "changes": [
          {
            "subspace": "gov",
            "key": "votingparams",
            "value": "{         \"voting_period\": \"86400\"       }"
          },
          {
            "subspace": "gov",
            "key": "depositparams",
            "value": "{         \"min_deposit\": [           {             \"denom\": \"azeta\",             \"amount\": \"1000000\"           }         ],         \"max_deposit_period\": \"86400\"       }"
          }
        ]
      },
      "status": "PROPOSAL_STATUS_REJECTED",
      "final_tally_result": {
        "yes": "0",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-22T22:21:12.889209729Z",
      "deposit_end_time": "2023-06-24T22:21:12.889209729Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-22T22:21:12.889209729Z",
      "voting_end_time": "2023-06-23T00:21:12.889209729Z"
    },
    {
      "proposal_id": "7",
      "content": {
        "@type": "/cosmos.params.v1beta1.ParameterChangeProposal",
        "title": "Gov Param Change",
        "description": "Update voting period",
        "changes": [
          {
            "subspace": "gov",
            "key": "votingparams",
            "value": "{         \"voting_period\": \"86400\"       }"
          },
          {
            "subspace": "gov",
            "key": "depositparams",
            "value": "{         \"min_deposit\": [           {             \"denom\": \"azeta\",             \"amount\": \"1000000\"           }         ],         \"max_deposit_period\": \"86400\"       }"
          }
        ]
      },
      "status": "PROPOSAL_STATUS_REJECTED",
      "final_tally_result": {
        "yes": "0",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-22T22:28:53.480668193Z",
      "deposit_end_time": "2023-06-24T22:28:53.480668193Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-22T22:28:53.480668193Z",
      "voting_end_time": "2023-06-23T00:28:53.480668193Z"
    },
    {
      "proposal_id": "8",
      "content": {
        "@type": "/cosmos.params.v1beta1.ParameterChangeProposal",
        "title": "Gov Param Change",
        "description": "Update voting period",
        "changes": [
          {
            "subspace": "gov",
            "key": "votingparams",
            "value": "{         \"voting_period\": \"86400\"       }"
          },
          {
            "subspace": "gov",
            "key": "depositparams",
            "value": "{         \"min_deposit\": [           {             \"denom\": \"azeta\",             \"amount\": \"1000000\"           }         ],         \"max_deposit_period\": \"86400\"       }"
          }
        ]
      },
      "status": "PROPOSAL_STATUS_REJECTED",
      "final_tally_result": {
        "yes": "0",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-22T22:41:30.271998385Z",
      "deposit_end_time": "2023-06-24T22:41:30.271998385Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-22T22:41:30.271998385Z",
      "voting_end_time": "2023-06-23T00:41:30.271998385Z"
    },
    {
      "proposal_id": "9",
      "content": {
        "@type": "/cosmos.params.v1beta1.ParameterChangeProposal",
        "title": "Gov Param Change",
        "description": "Update voting period",
        "changes": [
          {
            "subspace": "gov",
            "key": "votingparams",
            "value": "{         \"voting_period\": \"86400\"       }"
          },
          {
            "subspace": "gov",
            "key": "depositparams",
            "value": "{         \"min_deposit\": [           {             \"denom\": \"azeta\",             \"amount\": \"1000000\"           }         ],         \"max_deposit_period\": \"86400\"       }"
          }
        ]
      },
      "status": "PROPOSAL_STATUS_REJECTED",
      "final_tally_result": {
        "yes": "0",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-22T22:50:48.410680710Z",
      "deposit_end_time": "2023-06-24T22:50:48.410680710Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-22T22:50:48.410680710Z",
      "voting_end_time": "2023-06-23T00:50:48.410680710Z"
    },
    {
      "proposal_id": "10",
      "content": {
        "@type": "/cosmos.params.v1beta1.ParameterChangeProposal",
        "title": "Gov Param Change",
        "description": "Update voting period",
        "changes": [
          {
            "subspace": "gov",
            "key": "votingparams",
            "value": "{\"voting_period\":\"86400\"}"
          },
          {
            "subspace": "gov",
            "key": "depositparams",
            "value": "{\"min_deposit\":[{\"denom\":\"azeta\",\"amount\":\"1000000\"}],\"max_deposit_period\":\"86400\"}"
          }
        ]
      },
      "status": "PROPOSAL_STATUS_REJECTED",
      "final_tally_result": {
        "yes": "0",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-22T23:50:35.859117310Z",
      "deposit_end_time": "2023-06-24T23:50:35.859117310Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-22T23:50:35.859117310Z",
      "voting_end_time": "2023-06-23T01:50:35.859117310Z"
    },
    {
      "proposal_id": "11",
      "content": {
        "@type": "/cosmos.params.v1beta1.ParameterChangeProposal",
        "title": "Gov Param Change",
        "description": "Update voting period",
        "changes": [
          {
            "subspace": "gov",
            "key": "votingparams",
            "value": "{         \"voting_period\": \"86400000000000\"       }"
          },
          {
            "subspace": "gov",
            "key": "depositparams",
            "value": "{         \"min_deposit\": [           {             \"denom\": \"azeta\",             \"amount\": \"1000000\"           }         ],         \"max_deposit_period\": \"86400000000000\"       }"
          }
        ]
      },
      "status": "PROPOSAL_STATUS_PASSED",
      "final_tally_result": {
        "yes": "728940000000000000000030",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-23T16:37:45.270151273Z",
      "deposit_end_time": "2023-06-25T16:37:45.270151273Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-23T16:37:45.270151273Z",
      "voting_end_time": "2023-06-23T18:37:45.270151273Z"
    },
    {
      "proposal_id": "12",
      "content": {
        "@type": "/cosmos.upgrade.v1beta1.SoftwareUpgradeProposal",
        "title": "v3.0.0",
        "description": "Features:\\n - Generated spec from source.\\n - Implemented Stress test final.\\n - Added GH action for basic operations on athens3 validator nodes in CI.\\n - Added/refactored port 8123 telemetry in zetaclient.\\n - Added automatic stop in zetaclient at upgrade height when an upgrade plan is detected.\\n - Added flag for test keysign.\\n",
        "plan": {
          "name": "v3.0.0",
          "time": "0001-01-01T00:00:00Z",
          "height": "515000",
          "info": "{\"binaries\": {\"zetacored-linux/amd64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v3.0.0/zetacored-ubuntu-22-amd64?checksum=sha256:47210461f4c39a1ce566f6493fd09d8ad3bbba191ccf1c3493fc2c28905e1cff\",\"zetacored-linux/arm64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v3.0.0/zetacored-ubuntu-22-arm64?checksum=sha256:b80585715ce73eeb05591bcd2be5618543a020c30426b921ee00e880d5334b04\",\"zetaclientd-linux/amd64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v3.0.0/zetaclientd-ubuntu-22-amd64?checksum=sha256:dddd22c92099975d7c1d76faecefab4c757212935da61d6ea2780ef70d33e457\",\"zetaclientd-linux/arm64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v3.0.0/zetaclientd-ubuntu-22-arm64?checksum=sha256:7f27477dd96c0511492476fada2ecc584037bbffc3d8ffa32d1c527e2860a72d\"}}",
          "upgraded_client_state": null
        }
      },
      "status": "PROPOSAL_STATUS_REJECTED",
      "final_tally_result": {
        "yes": "91595300008659869719818",
        "abstain": "0",
        "no": "891188711108768066163176",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-26T18:02:21.567571689Z",
      "deposit_end_time": "2023-06-27T18:02:21.567571689Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-26T18:02:21.567571689Z",
      "voting_end_time": "2023-06-27T18:02:21.567571689Z"
    },
    {
      "proposal_id": "13",
      "content": {
        "@type": "/cosmos.upgrade.v1beta1.MsgCancelUpgrade",
        "authority": "zeta10d07y265gmmuvt4z0w9aw880jnsr700jvxasvr"
      },
      "status": "PROPOSAL_STATUS_REJECTED",
      "final_tally_result": {
        "yes": "299500000000011000000",
        "abstain": "0",
        "no": "638430860000000100000030",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-27T15:37:48.660608696Z",
      "deposit_end_time": "2023-06-28T15:37:48.660608696Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "1000000"
        }
      ],
      "voting_start_time": "2023-06-27T15:37:48.660608696Z",
      "voting_end_time": "2023-06-28T15:37:48.660608696Z"
    },
    {
      "proposal_id": "14",
      "content": {
        "@type": "/cosmos.upgrade.v1beta1.SoftwareUpgradeProposal",
        "title": "v3.0.0",
        "description": "Features:\\n - Generated spec from source.\\n - Implemented Stress test final.\\n - Added GH action for basic operations on athens3 validator nodes in CI.\\n - Added/refactored port 8123 telemetry in zetaclient.\\n - Added automatic stop in zetaclient at upgrade height when an upgrade plan is detected.\\n - Added flag for test keysign.\\n",
        "plan": {
          "name": "v3.0.0",
          "time": "0001-01-01T00:00:00Z",
          "height": "532300",
          "info": "{\"binaries\": {\"zetacored-linux/amd64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v3.0.0/zetacored-ubuntu-22-amd64?checksum=sha256:47210461f4c39a1ce566f6493fd09d8ad3bbba191ccf1c3493fc2c28905e1cff\",\"zetacored-linux/arm64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v3.0.0/zetacored-ubuntu-22-arm64?checksum=sha256:b80585715ce73eeb05591bcd2be5618543a020c30426b921ee00e880d5334b04\",\"zetaclientd-linux/amd64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v3.0.0/zetaclientd-ubuntu-22-amd64?checksum=sha256:dddd22c92099975d7c1d76faecefab4c757212935da61d6ea2780ef70d33e457\",\"zetaclientd-linux/arm64\": \"https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/v3.0.0/zetaclientd-ubuntu-22-arm64?checksum=sha256:7f27477dd96c0511492476fada2ecc584037bbffc3d8ffa32d1c527e2860a72d\"}}",
          "upgraded_client_state": null
        }
      },
      "status": "PROPOSAL_STATUS_PASSED",
      "final_tally_result": {
        "yes": "883901701117427926883154",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-27T19:42:58.282307592Z",
      "deposit_end_time": "2023-06-28T19:42:58.282307592Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-27T19:42:58.282307592Z",
      "voting_end_time": "2023-06-28T19:42:58.282307592Z"
    },
    {
      "proposal_id": "15",
      "content": {
        "@type": "/cosmos.params.v1beta1.ParameterChangeProposal",
        "title": "Gov Param Change",
        "description": "Update voting period",
        "changes": [
          {
            "subspace": "gov",
            "key": "votingparams",
            "value": "{\n        \"voting_period\": \"43200000000000\"\n      }"
          },
          {
            "subspace": "gov",
            "key": "depositparams",
            "value": "{\n        \"min_deposit\": [\n          {\n            \"denom\": \"azeta\",\n            \"amount\": \"1000000\"\n          }\n        ],\n        \"max_deposit_period\": \"43200000000000\"\n      }"
          }
        ]
      },
      "status": "PROPOSAL_STATUS_PASSED",
      "final_tally_result": {
        "yes": "921695521117627027894105",
        "abstain": "0",
        "no": "0",
        "no_with_veto": "0"
      },
      "submit_time": "2023-06-29T18:10:53.575671115Z",
      "deposit_end_time": "2023-06-30T18:10:53.575671115Z",
      "total_deposit": [
        {
          "denom": "azeta",
          "amount": "10000000"
        }
      ],
      "voting_start_time": "2023-06-29T18:10:53.575671115Z",
      "voting_end_time": "2023-06-30T18:10:53.575671115Z"
    }
  ],
  "pagination": {
    "next_key": null,
    "total": "15"
  }
}
```
{% endcode %}
