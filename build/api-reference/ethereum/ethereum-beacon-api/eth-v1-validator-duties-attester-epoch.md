# /eth/v1/validator/duties/attester/{epoch}

Requests the beacon node to provide a set of attestation duties, which should be performed by validators, for a particular epoch. Duties should only need to be checked once per epoch, however a chain reorganization (of > MIN\_SEED\_LOOKAHEAD epochs) could occur, resulting in a change of duties. For full safety, you should monitor head events and confirm the dependent root in this response matches:

* event.previous\_duty\_dependent\_root when `compute_epoch_at_slot(event.slot) == epoch`
* event.current\_duty\_dependent\_root when `compute_epoch_at_slot(event.slot) + 1 == epoch`
* event.block otherwise

The dependent\_root value is `get_block_root_at_slot(state, compute_start_slot_at_epoch(epoch - 1) - 1)` or the genesis block root in the case of underflow.

#### Parameters:

**epoch-string,**&#x20;



**Request body:**

An array of the validator indices for which to obtain the duties.

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X POST-H 'Content-Type: application/json' 
https://ethereum-beacon.blockpi.network/rpc/v1/your-rpc-key/eth/v1/validator/duties/attester/274805
‘
[
  "1"
]
’
// Result
{
    "dependent_root": "0x7d319771b89fbe33e7ec458edefbe1074c31d4adb44e87bdbbc11155955a5822",
    "execution_optimistic": false,
    "data": [
        {
            "pubkey": "0xa1d1ad0714035353258038e964ae9675dc0252ee22cea896825c01458e1807bfad2f9969338798548d9858a571f7425c",
            "validator_index": "1",
            "committees_at_slot": "64",
            "committee_index": "59",
            "committee_length": "492",
            "validator_committee_index": "449",
            "slot": "9091219"
        }
    ]
}
```
{% endcode %}
