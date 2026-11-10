# debug\_traceblockbyhash

#### **Parameters:**

**DATA, 32 Bytes** - hash of a block.

**Object** - (optional) Tracer configuration. Supported tracers: `callTracer`.

#### **Returns:**

**Array** - Array of trace results, one per transaction in the block. Each result includes `txHash` and trace output from the specified tracer.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl https://elysium.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"debug_traceBlockByHash","params":["0xd0eec69c7e7de05ba0e5202d1c50dffe42d897396637d35ee169bbb9fa55cf5f",{"tracer":"callTracer"}],"id":1}'

// Result
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "txHash": "0xa81a13a67e2525f764a7af306659c17c83d8294cc3880cf3f7d756cded2fc4bb",
      "result": {
        "beforeEVMTransfers": [],
        "afterEVMTransfers": [],
        "from": "0x00000000000000000000000000000000000a4b05",
        "gas": "0x0",
        "gasUsed": "0x0",
        "to": "0x00000000000000000000000000000000000a4b05",
        "input": "0x6bf6a42d00000000000000000000000000000000000000000000000000...",
        "calls": [
          {
            "from": "0xfffffffffffffffffffffffffffffffffffffffe",
            "gas": "0x1c9c380",
            "gasUsed": "0x212c",
            "to": "0x0000f90827f1c53a10cb7a02335b175320002935",
            "input": "0x56eb280f4d67f9d971cf16aad7df2870167c0300428fbc14cd3ec5d419d87674",
            "calls": [
              {
                "from": "0x0000f90827f1c53a10cb7a02335b175320002935",
                "gas": "0x1c29238",
                "gasUsed": "0x323",
                "to": "0x0000000000000000000000000000000000000064",
                "input": "0xa3b1b31d",
                "output": "0x000000000000000000000000000000000000000000000000000000000037a200",
                "type": "STATICCALL"
              }
            ],
            "value": "0x0",
            "type": "CALL"
          }
        ],
        "value": "0x0",
        "type": "CALL"
      }
    },
    {
      "txHash": "0xc6ed0a1582d665eca7f4d61f87d9ec72c58b6643ec864af2b6ed8dd665356a03",
      "result": {
        "beforeEVMTransfers": [
          {
            "purpose": "feePayment",
            "from": "0x148dDcEfd47234B60d4fe0463F7497ef7a71A27b",
            "to": null,
            "value": "0x1118ecd0e3800"
          }
        ],
        "afterEVMTransfers": [
          {
            "purpose": "gasRefund",
            "from": null,
            "to": "0x148dDcEfd47234B60d4fe0463F7497ef7a71A27b",
            "value": "0xced9ca48e540"
          },
          {
            "purpose": "tip",
            "from": null,
            "to": "0x6CBb552855CE5Eb70af49B76a8048be8E3799A05",
            "value": "0x2c7dc8a09020"
          },
          "..."
        ],
        "from": "0x148ddcefd47234b60d4fe0463f7497ef7a71a27b",
        "gas": "0x30d40",
        "gasUsed": "0xbe82",
        "to": "0x063f7cc5339f92a5fd7baf3d22233044fda1f327",
        "input": "0x095ea7b3000000000000000000000000ca0d2b3047e547fd256c325db04634fa923aab52000000000000000000000000000000000000000000000d51097a8a84d0836dc5",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000001",
        "calls": [
          {
            "from": "0x063f7cc5339f92a5fd7baf3d22233044fda1f327",
            "gas": "0x2a386",
            "gasUsed": "0x5f5c",
            "to": "0x10b0292fb853966d3039d80bbef98b1a9507f55f",
            "input": "0x095ea7b3000000000000000000000000ca0d2b3047e547fd256c325db04634fa923aab52000000000000000000000000000000000000000000000d51097a8a84d0836dc5",
            "output": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "value": "0x0",
            "type": "DELEGATECALL"
          }
        ],
        "value": "0x0",
        "type": "CALL"
      }
    },
    "..."
  ]
}
```
{% endcode %}
