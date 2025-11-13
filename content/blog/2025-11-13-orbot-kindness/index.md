---
title: "Kindness Mode: Help People Connect to Tor on World Kindness Day"
author: n8fr8
categories:
  - News
tags:
  - free software
  - open source
  - sharing
  - tor
  - community
---

Today is [World Kindness Day](https://en.wikipedia.org/wiki/World_Kindness_Day). As stated on Wikipedia, "World Kindness Day is to highlight good deeds in the community focusing on the positive power and the common thread of kindness for good which binds us."

<a href="https://en.wikipedia.org/wiki/World_Kindness_Day"><img src="worldkindnessday.png" width=200/></a>

Now that world __bind__ is particularly meaningful to use in a technical way - when a remote computer connects to another computer over a network, whether peer-to-peer or a server, one way to state what happens is "binding to their socket port". Especially considering something like the [tor network](https://torproject.org), which is powered by volunteer organizations and inviduals around the world sharing their network resources, there is a great deal of positive, community "good which binds us" going on.

So on this auspicious day of kindness, we wanted to share some new guidance we have put together about __KINDNESS MODE__, a feature for helping others in need, available in our app, [Orbot for Android and iOS](https://orbot.app). Kindness Mode is our name for the underlying technology also known as "Snowflake", which helps people get around extreme forms of network censorship and filtering.

## Running a Snowflake Proxy

Running a [Snowflake Proxy](https://snowflake.torproject.org) is one of the easiest, safest, and most impactful ways to help people circumvent censorship, especially if you’re in a place with an open and free internet. Your device, through your public IP address, becomes an essential bridge for people where Tor is blocked (in, say, Iran or China) and the entrance to the Tor network. There are many ways you can run a Snowflake Proxy:

* Orbot’s “Kindness Mode” on iOS and Android: https://orbot.app/kindness
* Snowflake add-on for Firefox, Chrome or Edge: https://snowflake.torproject.org
* WEPN home device: https://we-pn.com/kindness-faq.html

## Key Facts to Know

* You are not using Tor yourself, you are simply a bridge for someone else.
* All of the data passing through your device is encrypted; nothing is visible to you.
* There will be an impact on your bandwidth, but it is minimal, and you can set limits.

[![Kindness Mode diagram](kindessmode1.jpg)](kindessmodehandout.pdf)

## Risks and Considerations

1. Legality

* In most countries, running a Snowflake Proxy is legal. It’s equivalent to making an online “VOIP” call between two points on the internet.
* In high-censorship networks, this traffic could draw attention, and since your internet is not free and open, it doesn’t make sense to run a Snowflake Proxy.

2. Privacy and IP Visibility
* The fact that your device was connected to by a remote device on the internet can be seen and logged by your internet service provider.  
* Your IP address will appear in the central Snowflake “Broker” logs since it is necessary to share your proxy’s existence so others can find it.
* In the app or browser activity of the person you are helping, YOUR IP address is NOT visible and there is no link to your or your device.

3. Network and Bandwidth load
* Any data used by the device proxying through your connection will count as data on your service or plan. It is best on wifi or with unlimited plans.
* Proxying can slow your connection slightly. However by default only a very limited number of devices can use your proxy at a time.

## How to Minimize Risks

* Run Snowflake from a trusted, unrestricted, unlimited network.
* Don’t use it on shared, public, or corporate networks where administrators might block or misinterpret traffic.
* When you can, set limits to when and how the Snowflake Proxy should be available.

## Orbot is Kind!

Now that you have all this important knowledge, you can understand better if you are in a position to be kind, and share your network. [Get Orbot Today](https://orbot.app/downlaod) and see how good it feels each time someone connects through your Kindness Mode Snowflake Proxy!

[View our Orbot Kindness Mode How-To Guide PDF](kindessmodehandout.pdf)


