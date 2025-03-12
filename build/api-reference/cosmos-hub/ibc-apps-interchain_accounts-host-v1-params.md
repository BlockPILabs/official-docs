---
description: Params queries all parameters of the ICA host submodule.
---

# /ibc/apps/interchain\_accounts/host/v1/params

#### **Parameters:**

None

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://cosmos-lcd.blockpi.network/cosmos/<your-api-key>/v1/ibc/apps/interchain_accounts/host/v1/params

// Result
{
    "params": {
        "host_enabled": true,
        "allow_messages": [
            "/cosmos.authz.v1beta1.MsgExec",
            "/cosmos.authz.v1beta1.MsgGrant",
            "/cosmos.authz.v1beta1.MsgRevoke",
            "/cosmos.bank.v1beta1.MsgSend",
            "/cosmos.bank.v1beta1.MsgMultiSend",
            "/cosmos.distribution.v1beta1.MsgSetWithdrawAddress",
            "/cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission",
            "/cosmos.distribution.v1beta1.MsgFundCommunityPool",
            "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward",
            "/cosmos.feegrant.v1beta1.MsgGrantAllowance",
            "/cosmos.feegrant.v1beta1.MsgRevokeAllowance",
            "/cosmos.gov.v1beta1.MsgVoteWeighted",
            "/cosmos.gov.v1beta1.MsgSubmitProposal",
            "/cosmos.gov.v1beta1.MsgDeposit",
            "/cosmos.gov.v1beta1.MsgVote",
            "/cosmos.staking.v1beta1.MsgEditValidator",
            "/cosmos.staking.v1beta1.MsgDelegate",
            "/cosmos.staking.v1beta1.MsgUndelegate",
            "/cosmos.staking.v1beta1.MsgBeginRedelegate",
            "/cosmos.staking.v1beta1.MsgCreateValidator",
            "/cosmos.vesting.v1beta1.MsgCreateVestingAccount",
            "/ibc.applications.transfer.v1.MsgTransfer",
            "/tendermint.liquidity.v1beta1.MsgCreatePool",
            "/tendermint.liquidity.v1beta1.MsgSwapWithinBatch",
            "/tendermint.liquidity.v1beta1.MsgDepositWithinBatch",
            "/tendermint.liquidity.v1beta1.MsgWithdrawWithinBatch"
        ]
    }
}
```
{% endcode %}
