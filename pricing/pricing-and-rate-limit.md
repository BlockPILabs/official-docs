---
icon: square-dollar
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Pricing & Rate Limit

To meet the needs of customers with different usage volumes, we have designed three types of RU packages, free, elementary, and premium. If you have greater demand for RPC services and look for some customized service, please contact us and we are glad to customize an enterprise package for you. Each RU package has an expiration time. Make sure to schedule your purchasing plan or turn on the Auto-Scaling function.&#x20;

The Free package is not purchasable. It is designed as a gift package to be distributed to registered users on the 1st of every month.&#x20;

You can purchase packages before your current RU balance depletes. Please be aware that the validity period of any package you purchase begins immediately. If there are multiple existing packages in your account, the system adheres to a 'first expired, first consumed' policy for RU consumption, ensuring you don’t lose out on any benefits while managing multiple packages in your account.

## RU Packages

<table data-full-width="false"><thead><tr><th width="134">Package</th><th width="113">Price</th><th width="95">RUs</th><th width="105">Expiration</th><th width="173">Rate Limit</th><th width="312">Features</th></tr></thead><tbody><tr><td>Public RPC</td><td>-</td><td>-</td><td>-</td><td>10 requests/sec<br>200 RU/sec</td><td>-</td></tr><tr><td>Free</td><td>$0</td><td>50M</td><td>32 days</td><td>20 requests/sec<br>400 RU/sec</td><td><p>Archive data</p><p>Ticket support</p></td></tr><tr><td>Elementary</td><td>$49</td><td>500M</td><td>60 days</td><td>1000 requests/sec<br>40000 RU/sec</td><td><p>Archive data</p><p>Ticket support </p></td></tr><tr><td>Premium</td><td>$299</td><td>4,000M</td><td>90 days</td><td>2500 requests/sec<br>100000 RU/sec</td><td><p>Archive data</p><p>Ticket support </p><p>Technical consultant </p></td></tr><tr><td>Pay As You Go</td><td>$0.01</td><td>50000 </td><td>-</td><td>20 requests/sec<br>1000 RU/sec</td><td><p>Archive data</p><p>Ticket support </p><p>Technical consultant</p></td></tr><tr><td>Enterprise</td><td>Contact us</td><td>-</td><td>-</td><td>Custom</td><td><p>Archive data</p><p>Ticket support </p><p>Technical consultant </p><p>Dedicated telegram channel support</p></td></tr></tbody></table>

## Rate Limit Policy

To ensure a better user experience for all users, there are two types of rate limit in place: request volume and RU consumption. If either of these limits is exceeded, a rate limit error will be returned. When a user holds an RU package, the rate limit for that account will be determined by the value specified in that RU package. Please note the rate limit will be effective on a single endpoint.

When the Pay As You Go function is activated and the user has a positive account balance, it is equivalent to the user having an Free package.

Regardless of which RU package the user is using, when there are multiple RU packages associated with the account, the rate limit value will be determined by the **more advanced one**.

Here are scenarios to help you understand:

* _**Scenario 1**_\
  &#xNAN;_&#x49;f you have a premium package in your account, your rate will be 2500RPS and 100000 RUPS, even you are consuming the monthly free package._
* _**Scenario 2**_\
  &#xNAN;_&#x59;ou are using the monthly free package but have made deposit and set your Auto-Scaling to Pay As You Go. Your rate limit will be 20 RPS and 400 RUPS._
* _**Scenario 3**_\
  &#xNAN;_&#x59;ou are using the monthly free package and set your Auto-Scaling to Pay As You Go or any paid package, but your wallet balance is zero. Your rate limit will be 20RPS and 400RUPS._
