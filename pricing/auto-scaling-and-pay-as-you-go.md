---
icon: credit-card
---

# Auto-Scaling & Pay As You Go

## Auto-Scaling

The Auto-Scaling setting is the following automatic purchase strategy when the current RU packages are fully consumed. As the API keys are going to freeze when there is no remaining RUs, you can set the Auto-Scaling to any purchasable packages or Pay As You Go. When you set it to be the package, the system will automatically buy the package if the wallet balance is enough and the RU balance is 0.&#x20;

This setting can be done even if your account balance is not enough to purchase the package. When the system tries to auto-purchase the package when the remaining account fund is not enough, this setting will be automatically turned off.&#x20;

## Pay As You Go

Pay As You Go is a more flexible function of Auto-Scaling. When you set it to be Pay As You Go, the system will directly deduct the wallet balance for extra RU use if the wallet balance is greater than $0.01 and the RU balance meets 0. **The rate is 50000 RUs per $0.01**.&#x20;

{% hint style="info" %}
You can only choose one among Pay As You Go and other packages to be your Auto-Scaling strategy.&#x20;
{% endhint %}

Here are some use cases:

* You can set Pay As You Go for daily use and buy additional elementary or premium packages for a large traffic period.&#x20;
* You can also set elementary as your Auto-Scaling package and buy a premium package separately.&#x20;
* Or, you can just use the free package and enable Pay As You Go in case the balance runs out.&#x20;

{% hint style="info" %}
The RU consumption follows first expired, first consumed. You won’t lose any benefits for having different packages in your account.
{% endhint %}
