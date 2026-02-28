# VerifySignature

#### **Parameters:**

**address** - [string](https://docs.sui.io/references/fullnode-protocol#string)  Address to validate against the provided signature. If provided, this address will be compared against the the address derived from the provide signature and a successful response will only be returned if they match.

**jwks** - [ActiveJwk](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-ActiveJwk) The set of JWKs to use when verifying Zklogin signatures. If this is empty the current set of valid JWKs stored onchain will be used

**message** - [Bcs](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-Bcs) The message to verify against. Today the only supported message types are `PersonalMessage` and `TransactionData` and the `Bcs.name` must be set to indicate which type of message is being verified.

**signature** - [UserSignature](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2beta2-UserSignature) The siganture to verify.

#### **Returns:**

**is\_valid** - [bool](https://docs.sui.io/references/fullnode-protocol#bool) Indicates if the provided signature was valid given the requested parameters.

**reason** - [string](https://docs.sui.io/references/fullnode-protocol#string) If `is_valid` is `false`, this is the reason for why the signature verification failed.

#### Example:

{% code overflow="wrap" %}
```json
grpcurl -proto .sui/rpc/v2/signature_verification_service.proto
-H "x-token: YOUR_TOKEN_VALUE" 
-d 
'{
  "signature": [ ... ]

}' 
sui.blockpi.network:443 sui.rpc.v2beta.SignatureVerificationService/VerifySignature
```
{% endcode %}
