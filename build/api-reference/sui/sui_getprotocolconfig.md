---
description: >-
  Return the protocol config table for the given version number. If the version
  number is not specified, If none is specified, the node uses the version of
  the latest epoch it has processed.
---

# sui\_getProtocolConfig

#### **Parameters:**

**version< BigInt\_for\_uint64 >** - An optional protocol version specifier. If omitted, the latest protocol config table for the node will be returned.

#### **Returns:**

ProtocolConfigResponse< ProtocolConfig >

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl  https://sui.blockpi.network/v1/rpc/your-rpc-key -X POST -H "Content-Type: application/json" 
--data 
'{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sui_getProtocolConfig",
  "params": []
}'

// Result
{
    "jsonrpc": "2.0",
    "result": {
        "minSupportedProtocolVersion": "1",
        "maxSupportedProtocolVersion": "47",
        "protocolVersion": "47",
        "featureFlags": {
            "accept_zklogin_in_multisig": true,
            "advance_epoch_start_time_in_safe_mode": true,
            "advance_to_highest_supported_protocol_version": true,
            "allow_receiving_object_id": true,
            "ban_entry_init": true,
            "bridge": false,
            "commit_root_state_digest": true,
            "consensus_order_end_of_epoch_last": true,
            "disable_invariant_violation_check_in_swap_loc": true,
            "disallow_adding_abilities_on_upgrade": true,
            "disallow_change_struct_type_params_on_upgrade": true,
            "enable_coin_deny_list": true,
            "enable_effects_v2": true,
            "enable_group_ops_native_function_msm": false,
            "enable_group_ops_native_functions": true,
            "enable_jwk_consensus_updates": true,
            "enable_poseidon": false,
            "end_of_epoch_transaction_supported": true,
            "hardened_otw_check": true,
            "include_consensus_digest_in_prologue": true,
            "loaded_child_object_format": true,
            "loaded_child_object_format_type": true,
            "loaded_child_objects_fixed": true,
            "missing_type_is_compatibility_error": true,
            "mysticeti_leader_scoring_and_schedule": false,
            "narwhal_certificate_v2": true,
            "narwhal_new_leader_election_schedule": true,
            "narwhal_versioned_metadata": true,
            "no_extraneous_module_bytes": true,
            "package_digest_hash_module": true,
            "package_upgrades": true,
            "random_beacon": false,
            "receive_objects": true,
            "recompute_has_public_transfer_in_execution": true,
            "reject_mutable_random_on_entry_functions": true,
            "reshare_at_same_initial_version": true,
            "scoring_decision_with_validity_cutoff": true,
            "shared_object_deletion": true,
            "simple_conservation_checks": true,
            "simplified_unwrap_then_delete": true,
            "throughput_aware_consensus_submission": false,
            "txn_base_cost_as_multiplier": true,
            "upgraded_multisig_supported": true,
            "verify_legacy_zklogin_address": true,
            "zklogin_auth": true
        },
        "attributes": {
        ......
```
{% endcode %}
