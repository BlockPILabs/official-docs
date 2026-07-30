# userFees

#### Parameters

type: userFees user: address (42-char hex)

#### Returns

Fee schedule and recent fee breakdown.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"userFees","user":"0x563d3f4e57a4982f8cec0d3eaf47c5e6dbbaf337"}'

// Result
{"dailyUserVlm":[{"date":"2026-07-16","userCross":"0.0","userAdd":"0.0","exchange":"4505319687.5200004578"},{"date":"2026-07-17","userCross":"0.0","userAdd":"0.0","exchange":"4709850328.6300001144"},{"date":"2026-07-18","userCross":"0.0","userAdd":"0.0","exchange":"1751223474.0899999142"},{"date":"2026-07-19","userCross":"0.0","userAdd":"0.0","exchange":"1899526098.25"},{"date":"2026-07-20","userCross":"0.0","userAdd":"0.0","exchange":"5228174371.25"},{"date":"2026-07-21","userCross":"0.0","userAdd":"0.0","exchange":"4451931406.6899995804"},{"date":"2026-07-22","userCross":"0.0","userAdd":"0.0","exchange":"4536477535.9799995422"},{"date":"2026-07-23","userCross":"0.0","userAdd":"0.0","exchange":"4169194989.8200001717"},{"date":"2026-07-24","userCross":"0.0","userAdd":"0.0","exchange":"4202207563.6500000954"},{"date":"2026-07-25","userCross":"0.0","userAdd":"0.0","exchange":"1474606949.4700000286"},{"date":"2026-07-26","userCross":"0.0","userAdd":"0.0","exchange":"2009100758.3199999332"},{"date":"2026-07-27","userCross":"0.0","userAdd":"0.0","exchange":"4852093730.470000267"},{"date":"2026-07-28","userCross":"0.0","userAdd":"0.0","exchange":"4755335311.0799999237"},{"date":"2026-07-29","userCross":"0.0","userAdd":"0.0","exchange":"5566694383.9300003052"},{"date":"2026-07-30","userCross":"0.0","userAdd":"0.0","exchange":"1298327452.4500000477"}],"feeSchedule":{"cross":"0.00045","add":"0.00015","spotCross":"0.0007","spotAdd":"0.0004","tiers":{"vip":[{"ntlCutoff":"5000000.0","cro
  ...
```
{% endcode %}
