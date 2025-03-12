---
description: Return the latest SUI system state object on-chain.
---

# suix\_getLatestSuiSystemState

#### **Parameters:**

None

#### **Returns:**

SuiSystemStateSummary< SuiSystemStateSummary >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "suix_getLatestSuiSystemState",
  "params": []
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "epoch": "418",
        "protocolVersion": "47",
        "systemStateVersion": "2",
        "storageFundTotalObjectStorageRebates": "493790667507600",
        "storageFundNonRefundableBalance": "170913218670418",
        "referenceGasPrice": "750",
        "safeMode": false,
        "safeModeStorageRewards": "0",
        "safeModeComputationRewards": "0",
        "safeModeStorageRebates": "0",
        "safeModeNonRefundableStorageFee": "0",
        "epochStartTimestampMs": "1717435879365",
        "epochDurationMs": "86400000",
        "stakeSubsidyStartEpoch": "20",
        "maxValidatorCount": "150",
        "minValidatorJoiningStake": "30000000000000000",
        "validatorLowStakeThreshold": "20000000000000000",
        "validatorVeryLowStakeThreshold": "15000000000000000",
        "validatorLowStakeGracePeriod": "7",
        "stakeSubsidyBalance": "628398000000000010",
        "stakeSubsidyDistributionCounter": "398",
        "stakeSubsidyCurrentDistributionAmount": "729000000000000",
        "stakeSubsidyPeriodLength": "90",
        "stakeSubsidyDecreaseRate": 1000,
        "totalStake": "8152950675010670705",
        "activeValidators": [
            {
                "suiAddress": "0x11ec7353e9e08ed4ca13b935ad930a2f937112736aec5eedd08c95cc5cd4c264",
                "protocolPubkeyBytes": "gHcc2rJLuqE2EX+S1nvErlvh2CtcMkoTVJieRgH/k8gNEDjQaZ87OkdgmaR1RQjqBKwk5wCiKcMrfjeAwcSnqI4EVKTuWw12Rj6qIhjCqulY+E3y0zCvsgd81MgqTzCs",
                "networkPubkeyBytes": "dJZOTBVNNWT1ga7uHIyb7sqeKyUtD5MeqYLxSFcUXJk=",
                "workerPubkeyBytes": "5zpGGKL8rAT+rvQaKpjiacy8qe9mYGg4sj+XEnBZw4c=",
                "proofOfPossessionBytes": "gypDu173SPf2p8lb92v8h2MICgK6DxNFMrTxoAd4IyiaHd998g7INgqt1bBvwm3p",
                "name": "ComingChat",
                "description": "ComingChat is a SocialFi-based Web3 portal application with #DeFi and #GameFi function",
                "imageUrl": "https://aptoscid.coming.chat/favicon.png",
                "projectUrl": "https://coming.chat/",
                "netAddress": "/dns/sui-mainnet-validator.coming.chat/tcp/8080/http",
                "p2pAddress": "/dns/sui-mainnet-validator.coming.chat/udp/8084",
                "primaryAddress": "/dns/sui-mainnet-validator.coming.chat/udp/8081",
                "workerAddress": "/dns/sui-mainnet-validator.coming.chat/udp/8082",
                "nextEpochProtocolPubkeyBytes": null,
                "nextEpochProofOfPossession": null,
                "nextEpochNetworkPubkeyBytes": null,
                "nextEpochWorkerPubkeyBytes": null,
                "nextEpochNetAddress": null,
                "nextEpochP2pAddress": null,
                "nextEpochPrimaryAddress": null,
                "nextEpochWorkerAddress": null,
                "votingPower": "47",
                "operationCapId": "0x70dcdd67ff1c2fe18c9f2918a5f31de1a9444743e13392b1d31783b91f0aca99",
                "gasPrice": "1000",
                "commissionRate": "800",
                "nextEpochStake": "38595086844703348",
                "nextEpochGasPrice": "1000",
                "nextEpochCommissionRate": "800",
                "stakingPoolId": "0xc0467666f8a8913ad0a8dfd0a4ce9ce813121258524fac13427668af8d70b2f4",
                "stakingPoolActivationEpoch": "0",
                "stakingPoolDeactivationEpoch": null,
                "stakingPoolSuiBalance": "38595086844703348",
                "rewardsPool": "1261889757332731",
                "poolTokenBalance": "36961907342022901",
                "pendingStake": "0",
                "pendingTotalSuiWithdraw": "0",
                "pendingPoolTokenWithdraw": "0",
                "exchangeRatesId": "0x2e25e1f84aa94a70a2db3d1189f8bd3ea87db16ba0679123f5231f7f8c00c67c",
                "exchangeRatesSize": "419"
            },
            ......
```
{% endcode %}
