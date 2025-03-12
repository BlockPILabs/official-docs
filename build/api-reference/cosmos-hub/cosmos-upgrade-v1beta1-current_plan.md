---
description: CurrentPlan queries the current upgrade plan.
---

# /cosmos/upgrade/v1beta1/current\_plan

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos.blockpi.network/lcd/v1/<your-api-key>/cosmos/upgrade/v1beta1/current_plan

// Result
{
    "plan": {
        "name": "v8-Rho",
        "time": "0001-01-01T00:00:00Z",
        "height": "14099412",
        "info": "{\"binaries\":{\"linux/amd64\":\"https://github.com/cosmos/gaia/releases/download/v8.0.0/gaiad-v8.0.0-linux-amd64?checksum=sha256:6d0c123e246a8b56ba534f70dd5dc72058b00fd5e5dde5ea40509ff51efc42e2\",\"linux/arm64\":\"https://github.com/cosmos/gaia/releases/download/v8.0.0/gaiad-v8.0.0-linux-arm64?checksum=sha256:a0afbbe35eda3d5e52a7907bcae296415e84b3ff6c7da97429d91f324004a5ab\",\"darwin/amd64\":\"https://github.com/cosmos/gaia/releases/download/v8.0.0/gaiad-v8.0.0-darwin-amd64?checksum=sha256:e66c0e62aa5b0ccf9fb174c50b598df6048c1d7952f5f99b807b9934c9629f2c\",\"darwin/arm64\":\"https://github.com/cosmos/gaia/releases/download/v8.0.0/gaiad-v8.0.0-darwin-arm64?checksum=sha256:95000b52f55f22e1b40b81263bc0ae0df1351e8b9b40264c54509ad1e4d6e9fb\",\"windows/amd64\":\"https://github.com/cosmos/gaia/releases/download/v8.0.0/gaiad-v8.0.0-windows-amd64.exe?checksum=sha256:fca2a4371eef6dc50b6b46a025bde3537fa96ec32c732499c8be8aa64683f147\"}}",
        "upgraded_client_state": null
    }
}
```
{% endcode %}
