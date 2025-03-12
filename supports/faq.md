---
description: >-
  Below are the frequently asked questions from users, which we have organized
  into an FAQ for easier reference.
icon: message-question
---

# FAQ

### **How can I open archive mode/get historical data?**

If you require access to data from earlier blocks, you can utilize the Archive Mode. This feature enables users to retrieve and access the complete historical data of the blockchain. You can enable it in your API List or the endpoint page. [Click here to see the tutorial.](../basic-tutorials/api-key/customize-endpoint-advanced-features.md)\
Please note it will take a few minutes for the setting to be effective after you toggle the switch.

### **How can I resolve a 429 error?**

We recognize the importance of keeping our customers' applications responsive and available at all times. To prevent abuse, we have implemented a rate limit. Exceeding this limit will result in a 429 Too Many Requests error.\
You can view your current rate limit on the dashboard. If you require a higher rate limit, please consider upgrading your package, and the new rate limit may take a few minutes to be effective. [Click here to get more details.](../pricing/pricing-and-rate-limit.md)

### **How many endpoints can I create in my account?**

The current maximum number of endpoints per user account is 50.

### **Why are there no responses/timeout to any requests when using a WSS?**

A long-term connection over WSS may result in requests not being responded to, which could be caused by network fluctuations or variations in server hardware performance. We recommend that users of WSS maintain heartbeat checks and implement reconnections if the heartbeat response time is too long or if there is no response.

### **Do you support archive nodes on all the blockchain networks?**

[Click here to check the full list of supported network and Archive Mode.](../build/supported-networks-and-advanced-features.md)

### **How can I resolve {code: -32000, message: missing trie node} error?**

Please enable Archive Model to solve this error. Please note it will take a few minutes for the setting to be effective after you toggle the switch.

### **If the $49 Elementary package is not enough for my monthly usage and the $299 Premium package is way too much for me, what should I do?**

You can buy packages any time. For example, if you buy a package on the 10th of the month, and you consume it all on the 20th. You can buy a package on the 20th. Also, we recommend you set up your Auto-scaling package. [Please check more details about the Auto-scaling here.](../pricing/auto-scaling-and-pay-as-you-go.md)

### **What is the validity period of the packages? And how is it calculated?**

The validity period of the Elementary and Premium packages is 60 days and 90 days respectively. The validity period will start counting when you purchase the package. If you have more than one package in your account, **the system will consume the package that expires first.**

&#x20;For example, if you have purchased an Elementary and a Premium package at the same time, the system will consume the Elementary package first. Don't worry, **the rate limit will be based on the Premium package level.**

We recommend that you set your Auto-Scaling to avoid waste. [Please check more details about the Auto-scaling here.](../pricing/auto-scaling-and-pay-as-you-go.md)

### **Why don't we support the custom tracer in the Debug methods?**

Custom tracers incur significant system cost, so we are unable to provide them in our general services. Otherwise this would lead to an increase in service prices for all users. If debug\_traceCall with a custom tracer is an essential requirement for you, you may need to consult with our dedicated node service. [https://blockpi.io/?contact=sale](https://blockpi.io/?contact=sale)

### **Why do I get SSLCertVerificationError?**

This is an issue with the user's own sever environment. Please check SSL certificate.
