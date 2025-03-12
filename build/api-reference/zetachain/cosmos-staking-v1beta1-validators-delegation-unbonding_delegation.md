---
description: UnbondingDelegation queries unbonding info for given validator delegator pair.
---

# /cosmos/staking/v1beta1/validators/{}/delegation/{}/unbonding\_delegation

#### **Parameters:**

**validator\_address - string**, validator\_address defines the validator address to query for.

**delegator\_address - string**, delegator\_address defines the delegator address to query for.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/cosmos/staking/v1beta1/validators/zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r/delegations/zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84/unbonding_delegation

// Result
{
  "code": 5,
  "message": "rpc error: code = NotFound desc = unbonding delegation with delegator zeta1t4zkm98wf625k7y5ntv850rqzy3rd4a0sv6u84 not found for validator zetavaloper1t4zkm98wf625k7y5ntv850rqzy3rd4a05vzq2r: key not found",
  "details": []
}
```
{% endcode %}
