# transfer

#### Request Body

action.type: transfer action.destination: address action.amount: string action.asset: number (0) nonce: timestamp(ms) signature: EIP-712 object vaultAddress: (optional)

{% hint style="warning" %}
Exchange endpoint requests require a valid cryptographic **signature** and **nonce**. The signature is generated using the EIP-712 typed data standard. Refer to the [HyperLiquid Python SDK](https://github.com/hyperliquid-dex/hyperliquid-python-sdk) for code examples.
{% endhint %}

#### Returns

Transaction hash confirming the transfer.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/exchange/your-api-key -X POST -H "Content-Type: application/json" --data '{"action":{"type":"transfer"},"nonce":1720000000000,"signature":{}}'

// Result
{"status":"ok","response":{"type":"transfer","data":{}}}
```
{% endcode %}
