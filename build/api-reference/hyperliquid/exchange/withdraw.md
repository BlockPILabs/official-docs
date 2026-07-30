# withdraw

#### Request Body

action.type: withdraw action.destination: EVM address action.amount: string action.time: timestamp(ms) nonce: timestamp(ms) signature: EIP-712 object

{% hint style="warning" %}
Exchange endpoint requests require a valid cryptographic **signature** and **nonce**. The signature is generated using the EIP-712 typed data standard. Refer to the [HyperLiquid Python SDK](https://github.com/hyperliquid-dex/hyperliquid-python-sdk) for code examples.
{% endhint %}

#### Returns

Transaction hash and withdrawal confirmation.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/exchange/your-api-key -X POST -H "Content-Type: application/json" --data '{"action":{"type":"withdraw"},"nonce":1720000000000,"signature":{}}'

// Result
{"status":"ok","response":{"type":"withdraw","data":{}}}
```
{% endcode %}
