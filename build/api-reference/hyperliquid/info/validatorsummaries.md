# validatorSummaries

#### Parameters

type: validatorSummaries

#### Returns

Validator information including staking amounts, uptime, and commission rates.

#### Example

{% code overflow="wrap" %}
```json
// Request
curl https://hyperliquid.blockpi.network/v1/info/your-api-key -X POST -H "Content-Type: application/json" --data '{"type":"validatorSummaries"}'

// Result
[{"validator":"0x000000000056f99d36b6f2e0c51fd41496bbacb8","signer":"0x0000000008b0b558419582041f85740344ae8fde","name":"ValiDAO","description":"The People’s Validator. Zero seed oils. Yours truly. https://validao.xyz","nRecentBlocks":1,"stake":668366174204757,"isJailed":false,"unjailableAfter":null,"isActive":true,"commission":"0.04","stats":[["day",{"uptimeFraction":"1.0","predictedApr":"0.021572699","nSamples":1440}],["week",{"uptimeFraction":"0.9970238095","predictedApr":"0.0215084945","nSamples":10080}],["month",{"uptimeFraction":"0.9993055556","predictedApr":"0.0215577179","nSamples":43200}]]},{"validator":"0x15458aed3c7a49b215fbfa863c6ff550c31e1a31","signer":"0x21d50a1c2e70b2b4b25516c744da7f1de760b2ec","name":"B-Harvest","description":"Provides secure validation services for dPoS networks(https://bharvest.io)","nRecentBlocks":1,"stake":517171222410213,"isJailed":false,"unjailableAfter":null,"isActive":true,"commission":"0.05","stats":[["day",{"uptimeFraction":"1.0","predictedApr":"0.0213479834","nSamples":1440}],["week",{"uptimeFraction":"1.0","predictedApr":"0.0213479834","nSamples":10080}],["month",{"uptimeFraction":"1.0","predictedApr":"0.0213479834","nSamples":43200}]]},{"validator":"0x30c66ebc7f5ef4f340b424a26e4d944f60129815","signer":"0xc304bcea88f450f3367bf5df3eea30eef4f0e9e9","name":"Bitwise Onchain Solutions x FalconX","description":"Trusted infrastructure for institutions. This node combines Bitwise Onchain Solutions' institutional-grade staking to deliver op
  ...
```
{% endcode %}
