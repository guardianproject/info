---
id: 1708
title: Acrobits Groundwire – OSTN supports iPhone
date: 2012-03-21T09:09:21-04:00
author: lee
layout: post
guid: https://guardianproject.info/?p=1708
permalink: /2012/03/21/acrobits-groundwire-ostel-supports-iphone/
categories:
  - News
tags:
  - iphone
  - ostn
  - sip
  - voip
  - zrtp
---
The Guardian Project develops open source software primarily for the Android platform [but we strive for security by design to be a part of all platforms](https://guardianproject.info/home/use-cases/). With [OSTN](https://guardianproject.info/wiki/OSTN), there are two major components. The the first is the server, which operates as the primary user directory and call switch. The other is the client, which is the program you interact with to send and receive calls.

While the Apple App Store [forbids distribution of GPL licensed software from their service](http://michelf.com/weblog/2011/gpl-ios-app-store/), the underlying protocols used by OSTN are open, so even iPhone developers may implement them in a proprietary client application without breaking any intellectual property laws.

And Acrobits software, an iOS dev shop in Prague, Czech Republic did just that. The result is an excellent OSTN compilant app for iPhone called [Groundwire](http://www.acrobits.cz/11/acrobits-groundwire-for-iphone).

![Groundwire logo](http://www.acrobits.cz/userfiles/images/groundwire_icon.png) 

Groundwire is not cheap when compared to competing apps for Android or desktop computers. They distribute it as a [feature-limited](http://en.wikipedia.org/wiki/Crippleware) app for $9.99. Unfortunately, one of the limited features is required to bring the app up to [OSTN spec](https://guardianproject.info/wiki/OSTN_Compliance_Specification), namely ZRTP support. ZRTP is the key exchange protocol to securely authenticate two caller’s identities during a call. To enable this feature, the user must pay a $24.99 fee as an “in-app purchase.” This purchase is only required to enable **outgoing** ZRTP calls. If you don’t have a need for this, you must only pay the $9.99 purchase price to get up and running.

The good news is that Groundwire is an excellent app. I’m testing it on an original iPhone with firmware 3.1.3. It supports push notifications to receive incoming calls even when the iPhone is asleep or Groundwire is in the background. This feature depends on Acrobits secure push servers, and a full security audit has not yet been performed to determine if this creates a risk.

I expect Groundwire to be a very popular client for OSTel, due to the high number of iPhones in the field. If you’d like to sign up for our alpha tested, named OSTel.me, [fill out the form](https://ostel.me/) and we’ll be in touch soon thereafter. You can also checkout another OSTN-compliant service at Tanstagi: <https://tanstagi.net/>