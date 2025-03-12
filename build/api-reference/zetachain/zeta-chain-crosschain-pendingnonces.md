---
description: Parameters queries the parameters of the module.
---

# /zeta-chain/crosschain/pendingNonces

#### **Parameters:**

**None**

#### Example:

{% code overflow="wrap" %}
```json
// Request
curl -X GET -H 'Content-Type: application/json' https://zetachain.blockpi.network/lcd/v1/<your-api-key>/zeta-chain/crosschain/pendingNonces

// Result
{
  "pending_nonces": [
    {
      "nonce_low": "0",
      "nonce_high": "0",
      "chain_id": "18332",
      "tss": ""
    },
    {
      "nonce_low": "0",
      "nonce_high": "0",
      "chain_id": "5",
      "tss": ""
    },
    {
      "nonce_low": "0",
      "nonce_high": "0",
      "chain_id": "7001",
      "tss": ""
    },
    {
      "nonce_low": "0",
      "nonce_high": "0",
      "chain_id": "80001",
      "tss": ""
    },
    {
      "nonce_low": "0",
      "nonce_high": "0",
      "chain_id": "97",
      "tss": ""
    },
    {
      "nonce_low": "0",
      "nonce_high": "1",
      "chain_id": "18332",
      "tss": "zetapub1addwnpepq28c57cvcs0a2htsem5zxr6qnlvq9mzhmm76z3jncsnzz32rclangr2g35p"
    },
    {
      "nonce_low": "22",
      "nonce_high": "22",
      "chain_id": "5",
      "tss": "zetapub1addwnpepq28c57cvcs0a2htsem5zxr6qnlvq9mzhmm76z3jncsnzz32rclangr2g35p"
    },
    {
      "nonce_low": "0",
      "nonce_high": "0",
      "chain_id": "7001",
      "tss": "zetapub1addwnpepq28c57cvcs0a2htsem5zxr6qnlvq9mzhmm76z3jncsnzz32rclangr2g35p"
    },
    {
      "nonce_low": "19",
      "nonce_high": "19",
      "chain_id": "80001",
      "tss": "zetapub1addwnpepq28c57cvcs0a2htsem5zxr6qnlvq9mzhmm76z3jncsnzz32rclangr2g35p"
    },
    {
      "nonce_low": "26",
      "nonce_high": "26",
      "chain_id": "97",
      "tss": "zetapub1addwnpepq28c57cvcs0a2htsem5zxr6qnlvq9mzhmm76z3jncsnzz32rclangr2g35p"
    },
    {
      "nonce_low": "0",
      "nonce_high": "0",
      "chain_id": "18332",
      "tss": "zetapub1addwnpepqfapt52wqw6k2kv0kvkuf8u0e8l37q57ntau7qu5ppz9sh690cs9cg0yxzs"
    },
    {
      "nonce_low": "1",
      "nonce_high": "1",
      "chain_id": "5",
      "tss": "zetapub1addwnpepqfapt52wqw6k2kv0kvkuf8u0e8l37q57ntau7qu5ppz9sh690cs9cg0yxzs"
    },
    {
      "nonce_low": "0",
      "nonce_high": "0",
      "chain_id": "7001",
      "tss": "zetapub1addwnpepqfapt52wqw6k2kv0kvkuf8u0e8l37q57ntau7qu5ppz9sh690cs9cg0yxzs"
    },
    {
      "nonce_low": "1",
      "nonce_high": "1",
      "chain_id": "80001",
      "tss": "zetapub1addwnpepqfapt52wqw6k2kv0kvkuf8u0e8l37q57ntau7qu5ppz9sh690cs9cg0yxzs"
    },
    {
      "nonce_low": "2",
      "nonce_high": "2",
      "chain_id": "97",
      "tss": "zetapub1addwnpepqfapt52wqw6k2kv0kvkuf8u0e8l37q57ntau7qu5ppz9sh690cs9cg0yxzs"
    }
  ]
}
```
{% endcode %}
