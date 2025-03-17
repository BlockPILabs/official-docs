# Estimate gas price



Currently, the gas estimation is handled by taking the median of the last 100,000 transactions If a user wants to prioritize their transaction and is willing to pay, they can pay more than the gas price. If they're willing to wait longer, they can pay less. Note that the gas price moves with the fee market, and should only increase when demand outweighs supply.

If there have been no transactions in the last 100,000 transactions, the price will be 1.

#### **Response Header:**

**X-APTOS-BLOCK-HEIGHT** integer&#x20;

Current block height of the chain

**X-APTOS-CHAIN-ID** integer&#x20;

Chain ID of the current chain

**X-APTOS-EPOCH** integer&#x20;

Current epoch of the chain

**X-APTOS-LEDGER-OLDEST-VERSION** integer&#x20;

Oldest non-pruned ledger version of the chain

**X-APTOS-LEDGER-TIMESTAMPUSEC** integer&#x20;

Current timestamp of the chain

**X-APTOS-LEDGER-VERSION** integer&#x20;

Current ledger version of the chain

**X-APTOS-OLDEST-BLOCK-HEIGHT** integer&#x20;

Oldest non-pruned block height of the chain

#### **Response Body:**

Struct holding the outputs of the estimate gas API

**deprioritized\_gas\_estimate** integer

The deprioritized estimate for the gas unit price

**gas\_estimate** integer required

The current estimate for the gas unit price

**prioritized\_gas\_estimate** integer

The prioritized estimate for the gas unit price

#### Example:

<pre class="language-json" data-overflow="wrap"><code class="lang-json">// Request
curl -X GET -H 'Content-Type: application/json' https://movement.blockpi.network/rpc/v1/your_api_key/v1/estimate_gas_price
<strong>
</strong>
// Result
{
    "deprioritized_gas_estimate": 100,
    "gas_estimate": 100,
    "prioritized_gas_estimate": 150
}
</code></pre>
